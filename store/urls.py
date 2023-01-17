
from django.urls import include, path
from . import views
from rest_framework_nested import routers

router = routers.DefaultRouter()
router.register('products', views.ProductViewSet, basename='products')
router.register('collections', views.CollectionViewSet)
router.register('carts', views.CartViewSet)
router.register('customers', views.CustomerViewSet)


products_router = routers.NestedDefaultRouter(router, 'products', lookup = 'product')
products_router.register('reviews', views.ReviewViewSet, basename = 'product-reviews')

carts_router =  routers.NestedDefaultRouter(router, 'carts', lookup = 'cart')
carts_router.register('items', views.CartItemViewSet, basename = 'carts-items')


urlpatterns = router.urls + products_router.urls + carts_router.urls

# cart_router = routers.NestedDefaultRouter(router, 'cart', lookup = 'id')

# URLConf

# urlpatterns = router.urls + products_router.urls

# urlpatterns = [
#     path(r'', include(router.urls)),
#     path(r'', include(products_router.urls)),
#     path(r'', include(carts_router.urls))
# ]
