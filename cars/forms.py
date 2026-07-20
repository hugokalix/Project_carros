from django import forms
from cars.models import Car


class CarModelForm(forms.ModelForm): #estou dizendo para o django que estou mapeando
    class Meta:
        model = Car
        fields = '__all__' #Essa string eu pego todos os campos

    def clean_value(self):
        value = self.cleaned_data.get('value') #O self é uma instancia do proprio form
        if value < 20000:
            self.add_error('value', 'Valor mínimo do carro deve ser de R$20.000')
        return value

    def clean_factory_year(self):
        factory_year = self.cleaned_data.get('factory_year') #capturando o valor do campo
        if factory_year < 1975:
            self.add_error('factory_year', 'Não é possível cadastrar carros fabricados antes de 1975')
        return factory_year


