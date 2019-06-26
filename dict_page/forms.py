from django import forms
from django.core.exceptions import ValidationError
from .models import Dictionary

class AddForm(forms.ModelForm):
    class Meta:
        model = Dictionary
        fields = ["word","definition"]

class InputForm(forms.ModelForm):
    class Meta:
        model = Dictionary
        fields = ["word",]

    def validate_word(self):
        word = self.cleaned_data['word']
        if len(word) > 50:
            raise ValidationError("The length of the word is more than 50 characters!")
            # word = word[:50]
        return word

