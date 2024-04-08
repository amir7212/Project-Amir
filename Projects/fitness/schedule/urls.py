from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from schedule.views import RoleViewSet, UserProfileViewSet, GymViewSet, TrainerViewSet, ScheduleViewSet, BookingViewSet

router = DefaultRouter()
router.register(r'roles', RoleViewSet)
router.register(r'userprofiles', UserProfileViewSet)
router.register(r'gyms', GymViewSet)
router.register(r'trainers', TrainerViewSet)
router.register(r'schedules', ScheduleViewSet)
router.register(r'bookings', BookingViewSet)

urlpatterns = [
    path('', include(router.urls)),
]