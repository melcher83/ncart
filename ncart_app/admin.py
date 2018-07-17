from __future__ import unicode_literals

from django.contrib import admin
from models import Project
from models import Port
from models import Firewall
from models import Picture
from models import Network_map
from users.models import UserProfile


admin.site.register(Project)
admin.site.register(Port)
admin.site.register(Firewall)
admin.site.register(UserProfile)
admin.site.register(Picture)
admin.site.register(Network_map)


