# users/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, Waiter, Promotion, Partner


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username', 'email')


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email')


class PartnerForm(forms.ModelForm):

    class Meta:
        model = Partner
        fields = ('Partner_company', 'Associted_person', 'email' , 'Phone_number')


class WaiterForm(forms.ModelForm):

    class Meta:
        model = Waiter
        fields = ('username', 'password', 'email')

class PromotionForm(forms.ModelForm):
    class Meta:
        model = Promotion
        fields = ('Partner', 'Valid_till', 'Approved', 'description')



