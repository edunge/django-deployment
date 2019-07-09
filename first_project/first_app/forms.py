from django import forms
from django.core import validators



class FormName(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    verifyemail = forms.EmailField(label='Verify Email')
    text = forms.CharField(widget=forms.Textarea)
    botcatcher = forms.CharField(required=False,
                                widget=forms.HiddenInput, validators=[validators.MaxLengthValidator(0)])


def clean(self):
    all_clean_data = super().clean
    email = all_clean_data['email']
    vemail = all_clean_data['verifyemail']

    if email != vemail:
        raise forms.ValidationError('Email mismatch!')


# def clean_botcatcher(self):
#     botcatcher = self.cleaned_data['botcatcher']
#     if len(botcatcher) > 0:
#         raise forms.ValidationError("GOTTA BOT!")
#     return botcatcher
