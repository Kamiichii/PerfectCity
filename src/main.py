from input import input_and_calculate
from Attributes import Attributes



def main():
   city_scores_dict = {}
   input_and_calculate(Attributes.AVERAGE_ANNUAL_TEMP,city_scores_dict)
   print(city_scores_dict)
   

main()