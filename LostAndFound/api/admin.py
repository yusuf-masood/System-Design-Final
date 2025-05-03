from django.contrib import admin
from .models import LostItem, FoundItem, Match, Claim

admin.site.register(LostItem)
admin.site.register(FoundItem)
admin.site.register(Match)
admin.site.register(Claim)
