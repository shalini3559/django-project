from django.urls import path
from .import views
urlpatterns=[
    path('', views.myapp, name='myapp'),
    path('login', views.userLogin, name=''),
    path('prod_details/<int:id>',views.prod_details, name= "prod_details" ),
    path('user_details/<int:pk>',views.user_details, name= "user_details" ),
]