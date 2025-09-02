from enum import Enum

class Attributes(Enum):
    AVERAGE_ANNUAL_TEMP = "AverageTemperature"
    YEARLY_RAINFALL = "Rainfall"
    AVERAGE_ANNUAL_CLEAR_DAYS = "Cloudiness"
    POPULATION = "Population"


def create_values_list(attribute):
    match attribute:
        case Attributes.AVERAGE_ANNUAL_TEMP:
            return ["Freezing(<0C°)","Cold(0C°-10C°)","Cool(10C°-18C°)","Warm(18C°-24C°)","Hot(24C°>)"]
        case Attributes.YEARLY_RAINFALL:
            return ["Arid(<250mm)","Dry(250mm-500mm)","Moderate(500mm-1000mm)","Wet(1000mm-2000mm)","VeryWet(2000mm>)"]
        case Attributes.AVERAGE_ANNUAL_CLEAR_DAYS:
            return ["VeryCloudy(0-20%)","MostlyCloudy(20-40%)","Balanced(40-60%)","MostlyClear(60-80%)","VeryClear(>80%)"]
        case Attributes.POPULATION:
            return ["Tiny(<50.000)","Small(50.000-200.000)","Medium(200.000-1.000.000)","Large(1.000.000-5.000.000)","VeryLarge(5.000.000-10.000.000)","Mega(>10.000.000)"]
        case _:
            raise Exception("Enter a proper Attributes.Enum value")
        


             
                





