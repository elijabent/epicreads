from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'app'

urlpatterns = [
    path('', views.index_request, name='index'),
    path('catalog/', views.catalog_request, name='catalog'),
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('admin_dashboard/new_book/', views.admin_dashboard_new_book, name="admin_dashboard_new_book"),
    path('admin_dashboard/edit_book/<int:id>/', views.admin_dashboard_edit_book, name="admin_dashboard_edit_book"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
