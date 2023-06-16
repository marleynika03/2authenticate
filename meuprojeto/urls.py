from django.views.generic.base import TemplateView
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from django.conf import settings

from doisfatores import views

router = DefaultRouter()
router.register("user", views.UserViewSet, basename="user")

urlpatterns = [
    path('', TemplateView.as_view(template_name='login.html'), name='home'),
    path('admin/', admin.site.urls),
    path('api-auth/', include("rest_framework.urls"))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += router.urls
