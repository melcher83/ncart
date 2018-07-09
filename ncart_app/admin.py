from __future__ import unicode_literals

from django.contrib import admin
from models import Project
from models import Port
from models import Firewall
from users.models import User


admin.site.register(Project)
admin.site.register(Port)
admin.site.register(Firewall)
admin.site.register(User)


