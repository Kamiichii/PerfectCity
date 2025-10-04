from input import input_and_calculate,replay_question
from Attributes import Attributes
from colorama import Fore,Style,init
init()


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
      top10 =list(sorted_dict)[:10]
      for i, city in enumerate(top10,start=1):
         if i <= 3:
            color = Fore.GREEN
         elif i <= 7:
               color = Fore.YELLOW
         else:
               color = Fore.RED
         print(f"{i}. {color}{city} {Style.RESET_ALL}")
      replay = replay_question()
   
main()