import requests

def recipe_search(ingredient):
    app_id = '35b30cea'
    app_key = '2422db83b20100056b7fcc54c5915c02'
    result = requests.get(f'https://api.edamam.com/search?q={ingredient}&app_id={app_id}&app_key={app_key}')
    data = result.json()
    return data['hits']

def search():
    user_ingredient = input('Enter an ingredient for your recipe: ')
    results = recipe_search(user_ingredient)

    if not results:
        print(f"Sorry, there's no recipies with {user_ingredient}.")
        try_again = input("Do you want to try any other? [Y/N]")
        answer = try_again.lower()
        if answer == "y":
            choose_ingredient = input('Enter an ingredient for your recipe: ')
            results = recipe_search(choose_ingredient)
            print_results(results)
        elif answer == 'n':
            print("Thank you, see you next time!")
        else:
            print('Please, try again!')
    else:
        print_results(results)

def print_results(results):
    for result in results:
        recipe = result['recipe']
        print(recipe['label'])
        print(recipe['url'])

search()