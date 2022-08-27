from django.contrib import admin
from django.contrib.auth.models import Group, User

from app.models import Tag, Task


class TagAdmin(admin.ModelAdmin):
    pass


class TaskAdmin(admin.ModelAdmin):
    pass


admin.site.unregister(User)
admin.site.unregister(Group)
admin.site.register(Tag, TagAdmin)
admin.site.register(Task, TaskAdmin)
