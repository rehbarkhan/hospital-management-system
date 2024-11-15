from django.urls import path
from .views import IndexView, AuthView, LogoutView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('login/', AuthView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]