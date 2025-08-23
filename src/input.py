from Attributes import Attributes,create_values_list
import re


def take_input(attribute):
    output = []
    value_list = create_values_list(attribute)
    value_string = ",".join(value_list)
    value = input("How do you want your city to be: " + value_string +"\n")
    match = re.findall(r"^(.*?)\(",value)
    if len(match) == 1:
        if match[0].strip().capitalize() in value_string:
            output.append(match[0].strip().capitalize())
        else:
            print("Please enter exactly one of the choices")
            return take_input(attribute)
    
    else:
        for instence in value_list:
            if value.strip().capitalize() in instence:
                output.append(instence)
        else:
            print("Please enter one of the choices")
            return take_input(attribute)
        
    output.append(take_importance())
    return output

    

def take_importance():
    importance = input("How important is this attribute for you from 0-5, 0 being I dont care and 5 being absoulute must")
    if int(importance) not in range (0,6):
        print("Please enter a number between 0 and 5")
        return take_importance()
    else:
        return int(importance)       


