from django.shortcuts import render
from TasksManager.models import Project
from django import forms
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
def page(request):
  if request.POST:
    print "form"
    form = Form_project(request.POST)
    if form.is_valid():
      print "saving"
      form.save()
      print "saved"
      # If the form is valid, we store the data in a model record in the form.
      return HttpResponseRedirect(reverse('index'))
      # This line is used to redirect to the specified URL. We use the reverse() function to get the URL from its name defines urls.py.
    else:
      print "wtf"
      return render(request, 'add_project.html', {'form': form})
  else:
    print "fail"
    form = Form_project()
    return render(request, 'add_project.html', {'form': form})
class Form_project(forms.ModelForm):


# Here we create a class that inherits from ModelForm.


  class Meta:
  # We extend the Meta class of the ModelForm. It is this class that will allow us to define the properties of ModelForm.
    model = Project
    # We define the model that should be based on the form.
    exclude = ('date_created', 'last_connexion', )