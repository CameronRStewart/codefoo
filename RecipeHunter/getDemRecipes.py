import requests
import hashlib


class RecipeFilter:

    def __init__(self):
        self.cache = {}

    def fetch_filtered_recipes(self, foodtype, allergens):
        cache_result = self.check_cache(foodtype, allergens)
        if cache_result:
            return cache_result
        else:
            queryurl = "http://www.recipepuppy.com/api/?q=" + foodtype
            r = requests.get(url=queryurl).json()
            res = r['results']
            results = [i for i in res if not self.includes_allergen(i["ingredients"], allergens)]
            self.push_cache(foodtype, allergens, results)
            print(results)

    def includes_allergen(self, ingredients, allergens):
        # Assume ingredients is a comma separated string of ingredient names
        # Assume allergens is list of allergen names
        for a in allergens:
            if ingredients.find(a) > -1:
                return True
            else:
                continue
        return False

    def check_cache(self, foodtype, allergens):
        # concat hash of first arg with the hash of the implode of the second args
        # check if that key exists
        if self.hashargs(foodtype, allergens) in self.cache:
            print("HIT")
            return self.cache[self.hashargs(foodtype, allergens)]
        else:
            return False

    def push_cache(self, foodtype, allergens,  results):
        # key = concat hash of first arg with the hash of the implode of the second args
        # value = result
        hash = self.hashargs(foodtype, allergens)
        if not self.check_cache(foodtype, allergens):
            self.cache[hash] = results
        else:
            return

    def hashargs(self, foodtype, allergens):
        m = hashlib.sha256()
        m.update(foodtype.encode('utf-8') + "".join(allergens).encode('utf-8'))
        return m.hexdigest()

#fetch_filtered_recipes('taco', ["cayenne", "chili"])
