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
from .forms import CustomUserCreationForm
from django.views import generic
from .models import Partner, Promotion
from .forms import PartnerForm,WaiterForm, PromotionForm
from .models import Waiter


from django.views.generic import(
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

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


def partner_list(request):
    partners = Partner.objects.all()
    return render(request, 'account/partner/partner_list.html', {'partners':partners})

def partner_detail(request, pk):
    partner = get_object_or_404(Partner, pk=pk)
    return render(request, 'account/partner/partner_detail.html', {'partners': partner})

def partner_new(request):
    if request.method == "POST":
       form = PartnerForm(request.POST)
       if form.is_valid():
           partner = form.save(commit=False)
           partner.save()
           return redirect('partner_list')
    else:
        form = PartnerForm()
    return render(request, 'account/partner/partner_edit.html', {'form': form})


def partner_edit(request, pk):
    partner = get_object_or_404(Partner, pk=pk)
    if request.method == "POST":
        form = PartnerForm(request.POST, instance=partner)
        if form.is_valid():
            partner = form.save(commit=False)
            partner.save()
            return redirect('partner_list')
    else:
        form = PartnerForm(instance=partner)

    return render(request, 'account/partner/partner_edit.html', {'form': form})


def partner_delete(request, pk):
  partner = get_object_or_404(Partner, pk=pk)
  partner.delete()
  return redirect('partner_list')



def waiter_list(request):
    waiters = Waiter.objects.all()
    return render(request, 'account/waiter/waiter_list.html', {'waiters':waiters})

# def partner_detail(request, pk):
#     partner = get_object_or_404(Partner, pk=pk)
#     return render(request, 'polls/partner/partner_detail.html', {'partners': partner})

def waiter_new(request):
    if request.method == "POST":
       form = WaiterForm(request.POST)
       if form.is_valid():
           waiter = form.save(commit=False)
           waiter.save()
           return redirect('waiter_list')
    else:
        form = WaiterForm()
    return render(request, 'account/waiter/waiter_edit.html', {'form': form})


def waiter_edit(request, pk):
    waiter = get_object_or_404(Waiter, pk=pk)
    if request.method == "POST":
        form = WaiterForm(request.POST, instance=waiter)
        if form.is_valid():
            waiter = form.save(commit=False)
            waiter.save()
            return redirect('waiter_list')
    else:
        form = WaiterForm(instance=waiter)

    return render(request, 'account/waiter/waiter_edit.html', {'form': form})


def waiter_delete(request, pk):
  waiter = get_object_or_404(Waiter, pk=pk)
  waiter.delete()
  return redirect('waiter_list')


def promotion_list(request):
    promotion = Promotion.objects.all()
    return render(request, 'account/promotion/promotion_list.html', {'promotion': promotion})


def promotion_new(request):
    if request.method == "POST":
        form = PromotionForm(request.POST)
        if form.is_valid():
            promotion = form.save(commit=False)
            promotion.save()
            return redirect('promotion_list')
    else:
        form = PromotionForm()
    return render(request, 'account/promotion/promotion_edit.html', {'form': form})


def promotion_edit(request, pk):
    promotion = get_object_or_404(Promotion, pk=pk)
    if request.method == "POST":
        form = PromotionForm(request.POST, instance=promotion)
        if form.is_valid():
            promotion = form.save(commit=False)
            promotion.save()
            return redirect('promotion_list')
    else:
        form = PromotionForm(instance=promotion)

    return render(request, 'account/promotion/promotion_edit.html', {'form': form})


def promotion_delete(request, pk):
    promotion = get_object_or_404(Promotion, pk=pk)
    promotion.delete()
    return redirect('promotion_list')










