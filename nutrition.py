#Nutrition tracker
#Bhumika
import random


#Calculate BMI


def calc_bmi(weight, height):
    
    '''(float, float)->float
    returns the value of BMI by taking height and weight as input.

    >>> calc_bmi(45, 1.5)
    Your BMI is 20.0
    You have a normal BMI!
    20.0

    >>>calc_bmi(45, 1.65)
    Your BMI is 16.0
    You are currently underweight.
    Do you want a tip on how to improve your health?
    Please answer in yes or no: yes
    Choose nutrient-rich foods.
    If you want to read more on this, here's a link!
    https://www.mayoclinic.org/healthy-lifestyle/nutrition-and-healthy-eating/expert-answers/underweight/faq-20058429
    16.0

    >>>calc_bmi(75, 1.65)
    Your BMI is 27.0
    You are currently overweight.
    Do you want a tip on how to improve your health?
    Please answer in yes or no: yes
    Eating 5 Smaller Meals Might Work Better Than Eating 3 Larger Ones
    If you want to read more on this, here's a link!
    http://stopcancerfund.org/pz-diet-habits-behaviors/eating-habits-that-improve-health-and-lower-body-mass-index/
    27.0

    >>>calc_bmi(70, 1.60)
    Your BMI is 27.0
    You are currently overweight.
    Do you want a tip on how to improve your health?
    Please answer in yes or no: no

    27.0

    >>>calc_bmi(45, 1.60)
    Your BMI is 17.0
    You are currently underweight.
    Do you want a tip on how to improve your health?
    Please answer in yes or no: no

    17.0
    '''

#calculates the BMI from the weight and height and prints it
    bmi = weight//(height)**2
    print("Your BMI is " + str(bmi))

#provides the user feedback on their body composition, underweight if less than 18.5
    if bmi < 18.5:
        user_response=input("You are currently underweight.\nDo you want a tip on how to improve your health?\nPlease answer in yes or no: ")
        
        if user_response== "yes":

#gives the user one random health tip from the list of the tips.
            
            tips_bmi = ["Eat more frequently. Eat five to six smaller meals during the day rather than two or three large meals.", "Choose nutrient-rich foods.", "Try smoothies and shakes. Don't fill up on diet soda, coffee and other drinks with few calories and little nutritional value.", "Eat More Fruits, Vegetables, Whole Grains, and Low- or No-Fat Dairy Products Every Day","Add extras to your dishes for more calories — such as cheese", "Don’t Waste Your Time, Energy, and Money on “Quick Fix” Solutions"]
            
            print(random.choice(tips_bmi))

#prints a link to a health blog according to the user's needs.
            
            print("If you want to read more on this, here's a link!\nhttps://www.mayoclinic.org/healthy-lifestyle/nutrition-and-healthy-eating/expert-answers/underweight/faq-20058429")
    
        elif user_response=="no":
            
#prints an empty string if the user doesn't want a health tip.            
            print("")
            

#provides the user feedback on their body composition, overweight if more than 25.0
    elif bmi>25.0:
        
        user_response=input("You are currently overweight.\nDo you want a tip on how to improve your health?\nPlease answer in yes or no: ")
       
        if user_response== "yes":

#gives the user one random health tip from the list of the tips.
            tips_bmi = ["The Only Way to Lose Weight is to Eat Fewer Calories Than You Burn in a Day", "Eating 5 Smaller Meals Might Work Better Than Eating 3 Larger Ones", "Eat Less Cholesterol and Less Fat – Especially Less Saturated Fat, and Almost No Trans-Fat", "Eat More Fruits, Vegetables, Whole Grains, and Low- or No-Fat Dairy Products Every Day","Staying Healthy is a Life-Long Proposition", "Don’t Waste Your Time, Energy, and Money on “Quick Fix” Solutions"]
            print(random.choice(tips_bmi))
            
#prints a link to a health blog according to the user's needs.

            print("If you want to read more on this, here's a link!\nhttp://stopcancerfund.org/pz-diet-habits-behaviors/eating-habits-that-improve-health-and-lower-body-mass-index/")
    
#prints an empty string if the user doesn't want a health tip.            
        
        elif user_response=="no":
            
            print ("")

#if thus user has a normal BMI, between 18.5 and 25.0
            
    else:
        print("You have a normal BMI!")
        
    return bmi
        
#calculate total calories on the basis of what they ate

def diet_plan(bmi):

    '''(float) -> float
    returns the total calorie count for the day according to user's choice of breakfast, lunch dinner and snacks.

    >>> diet_plan(16.0)
    Please choose what you want to eat from the list below

    ['Tomato Toast :  277', 'Egg and Veggie Sandwich : 371', 'Apple Vanilla Pancakes : 296', 'Ham and egg Burrito : 400', 'PB and J waffle : 385']
    Tomato Toast :  277
    Your total calorie count for today is 277.0 calories.
    '''

