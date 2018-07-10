from django.shortcuts import render
from users.models import UserProfile
from django import forms
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.contrib.auth.models import User
def page(request):
  if request.POST:
    form = Form_admin(request.POST)
    if form.is_valid():

      # In this line, we define the name of the new user.
      form.save()
      # In this line, we register the new user in the database.

      return HttpResponseRedirect(reverse('create_user'))
    else:
      return render(request, 'create_admin.html', {'form' : form})
  else:
    form = Form_admin()
    print 'TEST'
    form = Form_admin()
    return render(request, 'create_admin.html', {'form' : form})
class Form_admin(forms.ModelForm):

  user_auth = forms.CharField(label='User Auth', max_length=30, help_text='Try to make this Unique',widget=forms.HiddenInput())
  username = forms.CharField(label='Username', max_length=30, help_text='Try to make this Unique')

  class Meta:
      # We extend the Meta class of the ModelForm. It is this class that will allow us to define the properties of ModelForm.
      model = UserProfile
      exclude = ('date_created', 'last_connexion',)
