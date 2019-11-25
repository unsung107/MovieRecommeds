from django.shortcuts import render
from .forms import CustomUserCreationForm
from .serializer import UserSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from pprint import pprint
# Create your views here.

@api_view(['POST'])
@permission_classes([AllowAny])
def signup(request):
    form = CustomUserCreationForm(data=request.data)
    print(form.data)
    pprint(form)
    print(form.is_valid())
    if form.is_valid():
        print('들어오니')
        form.save()
        print(form)
    return Response(form.data)
    

