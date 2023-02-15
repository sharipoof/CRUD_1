from django import forms
from . import models

class ArtcileFrom(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'input'}), label="Name:")
    description = forms.CharField(widget=forms.TextInput(attrs={'class':'input'}),label="Description")
    price = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'input'}),label="Price") 
    category = forms.CharField(widget=forms.TextInput(attrs={'class':'input'}), label="Category")

    class Meta:
        model = models.Items
        fields = ['name','description','price','category']