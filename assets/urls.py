from rest_framework.routers import SimpleRouter

from .views import AssetViewSet, RequestViewSet


router = SimpleRouter()
router.register('assets', AssetViewSet, basename='asset')
router.register('requests', RequestViewSet, basename='request')
urlpatterns = router.urls
