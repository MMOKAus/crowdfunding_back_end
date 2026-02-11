from rest_framework import serializers
from django.apps import apps
from django.db.models import Sum
from django.db.models.functions import Coalesce

class PledgeSerializer(serializers.ModelSerializer):
    supporter = serializers.ReadOnlyField(source="supporter.id")
    supporter_username = serializers.ReadOnlyField(source="supporter.username")

    class Meta:
        model = apps.get_model("fundraisers.Pledge")
        fields = "__all__"
        read_only_fields = ["supporter"]


class FundraiserSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.id')
    total_pledged = serializers.SerializerMethodField()
    class Meta:
        model = apps.get_model('fundraisers.Fundraiser')
        fields = '__all__'
        read_only_fields = ['owner', 'date_created']

class FundraiserDetailSerializer(FundraiserSerializer):
    pledges = PledgeSerializer(many=True, read_only=True)
    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.goal = validated_data.get('goal', instance.goal)
        instance.image = validated_data.get('image', instance.image)
        instance.is_open = validated_data.get('is_open', instance.is_open)
        #instance.owner = validated_data.pop('owner', None)
        instance.save()
        return instance
    
def get_total_pledged(self, obj):
        # Uses the related name "pledges" from FundraiserDetailSerializer
        return obj.pledges.aggregate(total=Coalesce(Sum("amount"), 0))["total"]
