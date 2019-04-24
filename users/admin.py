from django.contrib import admin
#from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from users.forms import UserAdminCreationForm, UserAdminChangeForm
from .models import MyUser, Country, GradeUser, UserProfile
# Register your models here.

class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('email', 'username','admin')
    list_filter = ('admin',)
    searc_fields = ('username', 'email')
    fieldsets = (
        (None, {'fields': ('email', 'username', 'password', 'last_login')}),
        ('Personal info', {'fields': ()}),
        ('Permissions', {'fields': ()}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'password1', 'password2')}
        ),
    )
    search_fields = ('email',)
    ordering = ('username',)
    filter_horizontal = ()


admin.site.register(MyUser, UserAdmin)
class UserProfileModel(admin.ModelAdmin):
    list_display = ('user' ,'country', 'grade', 'reputation', 'sign_up_time', 'profile_views_')
    list_filter = ('grade', 'country')
    search_fields = ('user', 'country', 'grade' )
    def profile_views_(self, instance):
        return instance.profile_views.all().count()

admin.site.register(UserProfile, UserProfileModel)
admin.site.register(Country)
admin.site.register(GradeUser)



# Remove Group Model from admin. We're not using it.
