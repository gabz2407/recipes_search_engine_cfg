import requests

def recipe_search(ingredient):
    app_id = '35b30cea'
    app_key = '2422db83b20100056b7fcc54c5915c02'
    result = requests.get(f'https://api.edamam.com/search?q={ingredient}&app_id={app_id}&app_key={app_key}')
    data = result.json()
    return data['hits']

def search():
    choose_ingredient = input('Enter an ingredient: ')
    results = recipe_search(choose_ingredient)
    recipe_search(results)

search()