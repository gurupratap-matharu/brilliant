from django.contrib import admin

from puzzles.models import Choice, Puzzle


class ChoiceInline(admin.TabularInline):
    model = Choice


class PuzzleAdmin(admin.ModelAdmin):
    inlines = (ChoiceInline,)
    model = Puzzle
    list_display = ('title', )


admin.site.register(Puzzle, PuzzleAdmin)
