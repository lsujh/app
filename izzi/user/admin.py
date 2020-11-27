from datetime import datetime

from django.shortcuts import redirect, render
from django.urls import path
from django.contrib import admin
from django.conf import settings

from .models import User, Order
from .forms import CsvImportForm


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    change_list_template = 'admin/model_change_list.html'
    def get_urls(self):
        urls = super().get_urls()
        my_urls = [path('import-csv/', self.import_csv),]
        return my_urls + urls
    def import_csv(self, request):
        if request.method == 'POST':
            csv_file = request.FILES.get('csv_file')
            try:
                file_type = str(csv_file).split('.')[1]
            except:
                file_type = None
            if file_type in settings.CONTENT_TYPES:
                create = 0
                try:
                    for row, line in enumerate(csv_file):
                        line = line.decode().strip().split(',')
                        if row==0:
                            continue
                        obj, created = User.objects.update_or_create(first_name = line[0], last_name = line[1],
                                                   date_of_birth = datetime.strptime(line[2], '%Y/%m/%d'),
                                                   defaults={'registration_date':datetime.strptime(line[3], '%Y/%m/%d')})
                        create += int(created)
                    self.message_user(request, f'З файлу "{csv_file}" було опрацьовано {row} рядків, і успішно імпортовано {create} користувачів')
                except Exception as err:
                    self.message_user(request, f'Помилка "{str(err)}" при завантаженню з файла "{csv_file}"', 'error')
            else:
                self.message_user(request, f'Помилка імпорту з файлу "{csv_file}". Тип файлу "{file_type}" не підтримується', 'error')
                return redirect('.')
            return redirect('..')
        form = CsvImportForm()
        payload = {'form': form}
        return render(request, 'admin/csv_form.html', payload)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    pass



