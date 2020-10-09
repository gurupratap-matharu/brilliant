import factory
from puzzles.models import Choice, Puzzle
from users.tests.factories import UserFactory


class PuzzleFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Puzzle

    title = factory.Faker('word')
    description = factory.Faker('text')
    author = factory.SubFactory(UserFactory)


class ChoiceFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Choice

    text = factory.Faker('word')
    is_correct = factory.Faker('boolean')
    puzzle = factory.SubFactory(PuzzleFactory)
