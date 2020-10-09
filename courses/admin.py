from django.contrib import admin

from courses.models import Course


class CourseAdmin(admin.ModelAdmin):
    list_display = ('title',)


admin.site.register(Course, CourseAdmin)
