from ncart_app.models import Project
from django.shortcuts import render
def page(request):
  all_projects = Project.objects.all()
  return render(request, 'index.html', {'action': "Display all projects", 'all_projects': all_projects})