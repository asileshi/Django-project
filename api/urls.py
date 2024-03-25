from home import views
from django.urls import path
urlpatterns = [
    path('index/', views.index,name=''),
    path('person/',views.person,name='person/'),
    path('login/',views.login,name='login'),
    path('persons/',views.PersonApi.as_view())
]
