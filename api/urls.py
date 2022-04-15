from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from api.views import CreateUserView,\
    LargeListView,LargeRetrieveView,LargeViewSet,\
    MiddleListView,MiddleRetrieveView,MiddleViewSet,\
    TaskListView,TaskRetrieveView,TaskViewSet


router = routers.DefaultRouter()
router.register('larges',LargeViewSet,basename='larges')
router.register('middles',MiddleViewSet,basename='middles')
router.register('tasks',TaskViewSet,basename='tasks')

urlpatterns = [
    path('list-large/',LargeListView.as_view(),name='list-large' ),
    path('detail-large/<str:pk>/',LargeRetrieveView.as_view(),name='detail-large' ),
    path('list-middle/',MiddleListView.as_view(),name='list-middle' ),
    path('detail-middle/<str:pk>/',MiddleRetrieveView.as_view(),name='detail-middle' ),
    path('list-task/',TaskListView.as_view(),name='list-task' ),
    path('detail-task/<str:pk>/',TaskRetrieveView.as_view(),name='detail-task' ),
    path('register/',CreateUserView.as_view(), name='register'),
    path('auth/',include('djoser.urls.jwt')),
    path('', include(router.urls)),
]

