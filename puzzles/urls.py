from django.urls import path

from puzzles.views import PuzzleDetail, PuzzleList

urlpatterns = [
    path('', PuzzleList.as_view(), name='puzzle_list'),
    path('<uuid:pk>/', PuzzleDetail.as_view(), name='puzzle_detail'),
]
