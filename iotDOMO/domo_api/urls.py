from django.urls import path
from . import views
urlpatterns=[
    path("location/",views.Locations_method.as_view(),name="location"),
    path("location/<int:codigo>/",views.Locations_method.as_view(),name="location_parametro"),
    path("devices/",views.Devices_method.as_view(),name="devices"),
    path("devices/<int:codigo>/",views.Devices_method.as_view(),name="devices_parametro"),
    path("dots/",views.Dots_method.as_view(),name="dots"),
    path("dots/<int:codigo>/",views.Dots_method.as_view(),name="dots_parametro")
]