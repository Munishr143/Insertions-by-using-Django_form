from django import forms

class Topic_Form(forms.Form):

    S_No=forms.IntegerField()
    Topic_Name=forms.CharField(max_length=30)


