from django import forms
from .models import Coupon

class CouponCreateForm(forms.ModelForm):
    class Meta:
        model = Coupon
        fields = ['coupon_type', 'name', 'start', 'end', 'quantity', 'photo', 'shop', 'code' ]

        def clean_category(self):
            coupon_type = self.cleaned_data.get('coupon_type')
            if not coupon_type:
                raise forms.ValidationError('This field is required')
            
            for instance in Coupon.objects.all():
                if instance.coupon_type == coupon_type:
                    raise forms.ValidationError( coupon_type + 'already exists')
                return coupon_type
        
        def clean_name(self):
            name = self.cleaned_data.get('name')
            if not name:
                raise forms.ValidationError('This field is required')
                return name
            
            for instance in Coupon.objects.all():
                if instance.coupon_type == name:
                    raise forms.ValidationError( name + 'already exists')
            return name

class CouponSearchForm(forms.ModelForm):
    class Meta:
        model = Coupon
        fields = ['coupon_type', 'shop']


class CouponUpdateForm(forms.ModelForm):
    class Meta:
        model = Coupon
        fields = ['coupon_type', 'name', 'quantity']