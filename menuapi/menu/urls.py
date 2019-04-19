from django.urls import path
from .views import MenuView
from .views import MenuSectionView

app_name = "menu"

urlpatterns = [
    path('menu/', MenuView.as_view(), name='list'),
    path('menu/<int:pk>/', MenuSectionView.as_view(), name='detail')
]