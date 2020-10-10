from django.test import TestCase
from django.urls import resolve, reverse
from puzzles.tests.factories import PuzzleFactory
from puzzles.views import PuzzleDetail, PuzzleList
from users.tests.factories import UserFactory


class PuzzleListTests(TestCase):
    def setUp(self):
        self.user = UserFactory()
        self.puzzle = PuzzleFactory(author=self.user)

    def test_puzzle_list_resolves_puzzlelistview(self):
        view = resolve(reverse('puzzle_list'))
        self.assertEqual(view.func.__name__, PuzzleList.as_view().__name__)

    def test_puzzle_list_works_for_anonymous_user(self):
        response = self.client.get(reverse('puzzle_list'))
        no_response = self.client.get('/puzzle_list/')

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'puzzles/puzzle_list.html')
        self.assertContains(response, 'Puzzle')
        self.assertContains(response, self.puzzle.title)
        self.assertNotContains(response, 'Hi I should not be on this page')
        self.assertEqual(no_response.status_code, 404)


class PuzzleDetailTests(TestCase):
    def setUp(self):
        self.user = UserFactory()
        self.puzzle = PuzzleFactory(author=self.user)

    def test_puzzle_detail_resolves_puzzledetailview(self):
        view = resolve(self.puzzle.get_absolute_url())
        self.assertEqual(view.func.__name__, PuzzleDetail.as_view().__name__)

    def test_puzzle_detail_works_for_anonymous_user(self):
        response = self.client.get(self.puzzle.get_absolute_url())
        no_response = self.client.get('/puzzle/1234/')

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'puzzles/puzzle_detail.html')
        self.assertContains(response, 'Puzzle')
        self.assertContains(response, self.puzzle.title)
        self.assertNotContains(response, 'Hi I should not be on this page')
        self.assertEqual(no_response.status_code, 404)
