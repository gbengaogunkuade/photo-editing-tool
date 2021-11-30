from django import forms
from django.core import validators
from django.utils import timezone
from django.contrib.auth.models import User
from photoeditor.models import PhotoImage
from PIL import Image



class PhotoImageForm(forms.ModelForm):
    photo = forms.ImageField(label='photo', widget=forms.ClearableFileInput(attrs={'placeholder':'photo', 'class':'form-control gbengaForm'}))


    class Meta:
        model = PhotoImage
        fields = [
            'photo',
        ]





class PhotoDataForm(forms.Form):
    brightness = forms.BooleanField(label='brightness', widget=forms.CheckboxInput(attrs={'class':'form-check-input', 'role': 'switch'}), required=False)
    darken = forms.BooleanField(label='darken', widget=forms.CheckboxInput(attrs={'class':'form-check-input', 'role': 'switch'}), required=False)
    contrast = forms.BooleanField(label="contrast", widget=forms.CheckboxInput(attrs={'class':'form-check-input', 'role': 'switch'}), required=False)
    sharpness = forms.BooleanField(label="sharpness", widget=forms.CheckboxInput(attrs={'class':'form-check-input', 'role': 'switch'}), required=False)
    blur = forms.BooleanField(label="blur", widget=forms.CheckboxInput(attrs={'class':'form-check-input', 'role': 'switch'}), required=False)
    flip_left_right = forms.BooleanField(label="flip_left_right", widget=forms.CheckboxInput(attrs={'class':'form-check-input', 'role': 'switch'}), required=False)
    flip_top_bottom = forms.BooleanField(label="flip_top_bottom", widget=forms.CheckboxInput(attrs={'class':'form-check-input', 'role': 'switch'}), required=False)
    smoothness = forms.BooleanField(label="smoothness", widget=forms.CheckboxInput(attrs={'class':'form-check-input', 'role': 'switch'}), required=False)
    more_color = forms.BooleanField(label="more_color", widget=forms.CheckboxInput(attrs={'class':'form-check-input', 'role': 'switch'}), required=False)
    less_color = forms.BooleanField(label="less_color", widget=forms.CheckboxInput(attrs={'class':'form-check-input', 'role': 'switch'}), required=False)


    class Meta:
        fields = [
            'brightness',
            'darken',
            'contrast',
            'sharpness',
            'blur',
            'flip_left_right',
            'flip_top_bottom',
            'smoothness',
            'more_color',
            'less_color',
        ]

