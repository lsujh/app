from datetime import date

from rest_framework import generics
from rest_framework.response import Response

from .serializers import UserSerializer
from .models import User


class UserViews(generics.ListAPIView):
    """
       GET Request YYYY-MM-DD
       Response body
       [
         {
        "first_name": "Іван",
        "last_name": "Іванов",
        "date_of_birth": "1985-11-10",
        "registration_date": "2020-11-19"
         }
       ]
       """
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get(self, request, *args, **kwargs):
        if self.kwargs:
            registration_date = date(self.kwargs['year'], self.kwargs['month'], self.kwargs['day'])
            queryset = self.get_queryset().filter(registration_date=registration_date)
        else:
            queryset = self.get_queryset()

        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)
