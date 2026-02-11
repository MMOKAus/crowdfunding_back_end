from rest_framework import serializers
from django.apps import apps
from django.db.models import Sum


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

    def get_total_pledged(self, obj):
        total = obj.pledges.aggregate(total=Sum("amount"))["total"]
        return total or 0

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
    

