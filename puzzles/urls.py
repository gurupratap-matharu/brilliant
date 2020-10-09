from django.urls import path

from puzzles.views import PuzzleDetail

urlpatterns = [
    path('<uuid:pk>/', PuzzleDetail.as_view(), name='puzzle_detail'),
]
