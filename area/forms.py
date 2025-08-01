from django import forms


class CheckoutForm(forms.Form):
    address = forms.CharField(
        label="Address",
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter your Address'}),
        error_messages={
            'required': "Address can't be empty."
        }
    )
    order_note = forms.CharField(
        label="Order Note",
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter your Message'}),
        required=False
    )
