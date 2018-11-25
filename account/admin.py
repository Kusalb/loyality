from django.contrib import admin
from django.contrib.auth.models import Group

from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
# Register your models here.
from .models import Waiter

from .models import offer

from .models import Partner

from .models import Discount

from .models import Customer

from .models import Promotion

from .models import Trasaction

from .models import UserId

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser




admin.site.register(Waiter)
admin.site.register(offer)
admin.site.register(Partner)
admin.site.register(Discount)
admin.site.register(Customer)
admin.site.register(Promotion)
admin.site.register(Trasaction)
admin.site.register(UserId)

admin.site.unregister(Group)


admin.site.site_header = 'Loyalty App'
admin.site.index_title = 'Dashboard'


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username']


admin.site.register(CustomUser, CustomUserAdmin)
