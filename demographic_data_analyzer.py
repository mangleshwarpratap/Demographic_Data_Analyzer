import pandas as pd


def calculate_demographic_data(print_data=True):   
    # Read data from file
    df = pd.read_csv("adult.data.csv")
    df.columns = ['age', 'workclass', 'fnlwgt', 'education', 'education-num',
       'marital-status', 'occupation', 'relationship', 'race', 'sex',
       'capital-gain', 'capital-loss', 'hours-per-week', 'native-country',
       'salary']
    
    people_count = df['education'].count()
    

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = pd.Series(df['race'].value_counts())

    # What is the average age of men?
    average_age_men = pd.Series(df['age'].mean())

    # What is the percentage of people who have a Bachelor's degree?
    people_count = df['education'].count()
    people_bachelors = df['education'].value_counts()
    percentage_bachelors = (people_bachelors['Bachelors']/people_count) * 100
    

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    result_series = df.loc[df['salary'] == '>50K' ,'education']
    desired_educations = ['Bachelors', 'Masters','Doctorate']
    higher_education = result_series[result_series.isin(desired_educations)]
    lower_education = result_series[~result_series.isin(desired_educations)]
    
    # print(result_series.count())
    # print(higher_education.count())

    # percentage with salary >50K
    higher_education_rich = (higher_education.count()/people_count) * 100
    lower_education_rich = (lower_education.count()/people_count) * 100

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    result_series = df.loc[df['salary'] == '>50K' ,'hours-per-week']
    #min_hour = [1]
    num_min_workers = result_series[result_series.isin([min_work_hours])]
    
    rich_percentage = (num_min_workers.count()/people_count) * 100

    # What country has the highest percentage of people that earn >50K?

    highest_earning_country_list = df.loc[df['salary'] == '>50K' , 'native-country']
    highest_earning_country =  highest_earning_country_list.value_counts().idxmax()
    

    highest_earning_country_percentage =(highest_earning_country_list.count()/people_count) * 100

    # Identify the most popular occupation for those who earn >50K in India.
    india_high_earners = df[(df['salary'] == '>50K') & (df['native-country'] == 'India')]
    occupation_counts = india_high_earners['occupation'].value_counts()
    top_IN_occupation = occupation_counts.idxmax()

    

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }

calculate_demographic_data()
