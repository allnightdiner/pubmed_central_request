from django import forms

class PMCRequestForm(forms.Form):
   pmc_id = forms.IntegerField() 
