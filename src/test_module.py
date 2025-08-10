import unittest
from demographic_data_analyzer import *

expected_average_age = 39.4
expected_bachelors_percentage = 16.4
expected_advanced_education_salary_percentage = 46.5
expected_no_advanced_education_salary_percentage = 17.4
expected_minimum_hours = 1
expected_minimum_hours_salary_percentage = 10.0
expected_country = "Iran"
expected_percentage = 41.9
expected_occupation = "Prof-specialty"
total_population = 32561

class TestDemographicDataAnalyzer(unittest.TestCase):
    def test_race_count(self):
        self.assertEqual(race_count().sum(), total_population)

    def test_average_age_men(self):
        self.assertAlmostEqual(average_age_men(), expected_average_age, places=1)

    def test_bachelors_percentage(self):
        self.assertAlmostEqual(bachelors_percentage(), expected_bachelors_percentage, places=1)

    def test_advanced_education_salary_percentage(self):
        self.assertAlmostEqual(advanced_education_salary_percentage(), expected_advanced_education_salary_percentage, places=1)

    def test_no_advanced_education_salary_percentage(self):
        self.assertAlmostEqual(no_advanced_education_salary_percentage(), expected_no_advanced_education_salary_percentage, places=1)

    def test_minimum_hours_per_week(self):
        self.assertEqual(minimum_hours_per_week(), expected_minimum_hours)

    def test_minimum_hours_salary_percentage(self):
        self.assertAlmostEqual(minimum_hours_salary_percentage(), expected_minimum_hours_salary_percentage, places=1)

    def test_highest_earning_country(self):
        self.assertEqual(highest_earning_country(), (expected_country, expected_percentage))

    def test_most_popular_occupation_in_india(self):
        self.assertEqual(most_popular_occupation_in_india(), expected_occupation)

if __name__ == '__main__':
    unittest.main()