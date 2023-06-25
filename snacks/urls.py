from django.urls import path
from .views import SnackListView, SnackDetailView, SnackAboutView, SnackCreateView, SnackDeleteView


urlpatterns = [
    path('', SnackListView.as_view(), name='snack_list'),
    path('<int:pk>/', SnackDetailView.as_view(), name='snack_detail'),
    path('about', SnackAboutView.as_view(), name='snack_about'),
    path('create/', SnackCreateView.as_view(), name='snack_create'),
    path('<int:pk>/delete', SnackDeleteView.as_view(), name='snack_delete'),
]
