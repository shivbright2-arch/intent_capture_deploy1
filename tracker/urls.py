from django.urls import path
from . import views

urlpatterns = [
    #path('members/', views.members, name='members'),
    path('printed-vest-for-men/', views.printed_vest),
    path('track-flipkart-click/', views.track_flipkart_click),
]