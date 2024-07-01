import openai
from django.conf import settings
from django.shortcuts import render, get_object_or_404, redirect
from .models import Recipe
from .forms import RecipeForm

def index(request):
    recipes = Recipe.objects.all()
    return render(request, 'index.html', {'recipes': recipes})

def recipe_detail(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    return render(request, 'recipe_detail.html', {'recipe': recipe})

def create_recipe(request):
    instructions = None
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            if request.POST.get('action') == 'generate':
                ingredients = form.cleaned_data['ingredients']
                instructions = generate_instructions(ingredients)
                # 存储配方详情到 session 以便保存
                request.session['recipe_details'] = {
                    'name': form.cleaned_data['name'],
                    'ingredients': form.cleaned_data['ingredients'],
                    'instructions': instructions
                }
            elif request.POST.get('action') == 'save':
                # 检索之前在 session 中保存的配方信息
                recipe_details = request.session.get('recipe_details')
                if recipe_details:
                    recipe = Recipe(
                        name=recipe_details['name'],
                        ingredients=recipe_details['ingredients'],
                        instructions=recipe_details['instructions']
                    )
                    recipe.save()
                    return redirect('all_recipes')
        else:
            print("Form is invalid:", form.errors)
        return render(request, 'create_recipe.html', {'form': form, 'instructions': instructions})
    else:
        form = RecipeForm()
    return render(request, 'create_recipe.html', {'form': form})

def all_recipes(request):
    recipes = Recipe.objects.all()
    return render(request, 'all_recipes.html', {'recipes': recipes})

def generate_instructions(ingredients):
    openai.api_key = settings.OPENAI_API_KEY
    prompt = f"Generate a concise recipe based on the following ingredients: {ingredients}"
    
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=500
    )
    
    instructions = response['choices'][0]['message']['content'].strip()
    return instructions
