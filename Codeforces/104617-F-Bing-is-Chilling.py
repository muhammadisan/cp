from collections import defaultdict

def min_ingredient_cost(ingredient, ingredient_cost, ingredient_recipe):
  if len(ingredient_recipe[ingredient]) == 0:
    return ingredient_cost[ingredient]
  
  recipe_cost = 0
  for recipe in ingredient_recipe[ingredient]:
    recipe_cost += min_ingredient_cost(recipe, ingredient_cost, ingredient_recipe)
  
  return min(ingredient_cost[ingredient], recipe_cost)
  
n, m = map(int, input().split())
ingredients = input().split()
ingredient_cost = defaultdict(int)
ingredient_recipe = defaultdict(list)
while m > 0:
  s = input().split()
  ingredient_cost[s[0]] = int(s[1])
  for c in s[3:]:
    ingredient_recipe[s[0]].append(c)
  m -= 1

ans = 0
for ingredient in ingredients:
  ans += min_ingredient_cost(ingredient, ingredient_cost, ingredient_recipe)
print(ans)
