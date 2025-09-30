from Attributes import create_values_list
from ScoreCalculator import calculate_all

def input_and_calculate(attribute,dict):
    inputs = take_input(attribute)
    value = inputs[0]
    importance = inputs[1]
    calculate_all(attribute,value,importance,dict)


def take_input(attribute):
    output = []
    value_list = create_values_list(attribute)
    value_string = ",".join(value_list)
    value = input("How do you want your city to be: " + value_string +"\n")  
    for instence in value_list:
        if value.strip().capitalize() in instence:
            output.append(instence)
            break
    if len(output) == 0:    
        print("Please enter one of the choices")
        return take_input(attribute)
        
    output.append(take_importance())
    return output

    

def take_importance():
    importance = input("How important is this attribute for you from 0-5, 0 being I dont care and 5 being absoulute must")
    try:
        importance = int(importance)  
        if importance not in range(0, 6):  
            raise ValueError
    except ValueError:
        print("Please enter a number between 0 and 5")
        return take_importance()  

    return str(importance)       



