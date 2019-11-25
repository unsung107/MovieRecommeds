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
    # print(request.data)
    # date_of_birth = int(request.data.get('birthday')[0:4])
       
    # today = date.today()
    # today = int(datetime.strftime(today, '%Y'))
    # age = today - date_of_birth + 1
    
    # form.data['age'] = age
    # print(form.data)
    if form.is_valid():
        print('dd')
        form.save()
    return Response(form.data)
    pass
 