from rest_framework import serializers
from .models import Vendor, PurchaseOrder, HistoricalPerformanceModel


class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = "__all__"


class VendorPerformanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = [
            "name",
            "on_time_delivery_rate",
            "quality_rating_avg",
            "average_response_time",
            "fulfillment_rate",
        ]


class PurchaseOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseOrder
        fields = "__all__"


class HistoricalPerformanceModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoricalPerformanceModel
        fields = "__all__"
