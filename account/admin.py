from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import *
from django.contrib.auth import get_user_model
from .forms import UserAdminCreationForm,UserAdminChangeForm
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

User=get_user_model()


class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('email','D_O_B', 'admin')
    list_filter = ('admin','staff','active','applicant','accountant')
    fieldsets = (
        (None, {'fields': ('email','password',)}),
        ('Personal info', {'fields': ('D_O_B', 'disability','genotype','blood_group','parent_office','home_address','phone','contact_address','admission_no','maiden_no','domination',
                    'home_town','place_of_birth','Religion','profile_image','state_of_origin','local_government','gender','marital_status','Age','country','entry_class','othername','first_name','surname',)}),
        ('Permissions', {'fields': ('admin','staff','active','applicant','accountant')}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email','D_O_B','disability','genotype','blood_group','parent_office','home_address','phone','contact_address','admission_no','maiden_no','domination',
                    'home_town','place_of_birth','Religion','profile_image','state_of_origin','local_government','gender','marital_status','Age','country','entry_class','othername','first_name','surname', 'password1', 'password2')}
        ),
    )
    search_fields = ('email','D_O_B','disability','genotype','blood_group','parent_office','home_address','phone','contact_address','admission_no','maiden_no','domination',
                    'home_town','place_of_birth','Religion','profile_image','state_of_origin','local_government','gender','marital_status','Age','country','entry_class','othername','first_name','surname',)
    ordering = ('email','D_O_B','disability','genotype','blood_group','parent_office','home_address','phone','contact_address','admission_no','maiden_no','domination',
                    'home_town','place_of_birth','Religion','state_of_origin','local_government','gender','marital_status','Age','country','entry_class','othername','first_name','surname',)
    filter_horizontal = ()


# Remove Group Model from admin. We're not using it.
admin.site.unregister(Group)
admin.site.site_header="Prestige International College Admin"
# admin.site.register(Language)
# admin.site.register(Framework)
admin.site.register(User, UserAdmin)
# Register your models here.
