from rest_framework import generics, permissions
from .models import LostItem, FoundItem, Match
from .serializers import LostItemSerializer, FoundItemSerializer, MatchSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from django.db.models import Q


# LOST ITEMS
class LostItemListCreateView(generics.ListCreateAPIView):
    queryset = LostItem.objects.all()
    serializer_class = LostItemSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


# FOUND ITEMS
class FoundItemListCreateView(generics.ListCreateAPIView):
    queryset = FoundItem.objects.all()
    serializer_class = FoundItemSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


# MATCHED ITEMS LIST VIEW
class MatchListView(generics.ListAPIView):
    queryset = Match.objects.all()
    serializer_class = MatchSerializer
    permission_classes = [permissions.IsAuthenticated]

from .models import Claim
from .serializers import ClaimSerializer

class ClaimListCreateView(generics.ListCreateAPIView):
    queryset = Claim.objects.all()
    serializer_class = ClaimSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

# MATCHING ENGINE (for demo, naive logic)
class RunMatchingEngineView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        lost_items = LostItem.objects.all()
        found_items = FoundItem.objects.all()
        matches_created = 0

        for lost in lost_items:
            for found in found_items:
                if lost.category == found.category:
                    if not Match.objects.filter(lost_item=lost, found_item=found).exists():
                        Match.objects.create(
                            lost_item=lost,
                            found_item=found,
                            confidence_score=90.0  # Example fixed score
                        )
                        matches_created += 1

        return Response({"matches_created": matches_created})
