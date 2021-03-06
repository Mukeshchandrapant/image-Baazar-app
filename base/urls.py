from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('',views.aboutus, name = 'aboutus'),
    path('home/',views.home, name = 'home'),
    path('category/<int:cid>/', views.show_category, name = 'category')

] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
