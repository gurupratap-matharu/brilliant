from django.views.generic import DetailView, ListView

from courses.models import Course


class CourseList(ListView):
    model = Course
    context_object_name = 'course_list'
    template_name = 'courses/course_list.html'


class CourseDetail(DetailView):
    model = Course
    context_object_name = 'course'
    template_name = 'courses/course_detail.html'
