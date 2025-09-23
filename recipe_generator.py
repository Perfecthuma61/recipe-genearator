import pandas as pd

# Load dataset path
df = pd.read_csv("recipess.csv")

# Keep only useful columns and print randoms
df = df[['recipe_name', 'ingredients', 'directions', 'rating', 'cuisine_path']]
print(df.head())

# Convert ingredients into clean lists
df['ingredients_list'] = df['ingredients'].str.lower() \
                                         .str.replace('[^a-zA-Z, ]','', regex=True) \
                                         .str.split(", ")

# Show example
print(df[['recipe_name', 'ingredients_list']].head())
 
#creating function for word matching
def find_recipes(user_ingredients, top_n=5):
    user_ingredients = [i.lower().strip() for i in user_ingredients]

    scores = []
    for idx, row in df.iterrows():
        recipe_ingredients = row['ingredients_list']
        if isinstance(recipe_ingredients, list):
            # Check partial matches
            match_count = sum(
                1 for i in user_ingredients 
                for ing in recipe_ingredients 
                if i in ing  # <-- partial match
            )
            if match_count > 0:
                scores.append((
                    match_count,
                    row['recipe_name'],
                    recipe_ingredients,
                    row['rating'],
                    row['cuisine_path'],
                    row['directions']
                ))

    # Sort by best matches
    scores = sorted(scores, key=lambda x: x[0], reverse=True)
    return scores[:top_n]	
# Ask for ingredients
user_input = input("Which ingredients do you have? (comma separated): ")
user_ingredients = user_input.split(",")

# Find recipes
recipes = find_recipes(user_ingredients, top_n=5)

# Print results
print("\n🍲 Suggested Recipes:")
for match_count, name, ingredients, rating, cuisine, directions in recipes:
    print(f"- {name} ({cuisine}, ⭐ {rating}) | matches {match_count} ingredients")
    print(f"  Ingredients: {', '.join(ingredients[:10])}...\n")
    print(f"  Directions: {directions[:200]}...\n")  # show first 200 chars
    print("------------------------------------------------------------")





