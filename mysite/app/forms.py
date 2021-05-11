from django import forms


class Contacts(forms.Form) :
    emails = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea(attrs={'width':"100%", 'cols' : "80", 'rows': "20", }))

    def clean(self):
        cleaned_data = super(Contacts, self).clean()
        emails = cleaned_data.get('emails')
        message = cleaned_data.get('messages')
        if not emails and not message:
            raise forms.ValidationError('You have to write something!')