from django.urls import path
from .views import GenerationCreateView, GenerationDetailView, GenerationImageView

urlpatterns = [
    path("", GenerationCreateView.as_view(), name="generation-create"),
    path("<uuid:generation_id>/", GenerationDetailView.as_view(), name="generation-detail"),
    path("<uuid:generation_id>/image/", GenerationImageView.as_view(), name="generation-image"),
]
