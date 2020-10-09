from django.urls import path

from courses.views import CourseDetail, CourseList

urlpatterns = [
    path('', CourseList.as_view(), name='course_list'),
    path('<uuid:pk>/', CourseDetail.as_view(), name='course_detail'),
]
