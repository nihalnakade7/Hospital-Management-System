
from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.index,name='index'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('accounts/',include('accounts.urls'),name='accounts'),
    path('appointments/',views.appointments,name='appointments'),
    path('invoice/',views.invoice,name='invoice'),
    path('profile/',views.profile,name='profile'),
    path('med_history/',views.med_history,name='med_history'),
    path('res_dashboard/',views.res_dashboard,name='res_dashboard'),
    path('create_app/',views.create_app,name='create_app'),
    path('update_user/',views.update_user,name='update_user'),
    path('del_confirm/del_user/',views.del_user,name='del_user'),
    path('del_confirm/',views.del_confirm,name='del_confirm'),
    path('hr_dashboard/',views.hr_dashboard,name='hr_dashboard'),



]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)