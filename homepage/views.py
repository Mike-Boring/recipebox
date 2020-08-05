from django.shortcuts import render

from homepage.models import Recipe, Author

# Create your views here.

def index(request):
    my_recipes = Recipe.objects.all()
    return render(request, "index.html", {"recipes": my_recipes})

def recipe_detail(request, post_id):
    my_recipe = Recipe.objects.filter(id=post_id).first()
    selected_author = Author.objects.filter(id=post_id).first()
    return render(request, "recipe_detail.html", {"recipe": my_recipe, "author": selected_author})

def author_detail(request, author_id):
    selected_author = Author.objects.filter(id=author_id).first()
    return render(request, "author_detail.html", {"author": selected_author})    