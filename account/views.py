from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Waiter
from .models import offer
from .models import Partner
from .models import Promotion
from .models import Trasaction
from .serializer import WaiterSerializer
from .serializer import offerSerializer
from .serializer import PartnerSerializer
from .serializer import TransactionSerializer
from .serializer import PromotionSerializer



# Create your views here.

class WaiterList(APIView):

    def get(self, request):
        users = Waiter.objects.all()
        serializer = WaiterSerializer(users, many=True)
        return Response(serializer.data)

    def post(self):
        pass


class offerList(APIView):
    def get(self, request):
        offers = offer.objects.all()
        serializer = offerSerializer(offers, many=True)
        return Response(serializer.data)

    def post(self, request):
        pass


class PromotionList(APIView):
    def get(self, request):
        promotions = Promotion.objects.all()
        serializer = PromotionSerializer(promotions, many=True)
        return Response(serializer.data)

    def post(self, request):
        pass


class PartnerList(APIView):
    def get(self, request):
        partners = Partner.objects.all()
        serializer = PartnerSerializer(partners, many=True)
        return Response(serializer.data)

    def post(self, request):
        pass


class TransactionList(APIView):
    def get(self, request):
        Trasactions = Trasaction.objects.all()
        serializer = TransactionSerializer(Trasactions, many=True)
        return Response(serializer.data)

    def post(self, request):
        pass


