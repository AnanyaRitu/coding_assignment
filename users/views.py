from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from django.template.loader import get_template
import pdfkit
from django.http import HttpResponse
from django.shortcuts import render
from django.db.models import Count
from .models import CustomUser, Sales
from .serializers import UserSerializer, UserRegSerializer, SalesSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

class UserCreate(generics.CreateAPIView):
    model = get_user_model()
    serializer_class = UserRegSerializer

class SalesViewSet(viewsets.ModelViewSet):
    queryset = Sales.objects.all()
    serializer_class = SalesSerializer
    permission_classes = [IsAuthenticated]

class SalesReport(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, format=None):
        data = dict()
        data["total_orders"] = Sales.objects.count()
        data["distinct_customer"] = Sales.objects.all().values('customer_id').distinct().count()
        template = get_template('home.html')
       
        html = template.render({"context":data})
        
        print(html)
        pdf = pdfkit.from_string(html, False)

        filename = "sample_pdf.pdf"

        response = HttpResponse(pdf, content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="' + filename + '"'
        return response
        

