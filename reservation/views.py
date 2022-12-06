from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from reservation.models import Reservation


from .serializers import  reservationSerializer

# Create your views here.

class reservationsList(APIView):
    
    def get(self, request, *args, **kwargs):
        try:
            Matricule = request.query_params["Matricule"]
            if Matricule != None:
                reservation = Reservation.objects.get(Matricule=Matricule)
                serializer = reservationSerializer(reservation)       
        except:
            reservation1 = None
            serializer = reservationSerializer(reservation1, many = True)

        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        pass

