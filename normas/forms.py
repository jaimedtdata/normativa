from django import forms

class EditForm(forms.Form):
    norma = forms.CharField(max_length=200)
    name_denom = forms.CharField(max_length=100)
    base_legal = forms.CharField(max_length=200)
    fecha_publi = forms.DateInput()
    