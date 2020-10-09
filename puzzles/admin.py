from django.contrib import admin

from puzzles.models import Choice, Puzzle


class ChoiceInline(admin.TabularInline):
    model = Choice


class PuzzleAdmin(admin.ModelAdmin):
    inlines = (ChoiceInline,)
    model = Puzzle
    list_display = ('title', 'is_active', 'author',)
    list_editable = ('is_active',)
    list_filter = ('is_active', 'created_on',)
    search_fields = ('title',)


admin.site.register(Puzzle, PuzzleAdmin)
