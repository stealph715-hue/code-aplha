from django.contrib import admin
from .models import Project, Membership, Task, TaskComment, Notification


class MembershipInline(admin.TabularInline):
    model = Membership
    extra = 0


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'owner', 'created_at']
    inlines = [MembershipInline]


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['title', 'project', 'status', 'assigned_to', 'due_date']
    list_filter = ['status', 'project']


admin.site.register(TaskComment)
admin.site.register(Notification)
