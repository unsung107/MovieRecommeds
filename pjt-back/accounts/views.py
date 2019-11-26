from django.shortcuts import render
from .forms import CustomUserCreationForm
from .serializer import UserSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from datetime import date, datetime


@api_view(['POST'])
@permission_classes([AllowAny])
def signup(request):
    form = CustomUserCreationForm(data=request.data)
    if form.is_valid():
        form.save()
        return Response(form.data)
    return Response(form.errors)
    
 