from django.db.models import Avg, F
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import HistoricalPerformanceModel, PurchaseOrder


@receiver(post_save, sender=PurchaseOrder)
def update_performance_metrics(sender, instance, created, **kwargs):
    """
    Signals to handle when a PurchaseOrder is created or updated
    """
    if instance.status == "COMPLETED":
        vendor = instance.vendor
        completed_pos = PurchaseOrder.objects.filter(vendor=vendor, status="COMPLETED")
        total_completed = completed_pos.count()

        # On-Time Delivery Rate
        on_time_count = completed_pos.filter(
            delivery_date__lte=F("planned_delivery_date")
        ).count()
        if total_completed > 0:
            vendor.on_time_delivery_rate = (on_time_count / total_completed) * 100
        else:
            vendor.on_time_delivery_rate = 0

        # Quality Rating Average
        vendor.quality_rating_avg = (
            completed_pos.aggregate(Avg("quality_rating"))["quality_rating__avg"] or 0
        )

        # Average Response Time (this calculation needs adjustment based on actual date fields)
        if instance.acknowledgement_date is not None:
            total_response_time = completed_pos.annotate(
                response_time=F("acknowledgement_date") - F("issue_date")
            ).aggregate(Avg("response_time"))["response_time__avg"]
            if total_response_time is not None:
                vendor.average_response_time = (
                    total_response_time.total_seconds() / 3600
                )
            else:
                vendor.average_response_time = 0

        # Fulfillment Rate
        vendor.fulfillment_rate = (
            (completed_pos.filter(no_issues=True).count() / total_completed) * 100
            if total_completed > 0
            else 0
        )

        vendor.save()

        # Update Historical Performance
        historyperformance, _ = HistoricalPerformanceModel.objects.get_or_create(
            vendor=vendor
        )
        historyperformance.on_time_delivery_rate = vendor.on_time_delivery_rate
        historyperformance.quality_rating_avg = vendor.quality_rating_avg
        historyperformance.average_response_time = vendor.average_response_time
        historyperformance.fulfillment_rate = vendor.fulfillment_rate
        historyperformance.save()
