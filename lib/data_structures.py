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

def get_names(spicy_foods):


    list_of_title = [a_dict["name"] for a_dict in spicy_foods]
 
    return list_of_title 


def get_spiciest_foods(spicy_foods):
   
    list_of_spiciest_food = [a_dict for a_dict in spicy_foods if a_dict["heat_level"]>5]
 
    return list_of_spiciest_food 

    

def print_spicy_foods(spicy_foods):

    for a_dict in spicy_foods:  
        chilli = "🌶"*a_dict['heat_level']
        print(a_dict['name']+" ("+a_dict['cuisine']+") | Heat Level: "+chilli)

    pass

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    list_of_spiciest_food = {}
     
    for a_dict in spicy_foods:
        if a_dict["cuisine"]==cuisine:
            return a_dict
    pass


def print_spiciest_foods(spicy_foods):
    
    list_of_spiciest_food = [a_dict for a_dict in spicy_foods if a_dict["heat_level"]>5]
 
    for a_dict in list_of_spiciest_food:  
        chilli = "🌶"*a_dict['heat_level']
        print(a_dict['name']+" ("+a_dict['cuisine']+") | Heat Level: "+chilli)
    # return list_of_spiciest_food 
    pass

def get_average_heat_level(spicy_foods):

    sum=0
    for a_dict in spicy_foods:  
        sum += a_dict['heat_level']
    
    return sum/len(spicy_foods)
    pass

def create_spicy_food(spicy_foods, spicy_food): 
    
    spicy_foods.append(spicy_food) 
    return spicy_foods


