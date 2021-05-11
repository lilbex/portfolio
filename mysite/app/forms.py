from django import forms


class Contacts(forms.Form) :
    emails = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea(attrs={'width':"100%", 'cols' : "80", 'rows': "20", }))
