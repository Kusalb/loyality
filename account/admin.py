from django.contrib import admin

# Register your models here.
from .models import User

from .models import offer

from .models import Partner

from .models import DiscountAmount

from .models import CustomerInfo

from .models import Promotion

from .models import Trasaction


admin.site.register(User)
admin.site.register(offer)
admin.site.register(Partner)
admin.site.register(DiscountAmount)
admin.site.register(CustomerInfo)
admin.site.register(Promotion)
admin.site.register(Trasaction)

