from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm

from multidb.products.models import Product
from .models import User,Database


class UserCreationFormExtended(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(UserCreationFormExtended, self).__init__(*args, **kwargs)
        self.fields['databases'] = forms.ModelMultipleChoiceField(label="Select Databases", queryset=Database.objects.all())

class MyUserChangeForm(UserChangeForm):

    class Meta(UserChangeForm.Meta):
        model = User


class MyUserCreationForm(UserCreationForm):

    error_message = UserCreationForm.error_messages.update(
        {"duplicate_username": "This username has already been taken."}
    )

    class Meta(UserCreationForm.Meta):
        model = User

    def clean_username(self):
        username = self.cleaned_data["username"]
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username

        raise forms.ValidationError(self.error_messages["duplicate_username"])


@admin.register(User)
class MyUserAdmin(AuthUserAdmin):
    form = MyUserChangeForm
    add_form = UserCreationFormExtended
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('databases', 'username', 'password1', 'password2',)
        }),
    )
    fieldsets = (("User Profile", {"fields": ("name",)}),) + AuthUserAdmin.fieldsets
    list_display = ("username", "name", "is_superuser")
    search_fields = ["name"]

admin.site.register(Database)
admin.site.register(Product)
