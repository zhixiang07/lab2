def calc_bmi(Height, Weight):
    print("height= " + str(Height))
    print("weight = " + str(Weight))
    BMI = Weight/(Height*Height)
    print("BMI = " + str(BMI))
    if (BMI < 18.5):
        classification = "under weight"
    elif (BMI > 25.0):
        classification = "over weight"
    else:
        classification = "normal weight"
    print("classification = " + str(classification))
calc_bmi(Weight = 57, Height = 1.73)
