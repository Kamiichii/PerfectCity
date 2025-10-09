from input import input_and_calculate,replay_question,ai_question
from Attributes import Attributes
from colorama import Fore,Style,init
init()


def main():
   
   replay = True
   final_list = []
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
         colored_item = f"{i}. {color}{city} {Style.RESET_ALL}"
         uncolored_item = f"{i}. {city}"
         final_list.append(uncolored_item)
         print(colored_item)
      replay = replay_question()
   ai_question("\n".join(final_list))
main()