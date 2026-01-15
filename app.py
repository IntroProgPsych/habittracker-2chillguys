#import all the modules you need, below this line


#write any functions you need, below this line


#use the main() function for your program, define all other functions above main
def main ():
    #use print statements such as this one, to mark important points in the application, to help you with debugging
    print("Starting application...")

#please do not change the lines below, they are needed for your tests to work properly
#write all your code in the current file, and all your tests in the tests.py file
if __name__ == "__main__":
    main()

items = [
    {"text": "How many days per week do you go to bed at a consistent hour?", "habit": "SleepRoutine"}, 
    {"text": "How many days per week do you eat at least one healthy meal?", "habit": "HealthyEating"},
    {"text": "How many days per week do you practice mindfulness or relaxation?", "habit": "Mindfulness"},
    {"text": "How many days per week do you spend meaningful time with others?", "habit": "SocialConnection"},
    {"text": "How many days per week do you exercise for at least 20 minutes?", "habit": "PhysicalActivity"}, 
    {"text": "How many days per week do you reach 10k steps?", "habit": "PhysicalActivity"}, 
    {"text": "How many days per week do you participate in group activities?", "habit": "SocialConnection"},
    {"text": "How many days per week do you practice journaling?", "habit": "Mindfulness"},
    {"text": "How many days per week do you practice yoga?", "habit": "Mindfulness"}, 
    {"text": "How many days per week do you reach your protein goal?", "habit": "HealthyEating"},
    {"text": "How many days per week do you eat the recommended 3 meals a day?", "habit": "HealthyEating"}, 
    {"text": "How many days per week do you lift weights?", "habit": "PhysicalActivity"},
    {"text": "How many days per week do you wake up rested?", "habit": "SleepRoutine"},
    {"text": "How many days per week do you get at least 8 hours of sleep?", "habit": "SleepRoutine"} 
]

def get_valid_input(question):
    while True:
        try:
            answer = int(input(question + " (0-7): "))
            if answer >=0 and answer <= 7: 
                return answer
            else:
                print("Error. Enter a number between 0 and 7.") 
        except ValueError:
            print("Please enter a number.") 

def interpret_score(score):
    if score >= 5:
        return "High adherence"
    elif score >= 3:
        return "Moderate adherence"
    else:
        return "Low adherence"
    

scores = {"PhysicalActivity": 0, "HealthyEating": 0, "SleepRoutine": 0, "Mindfulness": 0, "SocialConnection": 0}

for item in items: 
    answer = get_valid_input(item["text"])
    scores[item["habit"]] += answer 


print("\nHabit Adherence Scores:")  
for category, score in scores.items():
        interpretation = interpret_score(score)
        print(f"{category}: {score} - {interpretation}")



