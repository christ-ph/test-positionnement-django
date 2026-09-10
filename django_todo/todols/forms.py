from django import forms
from .models import Tache

INPUT_CLASS = 'w-full border border-gray-300 rounded-lg px-3 py-2 focus:outline-none focus:ring-2 focus:ring-blue-500'


class Tachesforms(forms.ModelForm):
    class Meta:
        model = Tache
        fields = ['titre', 'description', 'status', 'priorite', 'date_echeance']
        widgets = {
            'titre': forms.TextInput(attrs={'placeholder': 'Titre', 'class': INPUT_CLASS}),
            'description': forms.Textarea(attrs={'placeholder': 'Description', 'class': INPUT_CLASS, 'rows': 3}),
            'status': forms.Select(attrs={'class': INPUT_CLASS}),
            'priorite': forms.Select(attrs={'class': INPUT_CLASS}),
            'date_echeance': forms.DateInput(attrs={'type': 'date', 'class': INPUT_CLASS}),
        }