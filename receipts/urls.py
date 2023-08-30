from django.urls import path
from .views import receipt_list

app_name = "receipts"

urlpatterns = [
    path("", receipt_list, name="home"),
]
