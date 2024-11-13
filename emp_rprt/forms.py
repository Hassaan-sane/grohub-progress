from django import forms
from .models import Products, EmpUser


class UsernameLoginForm(forms.Form):
    username = forms.CharField(label="Username", max_length=100)

class UploadFileForm(forms.Form):
    file = forms.FileField()
    
class dataEntryForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = ["title", "sku", "quantity", "details", "sp" ,"cp", "size"]
    # title = forms.CharField(label="title", max_length=100)
    # sku = forms.CharField(label='sku', max_length=7)
    # quantity = forms.IntegerField(label = 'quantity', min_value=0, max_value=1000)
    # sp = forms.IntegerField(label = 'sp', min_value=0, max_value=100000)
    # cp = forms.IntegerField(label = 'cp', min_value=0, max_value=100000)
    # details = forms.CharField(label='colors',max_length=100) 


# Using Django's built-in user model


class UserDateSelectionForm(forms.Form):
    user = forms.ModelChoiceField(queryset=EmpUser.objects.filter(is_superuser=False), required=True)
    date_range = forms.ChoiceField(
        choices=[
            ('1', 'Yesterday'),
            ('7', 'Last 7 days'),
            ('15', 'Last 15 days'),
            ('30', 'Last 30 days'),
        ],
        required=True,
        label="Select Date Range"
    )
