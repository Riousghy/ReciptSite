from django import forms
from .models import Recipe

class RecipeForm(forms.ModelForm):
    ingredients = forms.CharField(
        widget=forms.Textarea(attrs={
            "placeholder": "Enter ingredients here"
        }),
        required=True,
        help_text=""
    )

    class Meta:
        model = Recipe
        fields = ['name', 'ingredients']