#lists of high calorie food options

    high_cal_brkfast = ["Tomato Toast :  277", "Egg and Veggie Sandwich : 371", "Apple Vanilla Pancakes : 296", "Ham and egg Burrito : 400","PB and J waffle : 385"]
    
    high_cal_lunch = []
    
    high_cal_snacks =[]
    
    high_cal_dinner = []
    
#lists of low calorie food options
    
    low_cal_brkfast = ["Salmon Cucumber Wraps : 169", "Steel Cut Oatmeal : 115", "spinach omellete : 150", "Cinnamon Toast : 092"]
    
    low_cal_lunch = []
    
    low_cal_snacks =[]
    
    low_cal_dinner = []

#creating the variable for user's choice of food and calorie count
    
    food_choice = ""
    calories_num = 0.0
    

    #cal_count = 0.0
    
#returning the cal count of a food choice
    
    def plan(meal):
        '''(list) -> float
        takes in the list of food options and returns th calorie count
        '''
        print("Please choose what you want to eat from the list below\n")
            
    #printing the list of breakfast options
            
        print(meal)

    #letting the user pick one option from  breakfasts
            
        food_choice = input()
            
    #Adding the calories to the final calorie counts variable.
            
            
        cal_count = float(food_choice[len(food_choice)-3: len(food_choice)])
            
        return cal_count
    
    def final_plan(breakfast, lunch, dinner, snack):
        
        '''(list,list,list,list)->float

        returns the total number of calories by taking suitable lists for breakfast, lunch, dinner
        and snack as input according to the user's BMI.
        
        '''
        
        brkfast_cal = plan(breakfast)
        lunch_cal = plan(lunch)
        dinner_cal = plan(dinner)
        snack_cal = plan(snack)
        
        total_cal = brkfast_cal + lunch_cal + dinner_cal + snack_cal
        
        return total_cal

#Printing out the calories for the entire day depending on bmi
    
    if bmi<18.5:
        
        calories_num = final_plan(high_cal_brkfast, high_cal_lunch, high_cal_dinner, high_cal_snacks)
        
    
    elif bmi>25.0:
        
        calories_num = final_plan(low_cal_brkfast, low_cal_lunch, low_cal_dinner, low_cal_snacks)
        
    else:
        
#pose question to choose between high calorie and low calorie if the user's bmi is normal
        
        print("Do you wanna eat a high calorie diet or low calorie diet for today?")
        
        user_choice = input()
        
        if user_choice== "high calorie diet":
            
            calories_num = final_plan(high_cal_brkfast, high_cal_lunch, high_cal_dinner, high_cal_snacks)
            
    
        if user_choice== "low calorie diet":
            
            calories_num = final_plan(low_cal_brkfast, low_cal_lunch, low_cal_dinner, low_cal_snacks)
        
#printing the final total number of calories for the day
            
    print("Your total calorie count for today is " + str(calories_num) + " calories")


def cal_burn(cal_goal, exercise):
    
    '''(int, string)->float
    returns the time in the units of minutes the user will have to exercise for
    taking exercise and calorie goal as input
    >>> cal_burn(100, "cardio")
    18.0
    >>> cal_burn(200, "cycling")
    20.0
    >>> cal_burn(150, "running")
    15.0
    >>> cal_burn(300, "walking")
    60.0
    >>> cal_burn(0, "walking")
    0.0
    >>> cal_burn(200, "")
    0.0
    '''
    time = 0.0
#calculating the time the user will have to workout according to their exercise
    
    if exercise == "cycling" :
        
        time = (cal_goal*5)/(50)
        
    elif exercise == "cardio" :
        
        time = (cal_goal*10)/(50)
        
    elif exercise == "running" :
        
        time = (cal_goal*5)/(50)
        
    elif exercise == "walking" :
        
        time = (cal_goal*10)/(50)
        
    return time


def nutrition_tracker():
    
#calling all the functions.

#taking the weight and height of the user as input to call the calc_bmi function
    
    weight = float(input("Please enter your weight in kilograms: "))
    
    height = float(input("Please enter your height in metres: "))
    
#calling the bmi function and storing the bmi in a variable
    
    bmi = calc_bmi(weight, height)

#calling the diet_plan function to prepare a diet plan and return calories
    
    diet_plan(bmi)

#taking the calorie burning goal and the exercise they want to do from the user.
    
    cal_goal = int(input("What is your calorie burning goal for today? Please answer in the multiple of 50's: "))
    
    print("Are you gonna achieve your goal by cardio, cycling, running or walking?\n")
    
    exercise = input()
    
#returning the time they will have to do the exercise.
    
    time_exercise = cal_burn(cal_goal, exercise)
    
    print("You will have to do " + exercise + " for " + str(time_exercise) + " minutes to burn " + str(cal_goal) + " calories ")
    
    

