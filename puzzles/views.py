from django.views.generic import DetailView

from puzzles.models import Puzzle


class PuzzleDetail(DetailView):
    model = Puzzle
    context_object_name = 'puzzle'
    template_name = 'puzzles/puzzle_detail.html'
