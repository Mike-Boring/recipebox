from django import forms
from homepage.models import Recipe, Author


class RecipeForm(forms.Form):
    title = forms.CharField(max_length=50)
    author = forms.ModelChoiceField(queryset=Author.objects.all())
    description = forms.CharField(widget=forms.Textarea)
    time_required = forms.CharField(max_length=50)
    instructions = forms.CharField(widget=forms.Textarea)


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ["name", "bio"]


class LoginForm(forms.Form):
    username = forms.CharField(max_length=240)
    password = forms.CharField(widget=forms.PasswordInput)


# from django import forms
# from homepage.models import Recipe, Author


# class RecipeForm(forms.Form):
#     title = forms.CharField(max_length=50)
#     description = forms.CharField(widget=forms.Textarea)
#     time_required = forms.CharField(max_length=50)
#     instructions = forms.CharField(widget=forms.Textarea)


# class AuthorForm(forms.ModelForm):
#     class Meta:
#         model = Author
#         fields = ["name", "bio"]


# class SignupForm(forms.Form):
#     username = forms.CharField(max_length=240)
#     password = forms.CharField(widget=forms.PasswordInput)
#     bio = forms.CharField(widget=forms.Textarea)
