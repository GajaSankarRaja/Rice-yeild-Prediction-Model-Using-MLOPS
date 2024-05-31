from django.urls import path
from . import views

urlpatterns = [
    path('', views.UserInputViewSet.as_view({'post': 'create'}), name='userinput-create'),
    # Add other URL patterns as needed
]
