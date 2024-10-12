from django import forms
from user_account.models import CustomUser
import re

class Signup(forms.Form):
    
    name=forms.CharField(max_length=200,widget=forms.TextInput(attrs={"name":"name","maxlength":"200","class":"input input-bordered w-full my-2"}))
    email = forms.EmailField(max_length=200, widget=forms.TextInput(attrs={"name":"signinnn","maxlength":"200","class":"input input-bordered w-full my-2"}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"input input-bordered w-full my-2"}))
    re_password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"input input-bordered w-full my-2"}))


    def clean_email(self):
        e = self.cleaned_data.get("email")
        index_user = CustomUser.objects.filter(username = e).first()
        if index_user is None:
            if "@" and "." in e and e is not None:
                pass
            else:
                raise forms.ValidationError("لطفا ایمیل خود را وارد کنید")
        else:
            raise forms.ValidationError("کاربری با این ایمیل در سایت وجود دارد !")
        
        return e
    
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        re_password = cleaned_data.get("re_password")

        if password and re_password:
            if len(password) < 8:
                self.add_error('password', "رمز عبور باید حداقل 8 کاراکتر باشد")
            if password != re_password:
                self.add_error('re_password', "رمز عبور یکسان نیست")

        return cleaned_data