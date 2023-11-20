from django import forms


class SearchForm(forms.Form):
    q = forms.CharField(
        help_text="Click to see help & options",
        required=False,
        widget=forms.TextInput(attrs={
            'autocomplete': 'off'
        })
    )
