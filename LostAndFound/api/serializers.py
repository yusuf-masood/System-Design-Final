from rest_framework import serializers
from .models import LostItem

class LostItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = LostItem
        fields = '__all__'
        read_only_fields = ['user']  # 🔑 this tells DRF not to expect it in the request

from .models import FoundItem

class FoundItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoundItem
        fields = '__all__'
        read_only_fields = ['user']

from .models import Match

class MatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Match
        fields = '__all__'

from .models import Claim
from rest_framework import serializers

class ClaimSerializer(serializers.ModelSerializer):
    class Meta:
        model = Claim
        fields = '__all__'
        read_only_fields = ['user', 'submitted_at', 'verified_by']
