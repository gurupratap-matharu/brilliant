from django.urls import path

from courses.views import CourseList

urlpatterns = [
    path('', CourseList.as_view(), name='course_list'),
]
