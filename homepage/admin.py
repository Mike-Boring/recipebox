from django.contrib import admin

from homepage.models import Author, Recipe, FavoriteRecipesModel

# Register your models here.
admin.site.register(Author)
admin.site.register(Recipe)
admin.site.register(FavoriteRecipesModel)
