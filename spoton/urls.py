from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from applications.order.urls import order_router
from applications.user.urls import user_router
from spoton import settings

router = routers.DefaultRouter()
router.registry.extend(order_router.registry)
router.registry.extend(user_router.registry)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]

if settings.DEBUG:
    schema_view = get_schema_view(
       openapi.Info(
          title="SpotOn API",
          default_version='v1',
          description="SpotOn API",
          terms_of_service="",
          contact=openapi.Contact(email="kndzh7@gmail.com"),
       ),
       public=True,
       permission_classes=(permissions.AllowAny,),
    )

    swagger_urls = [
        path(r'api/swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
        path(r'api/redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc-ui'),
    ]

    urlpatterns = urlpatterns + swagger_urls
