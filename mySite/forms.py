from django import forms

class HtmlForms(forms.Form):
  fName = forms.CharField(label="First Name",max_length=100)
  lName = forms.CharField(label="Last Name",max_length=100)
  email = forms.EmailField(label="Email",max_length=255)
  address = forms.CharField(label="Address", max_length=50)
  