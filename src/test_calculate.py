import unittest
from ScoreCalculator import *
from Attributes import Attributes


class TestCalculateDistence(unittest.TestCase):
    def test_calculate_dist_zero(self):
        output = calculate_distance(Attributes.AVERAGE_ANNUAL_CLEAR_DAYS,"Verycloudy(0-20%)","Verycloudy(0-20%)")
        self.assertEqual(output,0)
    def test_calculate_dist_non_zero(self):
        output = calculate_distance(Attributes.AVERAGE_ANNUAL_CLEAR_DAYS,"Verycloudy(0-20%)","Veryclear(>80%)")
        self.assertEqual(output,4)
    def test_calculate_att_dif_continent(self):
        output = calculate_distance(Attributes.CONTINENT,"Europe","Africa")
        self.assertEqual(output,1)
    def test_calculate_dist_non_zero_reversed(self):
        output = calculate_distance(Attributes.AVERAGE_ANNUAL_CLEAR_DAYS,"Veryclear(>80%)","Verycloudy(0-20%)")
        self.assertEqual(output,4)

class TestCalculateScore(unittest.TestCase):
    def test_calculate_score_importance_zero(self):
        output= calculate_score(4,0)
        self.assertEqual(output,0)
    def test_calculate_score_distance_zero(self):
        output= calculate_score(0,5)
        self.assertEqual(output,0)
    def test_calculate_score_non_zero(self):
        output= calculate_score(3,2)
        self.assertEqual(output,27)

class TestCalculateAll(unittest.TestCase):
    def test_calculate_all_importance_zero(self):
        new_dict = {}
        final_dict ={"Yakutsk":0,"Oslo":0,"Istanbul":0,"Cairo":0,"Bankok":0,"Denver":0,"Kuching":0,"Ronda":0,"Innsbruck":0,"Osaka":0,"Rio":0,"Sydney":0}
        calculate_all(Attributes.POPULATION,"Tiny(<50.000)",0,new_dict,"./data/TestAttributes.csv")
        self.assertEqual(new_dict,final_dict) 
    def test_calculate_all_importance_non_zero(self):
        new_dict = {}
        final_dict ={"Yakutsk":18,"Oslo":18,"Istanbul":45,"Cairo":45,"Bankok":45,"Denver":36,"Kuching":18,"Ronda":0,"Innsbruck":9,"Osaka":27,"Rio":36,"Sydney":27}
        calculate_all(Attributes.POPULATION,"Tiny(<50.000)",2,new_dict,"./data/TestAttributes.csv")
        self.assertEqual(new_dict,final_dict)
    def test_calculate_all_importance_non_zero_list_exists(self):
        new_dict = {"Yakutsk":0,"Oslo":0,"Istanbul":0,"Cairo":0,"Bankok":0,"Denver":0,"Kuching":0,"Ronda":0,"Innsbruck":0,"Osaka":0,"Rio":0,"Sydney":0}
        final_dict ={"Yakutsk":18,"Oslo":18,"Istanbul":45,"Cairo":45,"Bankok":45,"Denver":36,"Kuching":18,"Ronda":0,"Innsbruck":9,"Osaka":27,"Rio":36,"Sydney":27}
        calculate_all(Attributes.POPULATION,"Tiny(<50.000)",2,new_dict,"./data/TestAttributes.csv")
        self.assertEqual(new_dict,final_dict)  