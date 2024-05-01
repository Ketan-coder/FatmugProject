from django.urls import path
from .views import (
    VendorViewSet,
    PurchaseOrderViewSet,
    HistoricalPerformanceModelViewSet,
)

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path("vendors/", VendorViewSet.as_view({"get": "list", "post": "create"})),
    path("vendors/<int:pk>/",VendorViewSet.as_view({"get": "retrieve", "put": "update", "delete": "destroy"})),
    path("purchase_orders/",PurchaseOrderViewSet.as_view({"get": "list", "post": "create"})),
    path("purchase_orders/<int:pk>/",PurchaseOrderViewSet.as_view({"get": "retrieve", "put": "update", "delete": "destroy"})),
    path("purchase_orders/<int:pk>/acknowledge/",PurchaseOrderViewSet.as_view({"post": "acknowledge"})),
    path("vendors/<int:pk>/performance/",HistoricalPerformanceModelViewSet.as_view({"get": "retrieve"})),
]
