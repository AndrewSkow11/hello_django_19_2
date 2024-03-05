from django import forms

from catalog.models import Product, Version


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ProductForm(StyleFormMixin, forms.ModelForm):
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

    stop_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево',
                  'бесплатно', 'обман', 'полиция', 'радар']

    def clean_nomination(self):
        nomination = self.cleaned_data['nomination']
        for word in self.stop_words:
            if word in nomination:
                raise forms.ValidationError(f'Запрещено использовать {self.stop_words}')
        return nomination

    def clean_description(self):
        description = self.cleaned_data['description']
        for word in self.stop_words:
            if word in description:
                raise forms.ValidationError(f'Запрещено использовать {self.stop_words}')

        return description


class VersionForm(forms.ModelForm):
    class Meta:
        model = Version
        fields = '__all__'

