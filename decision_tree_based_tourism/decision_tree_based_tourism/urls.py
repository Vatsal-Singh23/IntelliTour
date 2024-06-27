from django.contrib import admin
from django.urls import path
from tree.views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index,name='index'),
    path('login',login,name='login'),
    path('signup',signup,name='signup'),
    path('admin_home',admin_home,name='admin_home'),
    path('user_home',user_home,name='user_home'),
    path('logout',logout,name='logout'),
    path('users',users,name='users'),
    path('delete_user/<int:id>',delete_user,name='delete_user'),
    path('edit_profile',edit_profile,name='edit_profile'),
    path('add_package',add_package,name='add_package'),
    path('manage_package',manage_package,name='manage_package'),
    path('delete_package/<int:id>',delete_package,name='delete_package'),
    path('edit_package/<int:id>',edit_package,name='edit_package'),
    path('view_packages',view_packages,name='view_packages'),
    path('book_package/<int:id>',book_package,name='book_package'),
    path('my_booking',my_booking,name='my_booking'),
    path('view_booking',view_booking,name='view_booking'),
    path('search',search,name='search'),
    path('search2',search2,name='search2'),


]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
