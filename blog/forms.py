from django import forms

class PostForm(forms.Form):
    # TODO: Define form fields here
    title = forms.CharField(max_length=30)  
    description = forms.CharField(max_length=200, widget=forms.Textarea)
    active = forms.BooleanField()
    
    