from django.urls import path
from .views import GenerationCreateView, GenerationDetailView

urlpatterns = [
    path("", GenerationCreateView.as_view(), name="generation-create"),
    path("<uuid:generation_id>/", GenerationDetailView.as_view(), name="generation-detail"),
]
