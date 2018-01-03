from django.conf.urls import url, include
from inventory import views

app_name = 'inventory'

urlpatterns = [
    url(r'^$', views.EquipmentListView.as_view(), name='list'),
    url(r'^dashboard/', views.DashboardListView.as_view(), name='dashboard'),
    url(r'^(?P<pk>\d+)/$', views.EquipmentDetailView.as_view(), name='detail'),
]
