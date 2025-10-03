from input import input_and_calculate,replay_question
from Attributes import Attributes



def main():
   replay = True
   while replay:
      city_scores_dict = {}
      input_and_calculate(Attributes.AVERAGE_ANNUAL_TEMP,city_scores_dict) 
      input_and_calculate(Attributes.YEARLY_RAINFALL,city_scores_dict)
      input_and_calculate(Attributes.AVERAGE_ANNUAL_CLEAR_DAYS,city_scores_dict)
      input_and_calculate(Attributes.POPULATION,city_scores_dict)
      input_and_calculate(Attributes.CONTINENT,city_scores_dict)
      sorted_dict = dict(sorted(city_scores_dict.items(),key=lambda item: item[1]))
      top10 =list(sorted_dict.keys())[:10]
      print(f"Your top 10 city recommendations are: {top10}")
      replay = replay_question()

   

main()