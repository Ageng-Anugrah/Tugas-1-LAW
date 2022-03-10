from django.urls import path
from .views import *

urlpatterns = [
    path('token/', GetToken.as_view()),
    path('resource/', GetResource.as_view()),
]
