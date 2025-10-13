from Attributes import create_values_list
from ScoreCalculator import calculate_all
from ai import create_system_prompt,use_ai
from colorama import Fore,Style,init
init()

def input_and_calculate(attribute,dict,path):
    inputs = take_input(attribute)
    value = inputs[0]
    importance = inputs[1]
    calculate_all(attribute=attribute,input_value=value,importance_value=importance,city_scores_dict=dict,path=path)


def take_input(attribute):
    output = []
    value_dict = {}
    shown_list = []
    for i, item in enumerate(create_values_list(attribute),start=1):
        shown_list.append(f"{i}: {item}")
        value_dict[i] = item
    value_string = "\n".join(shown_list)
    value = input("How do you want your city to be:\n" + value_string +"\n")  
    for i,att_val in value_dict.items():
        if value.strip() == "":
            print(f"{Fore.RED}Please enter one of the choices{Style.RESET_ALL}")
            return take_input(attribute)
        if value.isdigit():
            if int(value) == i:
                output.append(value_dict[i])
                break
        elif value.strip().capitalize() in att_val:
                output.append(att_val)
                break
    if len(output) == 0:    
        print(f"{Fore.RED}Please enter one of the choices{Style.RESET_ALL}")
        return take_input(attribute)      
    output.append(take_importance())
    return output

    

def take_importance():
    importance = input("How important is this attribute for you from 0-5, 0 being I dont care and 5 being absoulute must\n")
    try:
        importance = int(importance)  
        if importance not in range(0, 6):  
            raise ValueError
    except ValueError:
        print("Please enter a number between 0 and 5")
        return take_importance()  

    return importance       

def replay_question():
    replay = input("Do you want to select new attributes y/n\n").strip().lower()
    if replay in ("y","yes"):
        return True
    elif replay in ("n","no"):
        return False
    else:
        print("Please type yes or no")
        return replay_question()

def ai_question(final_list):
    ask_for_ai = input("Do you want to know more about these cities?\n")
    if ask_for_ai.strip().lower() in ("yes","y"):
        continue_using_ai = True
        system_prompt = create_system_prompt(final_list)
        user_input = input("Which city do you want to know more about\n")
        use_ai(user_input=user_input,system_prompt=system_prompt)
        while(continue_using_ai):
            user_input = input("Type quit to exit ai or continue asking questions\n")
            if user_input.strip().lower() in ("quit","q"):
                continue_using_ai = False
            else:
                use_ai(user_input=user_input,system_prompt=system_prompt)
    elif ask_for_ai.strip().lower() in ("no","n"):
        print("I hope you enjoyed this app")
    else:
        print("Please enter yes or no")
        ai_question(final_list)
