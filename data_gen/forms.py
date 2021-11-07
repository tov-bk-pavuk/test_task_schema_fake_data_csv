from django import forms


class AmountForm(forms.Form):
    data_gen_amount = forms.IntegerField(label='Rows')
