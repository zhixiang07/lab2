def calc_bmi(Height, Weight):
    print("height= " + str(Height))
    print("weight = " + str(Weight))
    BMI = Weight/(Height*Height)
    print("BMI = " + str(BMI))
    if (BMI < 18.5):
        classification = "-1"
    elif (BMI > 25.0):
        classification = "1"
    else:
        classification = "0"
    print("classification = " + str(classification))
    return classification

result = calc_bmi(Weight = 100, Height = 1.73)



