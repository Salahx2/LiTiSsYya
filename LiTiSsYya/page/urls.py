from . import views
from django.urls import path

urlpatterns = [
    path('about/',views.About,name="About"),
    path('privacy_policy/',views.Privacy,name="Privacy"),
    path('terms/',views.Terms,name="Terms"),
    path('docs/',views.Docs,name="Docs")
]