from input import input_and_calculate,replay_question,ai_question
from Attributes import Attributes
from rich.table import Table
from rich.console import Console

#finish bar calculation logic
def main():
   console = Console()
   replay = True
   ai_list = []
   while replay:
      city_scores_dict = {}
      input_and_calculate(Attributes.AVERAGE_ANNUAL_TEMP,city_scores_dict) 
      input_and_calculate(Attributes.YEARLY_RAINFALL,city_scores_dict)
      input_and_calculate(Attributes.AVERAGE_ANNUAL_CLEAR_DAYS,city_scores_dict)
      input_and_calculate(Attributes.POPULATION,city_scores_dict)
      input_and_calculate(Attributes.CONTINENT,city_scores_dict)
      top10 = sorted(city_scores_dict.items(),key=lambda item: item[1])[:10]
      table = Table(title="Top 10 City Recommendations")
      table.add_column("Rank", justify="center", style="bold cyan")
      table.add_column("City",style="bold")
      for i, city in enumerate(top10,start=1):
         color = "green" if i <= 3 else "yellow" if i <= 7 else "red"
         table.add_row(str(i), f"[{color}]{city[0]}[/{color}]")
         item_for_ai_list = f"{i}. {city}"
         ai_list.append(item_for_ai_list)
      console.print(table)
      replay = replay_question()
   ai_question("\n".join(ai_list))
main()