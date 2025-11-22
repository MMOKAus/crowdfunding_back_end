from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from .models import Fundraiser
from .models import Fundraiser, Pledge
from .serializers import FundraiserSerializer
from .serializers import FundraiserSerializer, PledgeSerializer, FundraiserDetailSerializer

class FundraiserList(APIView):
    def get(self, request):
        fundraisers = Fundraiser.objects.all()
        serializer = FundraiserSerializer(fundraisers, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = FundraiserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
class FundraiserDetail(APIView):
        def get_object(self, pk):
            try:
                fundraiser = Fundraiser.objects.get(pk=pk)
                return fundraiser
            except Fundraiser.DoesNotExist:
                raise Http404

        def get(self, request, pk):
            fundraiser = self.get_object(pk)
            serializer = FundraiserDetailSerializer(fundraiser)
            return Response(serializer.data)
        
class PledgeList(APIView):

    def get(self, request):
        pledges = Pledge.objects.all()
        serializer = PledgeSerializer(pledges, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PledgeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )