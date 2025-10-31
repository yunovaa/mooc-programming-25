# Write your solution here
def readrecipes(filename):
    with open(filename) as f:
        recipe = []
        recipes = {}
        lines = [line for line in f.readlines()]
        lines.append('\n')
        for line in lines:
            if line.strip():
                recipe.append(line.strip())
            else:
                recipes[recipe[0]] = recipe[1:]
                recipe = []
        return recipes

# print(readrecipes('recipes1.txt'))

def search_by_name(filename: str, word: str):
    names = readrecipes(filename).keys()
    return [name for name in names if word.lower() in name.lower()]

# found_recipes = search_by_name("recipes1.txt", "cake")
# print(found_recipes)

def search_by_time(filename: str, prep_time: int):
    ings = readrecipes(filename)
    return [f'{name}, preparation time {time[0]} min' for name, time in ings.items() if prep_time >= int(time[0])]

# found_recipes = search_by_time("recipes1.txt", 15)
# print(found_recipes)

def search_by_ingredient(filename: str, ingredient: str):
    ings = readrecipes(filename)
    return [f'{name}, preparation time {time[0]} min' for name, time in ings.items() if ingredient in time]

# found_recipes = search_by_ingredient("recipes1.txt", "eggs")
# print(found_recipes)