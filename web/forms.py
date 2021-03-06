#!/usr/bin/env python
from django import forms
from wehaveweneed.web.models import *
#from django.contrib.admin import widgets
from django.contrib.auth.models import User
from django.forms.util import ErrorList
from django.contrib.localflavor.us.forms import *

class PostForm(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = ('title', 'type', 'priority', 
                  'location', 'geostamp',
                  'time_start',
                  'time_end',
                  'category',
                  'content',)
        
class userprofileForm(forms.Form):
    username = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'size':'25'}),error_messages={'required': 'Please enter a username'})
    first_name = forms.CharField(initial='',label='First Name',max_length=50,widget=forms.TextInput(attrs={'size':'25'}),error_messages={'required': 'Please enter your First Name'})
    last_name = forms.CharField(initial='',label='Last Name',max_length=50,widget=forms.TextInput(attrs={'size':'25'}),error_messages={'required': 'Please enter your Last Name'})
    password1 = forms.CharField(label='Password',max_length=50,widget=forms.PasswordInput(attrs={'size':'25'}),error_messages={'required': 'Please enter your password'})
    password2 = forms.CharField(label='Password (Re-type)',max_length=50,widget=forms.PasswordInput(attrs={'size':'25'}),error_messages={'required': 'Please enter your password'})
    email =     forms.EmailField(initial='',max_length=50,widget=forms.TextInput(attrs={'size':'25'}),error_messages={'required': 'Please enter a valid email address'})
    phone_number = USPhoneNumberField(initial='',label='Phone Number (main)', widget=forms.TextInput(attrs={'size':'25'}),error_messages={'required': 'Please enter your Phone Number'}),
    
    
    def clean_username(self):
        data = self.cleaned_data['username']
        
        #check inputed data for current record in DB
        exist_check=User.objects.filter(username = data).count()

        if exist_check>0:
            raise forms.ValidationError("Username already exists. Please enter another username")

        # Always return the cleaned data, whether you have changed it or
        # not.
        return data
    
    def clean(self):
        cleaned_data = self.cleaned_data
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")
        
        if not password1:
            msg = u"You must enter a password"
            self._errors["password1"] = ErrorList([msg])
            self._errors["password2"] = ErrorList([msg])
            return cleaned_data
        
        if len(password1) < 7:
            msg = u"Your passwords must be at least 8 characters long"
            self._errors["password1"] = ErrorList([msg])
            self._errors["password2"] = ErrorList([msg])
            return cleaned_data
        
        #define error if user type is agent and entity not set
        if (password1 != password2):
            msg = u"Your passwords do not match. Please re-type your passwords"
            self._errors["password1"] = ErrorList([msg])
            self._errors["password2"] = ErrorList([msg])
            
        
        pin = cleaned_data.get("videntity_pin")
        phone_number = cleaned_data.get("phone_number")
        
        user=User.objects.filter(userprofile__phone_number=phone_number)
        
        if user.count() > 0:
            msg = u"Your phone_number is already registered."
            self._errors["phone_number"] = ErrorList([msg])
            
        # Always return the full collection of cleaned data.
        return cleaned_data