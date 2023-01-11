
from django.urls import include, path
from . import views
from rest_framework_nested import routers

router = routers.DefaultRouter()
router.register('products', views.ProductViewSet, basename='products')
router.register('collections', views.CollectionViewSet)

products_router = routers.NestedDefaultRouter(router, 'products', lookup = 'product')
products_router.register('reviews', views.ReviewViewSet, basename = 'product-reviews')


# URLConf

# urlpatterns = router.urls + products_router.urls

urlpatterns = [
    path(r'', include(router.urls)),
    path(r'', include(products_router.urls))
]
