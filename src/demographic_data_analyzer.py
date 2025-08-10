# File: /demographic-data-analyzer/demographic-data-analyzer/src/demographic_data_analyzer.py

import pandas as pd

class DemographicDataAnalyzer:
    def __init__(self, data_file):
        columns = [
            "age", "workclass", "fnlwgt", "education", "education-num",
            "marital-status", "occupation", "relationship", "race", "sex",
            "capital-gain", "capital-loss", "hours-per-week", "native-country", "salary"
        ]
        self.data = pd.read_csv(data_file, names=columns, header=None)
        self.data = self.data.map(lambda x: x.strip() if isinstance(x, str) else x)
        self.race_counts = None
        self.average_age_men = None
        self.bachelors_percentage = None
        self.higher_education_rich = None
        self.lower_education_rich = None
        self.min_work_hours = None
        self.rich_percentage_min_hours = None
        self.highest_earning_country = None
        self.highest_earning_country_percentage = None
        self.top_IN_occupation = None

    def calculate_race_counts(self):
        self.race_counts = self.data['race'].value_counts()

    def calculate_average_age_men(self):
        self.average_age_men = round(self.data[self.data['sex'] == 'Male']['age'].mean(), 1)

    def calculate_bachelors_percentage(self):
        total_people = len(self.data)
        bachelors_count = len(self.data[self.data['education'] == "Bachelors"])
        self.bachelors_percentage = round((bachelors_count / total_people) * 100, 1) if total_people > 0 else 0

    def calculate_advanced_education_percentages(self):
        advanced = ["Bachelors", "Masters", "Doctorate"]
        higher_edu = self.data[self.data['education'].isin(advanced)]
        lower_edu = self.data[~self.data['education'].isin(advanced)]

        higher_edu_rich = higher_edu[higher_edu['salary'] == '>50K']
        lower_edu_rich = lower_edu[lower_edu['salary'] == '>50K']

        self.higher_education_rich = round((len(higher_edu_rich) / len(higher_edu)) * 100, 1) if len(higher_edu) > 0 else 0
        self.lower_education_rich = round((len(lower_edu_rich) / len(lower_edu)) * 100, 1) if len(lower_edu) > 0 else 0

    def calculate_min_work_hours(self):
        self.min_work_hours = self.data['hours-per-week'].min()

    def calculate_rich_percentage_min_hours(self):
        min_hours = self.min_work_hours if self.min_work_hours is not None else self.data['hours-per-week'].min()
        min_workers = self.data[self.data['hours-per-week'] == min_hours]
        rich_min_workers = min_workers[min_workers['salary'] == '>50K']
        self.rich_percentage_min_hours = round((len(rich_min_workers) / len(min_workers)) * 100, 1) if len(min_workers) > 0 else 0

    def calculate_highest_earning_country(self):
        country_counts = self.data['native-country'].value_counts()
        rich = self.data[self.data['salary'] == '>50K']
        rich_country_counts = rich['native-country'].value_counts()
        percents = (rich_country_counts / country_counts * 100).round(1)
        percents = percents.dropna()
        if not percents.empty:
            self.highest_earning_country = percents.idxmax()
            self.highest_earning_country_percentage = percents.max()
        else:
            self.highest_earning_country = None
            self.highest_earning_country_percentage = 0

    def calculate_top_IN_occupation(self):
        india_rich = self.data[(self.data['native-country'] == 'India') & (self.data['salary'] == '>50K')]
        if not india_rich.empty:
            self.top_IN_occupation = india_rich['occupation'].value_counts().idxmax()
        else:
            self.top_IN_occupation = None

    def analyze(self):
        self.calculate_race_counts()
        self.calculate_average_age_men()
        self.calculate_bachelors_percentage()
        self.calculate_advanced_education_percentages()
        self.calculate_min_work_hours()
        self.calculate_rich_percentage_min_hours()
        self.calculate_highest_earning_country()
        self.calculate_top_IN_occupation()
        return {
            'race_counts': self.race_counts,
            'average_age_men': self.average_age_men,
            'bachelors_percentage': self.bachelors_percentage,
            'higher_education_rich': self.higher_education_rich,
            'lower_education_rich': self.lower_education_rich,
            'min_work_hours': self.min_work_hours,
            'rich_percentage_min_hours': self.rich_percentage_min_hours,
            'highest_earning_country': self.highest_earning_country,
            'highest_earning_country_percentage': self.highest_earning_country_percentage,
            'top_IN_occupation': self.top_IN_occupation
        }

def analyze_demographics(data_file):
    analyzer = DemographicDataAnalyzer(data_file)
    return analyzer.analyze()

DATA_FILE = "demographic_data.csv" 

def race_count():
    analyzer = DemographicDataAnalyzer(DATA_FILE)
    analyzer.calculate_race_counts()
    return analyzer.race_counts

def average_age_men():
    analyzer = DemographicDataAnalyzer(DATA_FILE)
    analyzer.calculate_average_age_men()
    return analyzer.average_age_men

def bachelors_percentage():
    analyzer = DemographicDataAnalyzer(DATA_FILE)
    analyzer.calculate_bachelors_percentage()
    return analyzer.bachelors_percentage

def advanced_education_salary_percentage():
    analyzer = DemographicDataAnalyzer(DATA_FILE)
    analyzer.calculate_advanced_education_percentages()
    return analyzer.higher_education_rich

def no_advanced_education_salary_percentage():
    analyzer = DemographicDataAnalyzer(DATA_FILE)
    analyzer.calculate_advanced_education_percentages()
    return analyzer.lower_education_rich

def minimum_hours_per_week():
    analyzer = DemographicDataAnalyzer(DATA_FILE)
    analyzer.calculate_min_work_hours()
    return analyzer.min_work_hours

def minimum_hours_salary_percentage():
    analyzer = DemographicDataAnalyzer(DATA_FILE)
    analyzer.calculate_min_work_hours()
    analyzer.calculate_rich_percentage_min_hours()
    return analyzer.rich_percentage_min_hours

def highest_earning_country():
    analyzer = DemographicDataAnalyzer(DATA_FILE)
    analyzer.calculate_highest_earning_country()
    return (analyzer.highest_earning_country, analyzer.highest_earning_country_percentage)

def most_popular_occupation_in_india():
    analyzer = DemographicDataAnalyzer(DATA_FILE)
    analyzer.calculate_top_IN_occupation()
    return analyzer.top_IN_occupation