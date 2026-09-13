from rest_framework.generics import ListAPIView, RetrieveAPIView
from .models import TrendProduct
from .serializers import TrendProductSerializer

class TrendListView(ListAPIView):
    serializer_class = TrendProductSerializer
    queryset = TrendProduct.objects.filter(status="active")

class TrendDetailView(RetrieveAPIView):
    serializer_class = TrendProductSerializer
    lookup_field = "slug"
    queryset = TrendProduct.objects.filter(status="active")
