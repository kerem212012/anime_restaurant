from django import forms

class ManagerFeedbackForm(forms.Form):
    name = forms.CharField(
        label="Name",
        widget=forms.TextInput(attrs={'class': 'form-control','placeholder' : 'Enter your Name'}),
        error_messages = {
            'required' : "Name can't be empty."
        }
    )
    email = forms.EmailField(
        label="Email",
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': "Enter your Email"}),
        error_messages={
            'required': "Email can't be empty.",
            'invalid': "Введите корректный email адрес."
        }
    )
    message = forms.CharField(
        label="Message",
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter your Message'}),
        error_messages={
            'required': "Message can't be empty."
        }
    )
