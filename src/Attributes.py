from enum import Enum

class Attributes(Enum):
    AVERAGE_ANNUAL_TEMP = "temp"
    YEARLY_RAINFALL = "rain"
    AVERAGE_ANNUAL_CLEAR_DAYS = "clear"
    POPULATION = "population"


def create_values_list(attribute):
    match attribute:
        case Attributes.AVERAGE_ANNUAL_TEMP:
            return ["Freezing(<0C°)","Cold(0C°-10C°)","Cool(10C°-18C°)","Warm(18C°-24C°)","Hot(24C°>)"]
        case Attributes.YEARLY_RAINFALL:
            return ["Arid(<250mm)","Dry(250mm-500mm)","Moderate(500mm-1000mm)","Wet(1000mm-2000mm)","Very wet(2000mm>)"]
        case Attributes.AVERAGE_ANNUAL_CLEAR_DAYS:
            return ["Very Cloudy(0-20%)","Mostly Cloudy(20-40%)","Balanced(40-60%)","Mostly Clear(60-80%)","Very Clear(>80%)"]
        case Attributes.POPULATION:
            return ["Tiny(<50,000)","Small(50,000-200,000)","Medium(200,000-1,000,000)","Large(1,000,000-5,000,000)","Very Large(5,000,000-10,000,000)","Mega(>10,000,000)"]
        case _:
            raise Exception("Enter a proper Attributes.Enum value")
        
def calculate_distance(input_value,internal_value,value_list):
    input_index = value_list.index(input_value)
    internal_value_index = value_list.index(internal_value)
    return abs(input_index - internal_value_index)

             
                





