from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .views import  InstituteListView, InstituteDetailView,InstituteCreateView,InstituteUpdateView,InstituteDeleteView 
from .views import  DirectionListView, DirectionDetailView,DirectionCreateView,DirectionUpdateView,DirectionDeleteView 
from . import views

app_name = 'UMK'
urlpatterns = [
    #path('institutes/',views.get_institutes, name='institutes'),
    #path('directions/',views.get_directions, name='directions'),
    path('get_document/<int:file_id>/', views.get_document, name ='document'),
    path('institutes/', InstituteListView.as_view(), name='institutes'),
    path('institutes/new/', InstituteCreateView.as_view(), name='institute_new'),
    path('institutes/<int:pk>/', InstituteDetailView.as_view(), name='institute_detail'),
    path('institutes/<int:pk>/edit/',InstituteUpdateView.as_view(), name = 'institute_edit'),
    path('institutes/<int:pk>/delete/',InstituteDeleteView.as_view(), name = 'institute_delete'),
    path('directions/', DirectionListView.as_view(), name='directions'),
    path('directions/generate/', views.downloadWord, name='generate'),
    path('directions/new/', DirectionCreateView.as_view(), name='direction_new'),
    path('directions/<int:pk>/', DirectionDetailView.as_view(), name='direction_detail'),
    path('directions/<int:pk>/edit/',DirectionUpdateView.as_view(), name = 'direction_edit'),
    path('directions/<int:pk>/delete/',DirectionDeleteView.as_view(), name = 'direction_delete'),
    

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)