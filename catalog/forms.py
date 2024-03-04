from django import forms

from catalog.models import Product

class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'
        # fields = ('nomination',
        #           'description',
        #           'imagine_url',
        #           'category',
        #           'created_at',
        #           'updated_at',
        #           'manufactured_at')
        # exclude =  ('manufactured_at', )

