from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User

from homepage.models import Recipe, Author, FavoriteRecipesModel

from homepage.forms import AddRecipeForm, AddAuthorForm, LoginForm, SignupForm


# Create your views here.


def index(request):
    my_recipes = Recipe.objects.all()
    return render(request, "index.html", {"recipes": my_recipes})


def recipe_detail(request, recipe_id):
    my_recipe = Recipe.objects.filter(id=recipe_id).first()
    selected_author = Author.objects.filter(id=recipe_id).first()
    whose_favoriterecipe = Author.objects.filter(user=request.user).first()
    if FavoriteRecipesModel.objects.filter(chosen_by=whose_favoriterecipe):
        favoriteby_user = True
    else:
        favoriteby_user = False
    return render(request, "recipe_detail.html", {"recipe": my_recipe, "author": selected_author, 'user': favoriteby_user})


def author_detail(request, author_id):
    selected_author = Author.objects.filter(id=author_id).first()
    author_recipes = Recipe.objects.filter(author=selected_author)
    favorites_byselectedauthor = FavoriteRecipesModel.objects.filter(chosen_by=selected_author)
    return render(request, "author_detail.html", {"author": selected_author, "recipes": author_recipes, 'favorites': favorites_byselectedauthor})


@login_required
def add_recipe(request):
    if request.method == "POST":
        form = AddRecipeForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            # breakpoint()
            new_recipe = Recipe.objects.create(
                title=data.get('title'),
                author=request.user.author,
                description=data.get('description'),
                time_required=data.get('time_required'),
                instructions=data.get('instructions')
            )
            return HttpResponseRedirect(reverse("recipeview", args=[new_recipe.id]))

    form = AddRecipeForm()
    return render(request, "generic_form.html", {"form": form})


@login_required
def editrecipe_view(request, recipe_id):
    edit_recipe = Recipe.objects.filter(id=recipe_id).first()
    if request.method == 'POST':
        editrecipe_form = AddRecipeForm(request.POST, instance=edit_recipe)
        editrecipe_form.save()
        return HttpResponseRedirect(reverse('recipe_detail', args=[edit_recipe.id]))
    editrecipe_form = AddRecipeForm(instance=edit_recipe)
    return render(request, 'generic_form.html', {'form': editrecipe_form})


# @ user_passes_test(lambda u: u.is_superuser)
@ login_required
def add_author(request):
    if request.user.is_staff:
        if request.method == "POST":
            form = AddAuthorForm(request.POST)
            if form.is_valid():
                data = form.cleaned_data
                new_user = User.objects.create_user(username=data.get(
                    "username"), password=data.get("password"))
                Author.objects.create(username=data.get(
                    "username"), bio=data.get("bio"), user=new_user)
                login(request, new_user)
                return HttpResponseRedirect(reverse("homepage"))

        form = AddAuthorForm()
        return render(request, "generic_form.html", {"form": form})
    else:
        return render(request, "permission_error.html")


def addfavoriterecipe_view(request, recipe_id):
    selected_favoriterecipe = Recipe.objects.filter(id=recipe_id).first()
    authorwho_favorited = Author.objects.filter(id=recipe_id).first()
    FavoriteRecipesModel.object.create(recipe=selected_favoriterecipe, author=authorwho_favorited)
    return HttpResponseRedirect(reverse('homepage'))


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, username=data.get(
                "username"), password=data.get("password"))
            if user:
                login(request, user)
                return HttpResponseRedirect(request.GET.get('next', reverse("homepage")))

    form = LoginForm()
    return render(request, "generic_form.html", {"form": form})


def signup_view(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_user = User.objects.create_user(username=data.get(
                "username"), password=data.get("password"))
            Author.objects.create(username=data.get(
                "username"), bio=data.get("bio"), user=new_user)
            login(request, new_user)
            return HttpResponseRedirect(reverse("homepage"))

    form = SignupForm()
    return render(request, "generic_form.html", {"form": form})


def permission_error_view(request):
    return HttpResponseRedirect(reverse("permissionerror"))


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("homepage"))
