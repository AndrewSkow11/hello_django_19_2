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

    stop_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево',
                  'бесплатно', 'обман', 'полиция', 'радар']

    def clean_nomination(self):
        nomination = self.cleaned_data['nomination']
        for word in self.stop_words:
            if word in nomination:
                raise forms.ValidationError(f'Запрещено использовать {self.stop_words}')

        return nomination

    # def clean_nomination(self):
    #     cleaned_data = self.cleaned_data.get('nomination')
    #
    #     if '1234' not in cleaned_data:
    #         raise forms.ValidationError('Очень плохое слово')

            # for word in self.stop_words:
            #     if word in cleaned_data:
            #         raise forms.ValidationError('Ипользовано запрещённое слово')

        return cleaned_data

        # def clean_description(self):

