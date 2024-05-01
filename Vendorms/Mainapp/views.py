from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
import datetime
from .signals import update_performance_metrics
from .models import Vendor, PurchaseOrder, HistoricalPerformanceModel
from .serializers import (
    VendorSerializer,
    PurchaseOrderSerializer,
    VendorPerformanceSerializer,
)
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication


class VendorViewSet(viewsets.ViewSet):
    # permission_classes = [IsAuthenticated]
    """
    API endpoint that allows vendors to be viewed or edited.
    """
    def list(self, request):
        vendors = Vendor.objects.all()
        serializer = VendorSerializer(vendors, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = VendorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        vendor = Vendor.objects.get(pk=pk)
        serializer = VendorSerializer(vendor)
        return Response(serializer.data)

    def update(self, request, pk=None):
        vendor = Vendor.objects.get(pk=pk)
        serializer = VendorSerializer(vendor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        vendor = Vendor.objects.get(pk=pk)
        vendor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def get_queryset(self):
        queryset = Vendor.objects.all()
        return queryset


class PurchaseOrderViewSet(viewsets.ViewSet):
    # permission_classes = [IsAuthenticated]
    """
    API endpoint that allows purchase orders to be viewed or edited.
    """
    def list(self, request):
        purchase_orders = PurchaseOrder.objects.all()
        serializer = PurchaseOrderSerializer(purchase_orders, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = PurchaseOrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        purchase_order = PurchaseOrder.objects.get(pk=pk)
        serializer = PurchaseOrderSerializer(purchase_order)
        return Response(serializer.data)

    def update(self, request, pk=None):
        purchase_order = PurchaseOrder.objects.get(pk=pk)
        serializer = PurchaseOrderSerializer(purchase_order, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        purchase_order = PurchaseOrder.objects.get(pk=pk)
        purchase_order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def mark_as_acknowleged(self, request, pk=None):
        purchase_order = PurchaseOrder.objects.get(pk=pk)
        purchase_order.acknowledgement_date = datetime.date.today()
        purchase_order.is_acknowledged = True
        purchase_order.save()
        update_performance_metrics(purchase_order)
        return Response(status=status.HTTP_200_OK)

    def get_queryset(self):
        queryset = PurchaseOrder.objects.all()
        return queryset


class HistoricalPerformanceModelViewSet(viewsets.ViewSet):
    # permission_classes = [IsAuthenticated]
    """
    API endpoint that allows vendors/performance to be viewed or edited.
    """
    def retrieve(self, request, pk=None):
        vendor = Vendor.objects.get(pk=pk)
        serializer = VendorPerformanceSerializer(vendor)
        return Response(serializer.data)

    def get_queryset(self):
        historyPerformance = HistoricalPerformanceModel.objects.all()
        return historyPerformance
