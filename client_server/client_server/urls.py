from django.contrib import admin
from django.urls import path
from order.views import OrderView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('order/', OrderView.as_view()),
]
