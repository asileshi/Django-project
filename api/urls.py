from home import views
from django.urls import path
urlpatterns = [
    path('index/', views.index,name=''),
    path('person/',views.person,name='person/')
]
