from django.urls import path
from blog import views

urlpatterns = [
    path('',views.signup,name='signup'),
    path('login/',views.login,name='login'),
    path('newblog/',views.newblog,name='newblog'),
    path('logout/',views.logout,name='logout'),
    path('home/',views.home,name='home'),
    
]