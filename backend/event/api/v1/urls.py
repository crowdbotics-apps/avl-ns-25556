from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import (
    VendorViewSet,
    LocationViewSet,
    FavoritesViewSet,
    VendorDetailViewSet,
    CategoryViewSet,
    FaqViewSet,
    PresenterViewSet,
    ScheduleViewSet,
    MyScheduleViewSet,
    SponsorViewSet,
)

router = DefaultRouter()
router.register("sponsor", SponsorViewSet)
router.register("favorites", FavoritesViewSet)
router.register("faq", FaqViewSet)
router.register("presenter", PresenterViewSet)
router.register("vendordetail", VendorDetailViewSet)
router.register("vendor", VendorViewSet)
router.register("myschedule", MyScheduleViewSet)
router.register("category", CategoryViewSet)
router.register("schedule", ScheduleViewSet)
router.register("location", LocationViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
