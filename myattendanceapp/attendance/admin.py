
from django.contrib import admin
from .models import Group, Member, Attendance, Session, leaders

admin.site.register(Group)
admin.site.register(Member)
admin.site.register(Attendance)
admin.site.register(Session)
admin.site.register(leaders)