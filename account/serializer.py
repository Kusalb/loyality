from rest_framework import serializers

from .models import Waiter
from .models import offer
from .models import Partner
from .models import Trasaction
from .models import Promotion

class WaiterSerializer(serializers.ModelSerializer):

    class Meta:
        model = Waiter
        fields = ('username', 'email')
        # fields = '__all__'
        # for returning all values


class offerSerializer(serializers.ModelSerializer):

    class Meta:
        model = offer
        fields = '__all__'


class PartnerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Partner
        fields = '__all__'

class PromotionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Promotion
        fields = '__all__'


class TransactionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Trasaction
        fields = '__all__'