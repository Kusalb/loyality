from django.shortcuts import get_object_or_404
from django.shortcuts import redirect, render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.urls import reverse_lazy
from django.http.response import HttpResponse
from rest_framework import status
from .models import Waiter
from .models import offer
from .models import Partner
from .models import Promotion
from .models import Trasaction
from.models import Discount
from .models import Customer
from .models import UserId
from .serializer import WaiterSerializer
from .serializer import offerSerializer
from .serializer import PartnerSerializer
from .serializer import TransactionSerializer
from .serializer import PromotionSerializer
from.serializer import DiscountSerializer
from.serializer import CustomerSerializer
from .serializer import UserIdSerializer
# from django.urls import path
# from . import views


from .forms import CustomUserCreationForm
from django.views import generic

# from django.template import  loader
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



class DiscountList(APIView):

    def get(self,request):
        user1= Discount.objects.all()
        serializer1 = DiscountSerializer(user1, many=True)
        return Response (serializer1.data)

    def post(self):
        pass

class CustomerList(APIView):

    def get(self,request):
        user2= Customer.objects.all()
        serializer2 = CustomerSerializer(user2, many=True)
        return Response (serializer2.data)

    def post(self):
        pass


class UserIdList(APIView):

    def get(self,request):
        user2= UserId.objects.all()
        serializer2 = UserIdSerializer(user2, many=True)
        return Response (serializer2.data)

    def post(self):
        pass


# def LoginView(request):
#
#     return render(request, 'login/login.html')


class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'



