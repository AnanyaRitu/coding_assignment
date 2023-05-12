from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from rest_framework.routers import DefaultRouter
from users.views import UserViewSet, UserCreate, SalesViewSet, SalesReport
from django.urls import path, re_path, include, reverse_lazy

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'sales', SalesViewSet)

urlpatterns = [
    # Your URLs...
        path('api/v1/', include(router.urls)),
    path('api/v1/registration/', UserCreate.as_view(), name='registration'),
    path('api/v1/sales_report/', SalesReport.as_view(), name='sales_report'),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]