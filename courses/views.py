from django.views.generic import TemplateView


class CourseList(TemplateView):
    template_name = 'courses/course_list.html'
