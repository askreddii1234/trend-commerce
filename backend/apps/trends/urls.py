from django.urls import path
from .views import TrendDetailView, TrendListView

urlpatterns = [
    path("", TrendListView.as_view(), name="trend-list"),
    path("<slug:slug>/", TrendDetailView.as_view(), name="trend-detail"),
]
