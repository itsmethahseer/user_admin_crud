from django.urls import path
from . import views
urlpatterns = [
    path('', views.sign, name='signup'),
    path('user_home', views.Homepage, name='user_home'),
    path('login', views.login_page, name='login'),
    path('logout',views.Logoutpage,name='logout'),
    path('adminlogin',views.adminlogin,name='adminlogin'),
    path('adminpage',views.adminpage,name='adminpage'),
    path('admin_delete <int:id>',views.admin_delete,name='admin_delete'),
    path('admin_logout',views.admin_logout,name='adminlogout'),
    path('user_insert <int:id>',views.user_insert,name='user_insert'),
    path('add_user',views.add_user,name='add_user'),
    path('search',views.search,name='search'),




]
