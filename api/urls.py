from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from api.views import CreateUserView,TargetListView,TargetRetrieveView,TargetViewSet

router = routers.DefaultRouter()
router.register('targets',TargetViewSet,basename='targets')

urlpatterns = [
    path('list-target/',TargetListView.as_view(),name='list-target' ),
    path('detail-target/<str:pk>/',TargetRetrieveView.as_view(),name='detail-target' ),
    path('register/',CreateUserView.as_view(), name='register'),
    path('auth/',include('djoser.urls.jwt')),
    path('', include(router.urls)),
]

