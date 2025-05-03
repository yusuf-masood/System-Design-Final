from django.urls import path
from .views import (
    LostItemListCreateView,
    FoundItemListCreateView,
    MatchListView,
    ClaimListCreateView,
    RunMatchingEngineView
)

urlpatterns = [
    path('lost-items/', LostItemListCreateView.as_view(), name='lost-items'),
    path('found-items/', FoundItemListCreateView.as_view(), name='found-items'),
    path('matches/', MatchListView.as_view(), name='matches'),
    path('claims/', ClaimListCreateView.as_view(), name='claims'),
    path('run-matching/', RunMatchingEngineView.as_view(), name='run-matching'),
]
