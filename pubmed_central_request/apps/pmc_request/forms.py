from django import forms

class PMCRequestForm(forms.Form):
   pmc_id = forms.IntegerField() 

class PMCRequestAcceptForm(forms.Form):
    accept_article = forms.BooleanField()
