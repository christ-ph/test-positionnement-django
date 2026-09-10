
from django import forms
from .models import User

INPUT_CLASS = 'w-full border border-gray-300 rounded-lg px-3 py-2 focus:outline-none focus:ring-2 focus:ring-blue-500'


class InscriptionForm(forms.Form):
    nom = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': INPUT_CLASS, 'placeholder': 'Nom'}))
    prenom = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': INPUT_CLASS, 'placeholder': 'Prénom'}))
    userid = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': INPUT_CLASS, 'placeholder': 'userid'}))
    mot_de_passe = forms.CharField(widget=forms.PasswordInput(attrs={'class': INPUT_CLASS, 'placeholder': 'Mot de passe'}))
    confirmation = forms.CharField(widget=forms.PasswordInput(attrs={'class': INPUT_CLASS, 'placeholder': 'Confirmer le mot de passe'}))

    def clean_userid(self):
        userid = self.cleaned_data['userid']
        if User.objects.filter(userid=userid).exists():
            raise forms.ValidationError("Un compte existe déjà avec cet userid.")
        return userid

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data.get('mot_de_passe') != cleaned_data.get('confirmation'):
            raise forms.ValidationError("Les mots de passe ne correspondent pas.")
        return cleaned_data


class ConnexionForm(forms.Form):
    userid = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': INPUT_CLASS, 'placeholder': 'userid'}))
    mot_de_passe = forms.CharField(widget=forms.PasswordInput(attrs={'class': INPUT_CLASS, 'placeholder': 'Mot de passe'}))



