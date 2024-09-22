spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

# 1. get_names() - Returns the names of the spicy foods
def get_names(spicy_foods):
    return [food['name'] for food in spicy_foods]

# 2. get_spiciest_foods() - Returns foods where heat level > 5
def get_spiciest_foods(spicy_foods):
    return [food for food in spicy_foods if food['heat_level'] > 5]

# 3. print_spicy_foods() - Prints each spicy food in formatted style
def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {'🌶' * food['heat_level']}")

# 4. get_spicy_food_by_cuisine() - Returns the food matching the given cuisine
def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food['cuisine'] == cuisine:
            return food
    return None

# 5. print_spiciest_foods() - Prints only the foods with heat level > 5
def print_spiciest_foods(spicy_foods):
    spiciest_foods = get_spiciest_foods(spicy_foods)  # Reuse get_spiciest_foods
    print_spicy_foods(spiciest_foods)

# 6. get_average_heat_level() - Returns the average heat level
def get_average_heat_level(spicy_foods):
    total_heat = sum([food['heat_level'] for food in spicy_foods])
    return total_heat // len(spicy_foods)

# 7. create_spicy_food() - Adds a new spicy food to the list and returns the updated list
def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
