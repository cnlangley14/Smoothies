from app import app
from flask import render_template

mysmoothies = []

class Smoothie:
    name = ""
    ingredients = []
    steps = []


    def __init__ (self, name):
        self.name = name
        print("making a new smoothie")
        self.ingredients = []
        self.steps = []

        
    def add_ingredient(self, ing):
        """add ingredients to the smoothie"""
        self.ingredients.append(ing)

    def add_steps(self, step):
        """adds directions to the steps"""
        self.steps.append(step)
    
    def print_ingredients(self):
        print(f"{self.name}'s ingredients")
        print ("=========================")
        for ing in self.ingredients:
            print(ing)
        
    def print_steps(self):
        print(f"{self.name}'s steps")
        print ("=========================")
        counter = 1
        for step in self.steps:
            print(f"{counter}. {step}")
            counter += 1

            
@app.route('/smoothies')
def smoothies ():
    return render_template("smoothies.html", smoothies=mysmoothies)


