
from django.urls import include, path
from . import views
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('products', views.ProductViewSet)
router.register('collections', views.CollectionViewSet)


# URLConf
urlpatterns = [
    path('', include(router.urls))

#     path('products/', views.ProductList.as_view()),
#     path('products/<int:pk>/', views.ProductDetails.as_view()),
#     path('collections/<int:pk>/', views.CollectionDetials.as_view(), name = 'Collection-detail'),
#     path('collections/', views.CollectionList.as_view()),
]
