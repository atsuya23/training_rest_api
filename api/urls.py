from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from api.views import TrainingViewSet, TrainingListView, TrainingRetrieveView, \
    ContentRetrieveView, ContentListView, CreateUserView

router = routers.DefaultRouter()
router.register('training', TrainingViewSet, basename='training')

urlpatterns = [
    path('list-training/', TrainingListView.as_view(), name='list-training'),
    path('detail-training/<str:pk>/', TrainingRetrieveView.as_view(), name='detail-training'),
    path('list-content/', ContentListView.as_view(), name='list-content'),
    path('detail-content/<str:pk>', ContentRetrieveView.as_view(), name='detail-content'),
    path('register/', CreateUserView.as_view(), name='register'),
    path('auth/', include('djoser.urls.jwt')),
    path('', include(router.urls)),
]
