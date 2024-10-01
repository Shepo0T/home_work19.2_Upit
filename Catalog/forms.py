from django import forms
from django.forms import BooleanField

from Catalog.models import Product, Version

forbidden_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']

class StyleFormMixin:
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, BooleanField):
                field.widget.attrs['class'] = 'form-check-input'
            else:
                field.widget.attrs['class'] = 'form-control'


class ProductForm(StyleFormMixin, forms.ModelForm):

    class Meta:
        model = Product
        fields = ('name', 'description', 'category', 'is_active', 'purchase_price', 'preview', 'owner' )

    def clean_name(self):
        cleaned_name = self.cleaned_data['name']
        for word in forbidden_words:
            if  word in cleaned_name:
                raise forms.ValidationError('Содержит запрещенные слова')

        return cleaned_name

    def clean_description(self):
        cleaned_description = self.cleaned_data['description']
        for word in forbidden_words:
            if word in cleaned_description:
                raise forms.ValidationError('Содержит запрещенные слова')

        return cleaned_description

class VersionForm(StyleFormMixin, forms.ModelForm):

    class Meta:
         model = Version
         fields = '__all__'

class ProductModeratorForm(StyleFormMixin, forms.ModelForm):

    class Meta:
        model = Product
        fields = ('description', 'category', 'is_active')

    def clean_name(self):
        cleaned_name = self.cleaned_data['name']
        for word in forbidden_words:
            if  word in cleaned_name:
                raise forms.ValidationError('Содержит запрещенные слова')

        return cleaned_name

    def clean_description(self):
        cleaned_description = self.cleaned_data['description']
        for word in forbidden_words:
            if word in cleaned_description:
                raise forms.ValidationError('Содержит запрещенные слова')

        return cleaned_description