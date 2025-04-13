from django.urls import path
from . import views

urlpatterns = [
    path('',views.greeting_function,name="index"),
    path('about',views.about_function,name="about"),
    path('add/<int:a>/<int:b>',views.add_function,name="add"),
    path('intro/<str:name>/<int:age>',views.intro_function,name="intro"),
    path('first_page',views.first_page,name="first_page")
]