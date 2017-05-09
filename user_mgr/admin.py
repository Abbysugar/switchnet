from django.contrib import admin

from user_mgr.models import FriendList, UserAccount, Address
# Register your models here.

admin.site.register(FriendList)
admin.site.register(UserAccount)
admin.site.register(Address)
