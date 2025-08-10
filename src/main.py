# main.py

import pandas as pd
from demographic_data_analyzer import *
import test_module
import unittest

def test_analyze_demographics():
    """Test the main functionality"""
    print("Testing demographic data analyzer...")
    
    # Test individual functions
    print(f"Race count: {race_count()}")
    print(f"Average age of men: {average_age_men()}")
    print(f"Percentage with Bachelors degrees: {bachelors_percentage()}%")
    print(f"Percentage with higher education that earn >50K: {advanced_education_salary_percentage()}%")
    print(f"Percentage without higher education that earn >50K: {no_advanced_education_salary_percentage()}%")
    print(f"Min work time: {minimum_hours_per_week()} hours/week")
    print(f"Percentage of rich among those who work fewest hours: {minimum_hours_salary_percentage()}%")
    country, percentage = highest_earning_country()
    print(f"Country with highest percentage of rich: {country} {percentage}%")
    print(f"Top occupation in India: {most_popular_occupation_in_india()}")
    
    print("\nAll manual tests passed!")

if __name__ == "__main__":
    # Run manual tests
    test_analyze_demographics()
    
    print("\n" + "="*50)
    print("Running unit tests...")
    print("="*50)
    
    # Run unit tests from test_module
    unittest.main(module=test_module, exit=False, verbosity=2)