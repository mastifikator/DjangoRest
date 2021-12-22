from django import forms


class UserForm(forms.Form):
    first_value = forms.IntegerField(
        label="Введите первозе значение", required=True)
    second_value = forms.IntegerField(
        label="Введите второе значение", required=True)
