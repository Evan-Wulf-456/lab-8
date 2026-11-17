'''Task 3: Filtering and Analyzing Data
Implement task3_filter_data(df) to:
1.	Select all disputes with a good outcome.
2.	Select all disputes with a bad outcome.
3.	Select disputes where wage_increase_first_year > 2.5.
4.	Select disputes where statutory_holidays > 10.
5.	Select disputes satisfying both conditions:
o	wage_increase_first_year > 2.5
o	statutory_holidays > 10
6.	Calculate the average wage_increase_first_year.
7.	Calculate the maximum wage_increase_first_year.
Answer the following questions:
•	How many disputes have good and bad outcomes?
•	How many disputes satisfy both conditions?
•	What are the average and maximum first-year wage increases?
'''
import pandas as pd
read_csv = pd.read_csv('labor(1).csv')

def task3_filter_data(df):
    good_outcome = df[df['class'] == 'good']
    bad_outcome = df[df['class'] == 'bad']
    wage_increase_gt_2_5 = df[df['wage-increase-first-year'] > 2.5]
    statutory_holidays_gt_10 = df[df['statutory-holidays'] > 10]
    both_conditions = df[(df['wage-increase-first-year'] > 2.5) & (df['statutory-holidays'] > 10)]
    avg_wage_increase = df['wage-increase-first-year'].mean()
    max_wage_increase = df['wage-increase-first-year'].max()
    print(f'the good outcome is len{good_outcome}')
    print(f'the bad outcome is len{bad_outcome}')
    print(f'wage increase {wage_increase_gt_2_5}')
    print(f'statutory holidays{statutory_holidays_gt_10}')
    print(f'both conditions {both_conditions}')
    print(f'average wage increase {avg_wage_increase}')
    print(f'maximum wage increase {max_wage_increase}')
    return good_outcome, bad_outcome, wage_increase_gt_2_5, statutory_holidays_gt_10, both_conditions, avg_wage_increase, max_wage_increase


task3_filter_data(read_csv)


