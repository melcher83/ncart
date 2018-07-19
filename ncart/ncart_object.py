from ncart_app.models import Project
from ncart_app.models import Firewall
from ncart_app.models import Port
from ncart_app.models import Picture
from ncart_app.models import Network

def get_all_projects():
    return Project.objects.all()


class ncart_firewall:
    # initialize the object
    def __init__(self,x):
        self.firewall=Firewall.objects.get(id=x)
    def get_ports(self):
        self.list = Port.objects.filter(Firewall=self.Firewall.id).values_list('id', flat=True)
        return self.list


class ncart_project:
    # initialize the object
    def __init__(self,x):
        self.proj=Project.objects.get(id=x)
    def get_firewalls(self):
        self.list = Firewall.objects.filter(Project=self.proj.id).values_list('id', flat=True)
        return self.list
    def get_project(self):
        return self.proj
    def get_projid(self):
        return self.proj.id
