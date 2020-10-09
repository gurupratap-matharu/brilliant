from django.views.generic import DetailView, ListView

from puzzles.models import Puzzle


class PuzzleList(ListView):
    model = Puzzle
    context_object_name = 'puzzle_list'
    template_name = 'puzzles/puzzle_list.html'


class PuzzleDetail(DetailView):
    model = Puzzle
    context_object_name = 'puzzle'
    template_name = 'puzzles/puzzle_detail.html'
