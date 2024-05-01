from django.db import models
import uuid


def generate_order_id(vendorName) -> str:
    """
    Generate a unique ID from a UUID
    """
    unique_id = str(uuid.uuid4().fields[-1])[:8]
    order_id = f"{vendorName[2]}{unique_id}"
    return order_id


class Vendor(models.Model):
    name: str = models.CharField(max_length=50)
    contact_details: str = models.TextField()
    address: str = models.TextField()
    vendor_code: str = models.CharField(max_length=15, unique=True)
    on_time_delivery_rate: float = models.FloatField(null=True, blank=True)
    quality_rating_avg: float = models.FloatField(null=True, blank=True)
    average_response_time: float = models.FloatField(null=True, blank=True)
    fulfillment_rate: float = models.FloatField(null=True, blank=True)

    def __str__(self) -> str:
        return self.vendor_code + self.name


DELIVERY_STATUS = (
    ("PENDING", "PENDING"),
    ("COMPLETED", "COMPLETED"),
    ("CANCELLED", "CANCELLED"),
)


class PurchaseOrder(models.Model):
    po_number: str = models.CharField(max_length=15, unique=True)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)
    delivery_date = models.DateTimeField()
    items = models.JSONField()
    quantity: int = models.IntegerField(default=0)
    status: str = models.CharField(max_length=10, choices=DELIVERY_STATUS)
    quality_rating: float = models.FloatField()
    issue_date = models.DateTimeField(auto_now_add=True)
    acknowledgement_date = models.DateTimeField(null=True, blank=True)
    is_acknowledged: bool = models.BooleanField(default=False)
    no_issues: bool = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.po_number + self.vendor.name

    def save(self, *args, **kwargs):
        if not self.po_number:
            self.po_number = generate_order_id(self.vendor.name)
        super(PurchaseOrder, self).save(*args, **kwargs)


class HistoricalPerformanceModel(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    on_time_delivery_rate: float = models.FloatField()
    quality_rating_avg: float = models.FloatField()
    average_response_time: float = models.FloatField()
    fulfillment_rate: float = models.FloatField()

    def __str__(self) -> str:
        return self.vendor.vendor_code + self.vendor.name

    def save(self):
        get_vendor = Vendor.objects.get_or_create(vendor=self.vendor)
        get_vendor.on_time_delivery_rate = self.on_time_delivery_rate
        get_vendor.quality_rating_avg = self.quality_rating_avg
        get_vendor.average_response_time = self.average_response_time
        get_vendor.fulfillment_rate = self.fulfillment_rate
        get_vendor.save()
        super().save()
