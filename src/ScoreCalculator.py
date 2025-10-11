import csv
from Attributes import create_values_list,Attributes

def calculate_all(attribute,input_value,importance_value,city_scores_dict):
    with open("./data/CityAttributes.csv", newline="") as csvfile:
        reader = csv.DictReader(csvfile)  
        for row in reader:
            city_name = row["City"]
            attribute_value = row[attribute.value]
            distance = calculate_distance(attribute,input_value,attribute_value)
            score=calculate_score(distance,importance_value)
            if city_name in city_scores_dict:
                city_scores_dict[city_name] += score
            else:
                city_scores_dict[city_name] = score
        
def calculate_distance(attribute,input_value,internal_value):
    value_list = create_values_list(attribute)
    input_index = value_list.index(input_value)
    internal_value_index = value_list.index(internal_value)
    distance = abs(input_index - internal_value_index)
    if attribute == Attributes.CONTINENT:
        if distance == 0:
            return distance
        return 1
    return distance

def calculate_score(distance,importance_value):
    importance = int(importance_value)
    if (importance == 0):
        return 0   
    else:
        return distance * (3 ** importance)

def calculate_score_bar(score):
    number_of_attributes=len(Attributes)
    worst_score = number_of_attributes * (4 * (3 ** 5))
    single_bar = worst_score / 10
    new_score = worst_score - score
    number_of_bars = new_score//single_bar
    return number_of_bars