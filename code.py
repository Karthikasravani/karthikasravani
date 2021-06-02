import json 
def bmi(filename):
    with open('filen.json') as f: 
      data = json.load(f)
    #print(data)
    no_of_over_weight = 0 # considering over weight, severely over weight, obese, severely obese
    remaining = 0
    for i in data:
        height = i['HeightCm']
        weight = i['WeightKg']
        BMI = weight / (height/100)**2
        print("BMI is "+str(BMI),end = " ")
        if BMI <= 18.4:
            remaining = remaining + 1
            print("You are underweight.",end = " ")
            print("Health Risk: MalNutrition")
        elif BMI <= 24.9:
            remaining = remaining + 1
            print("You are healthy.",end = " ")
            print("Health Risk: Low Risk")
        elif BMI <= 29.9:
            no_of_over_weight = no_of_over_weight +1
            print("You are over weight.",end = " ")
            print("Health Risk: Echanced Risk")
        elif BMI <= 34.9:
            no_of_over_weight = no_of_over_weight +1
            print("You are severely over weight.",end = " ")
            print("Health Risk: Medium Risk")
        elif BMI <= 39.9:
            no_of_over_weight = no_of_over_weight +1
            print("You are obese.",end = " ")
            print("Health Risk: High Risk")
        else:
            no_of_over_weight = no_of_over_weight +1
            print("You are severely obese.",end = " ")
            print("Health Risk: Very High Risk")
    if(no_of_over_weight+remaining == len(data)):
        print("Total number of over weight persons:",no_of_over_weight)
    else:
        print("Inconsistency in caluculation")