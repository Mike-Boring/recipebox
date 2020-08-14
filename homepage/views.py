from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User

from homepage.models import Recipe, Author

from homepage.forms import RecipeForm, AuthorForm, LoginForm, SignupForm


# Create your views here.


def index(request):
    my_recipes = Recipe.objects.all()
    return render(request, "index.html", {"recipes": my_recipes})


def recipe_detail(request, recipe_id):
    my_recipe = Recipe.objects.filter(id=recipe_id).first()
    selected_author = Author.objects.filter(id=recipe_id).first()
    return render(request, "recipe_detail.html", {"recipe": my_recipe, "author": selected_author})


def author_detail(request, author_id):
    selected_author = Author.objects.filter(id=author_id).first()
    author_recipes = Recipe.objects.filter(author=selected_author)
    return render(request, "author_detail.html", {"author": selected_author, "recipes": author_recipes})


@login_required
def recipe_form_view(request):
    if request.method == "POST":
        form = RecipeForm(request.POST)
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

    form = RecipeForm()
    return render(request, "generic_form.html", {"form": form})


# @ user_passes_test(lambda u: u.is_superuser)
@ login_required
def author_form_view(request):
    if request.user.is_staff:
        if request.method == "POST":
            form = AuthorForm(request.POST)
            if form.is_valid():
                data = form.cleaned_data
                new_user = User.objects.create_user(username=data.get(
                    "username"), password=data.get("password"))
                Author.objects.create(username=data.get(
                    "username"), bio=data.get("bio"), user=new_user)
                login(request, new_user)
                return HttpResponseRedirect(reverse("homepage"))

        form = AuthorForm()
        return render(request, "generic_form.html", {"form": form})
    else:
        return render(request, "permission_error.html")


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
