from django.urls import path
from .views import initiate_payment, callback,user_view

urlpatterns = [
    path('pay/', initiate_payment, name='pay'),
    path('callback/', callback, name='callback'),
    path('',user_view,)
]
