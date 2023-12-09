from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('items/', views.MenuItemsView.as_view()),
    path('<int:pk>', views.SingleMenuItemView.as_view()),
]