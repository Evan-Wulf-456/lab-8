
import pandas as pd


def task_1_load_explore():
    # Load the dataset
    df = pd.read_csv("labour.csv")

    # Display the first five rows
    print(df.head(5))

    # Display column names, dimensions, and data types
    print(df.columns)
    print(df.shape)
    print(df.dtypes)

    # Display wage_increase_first_year as a Series
    print(df["wage-increase-first-year"])

    return df


def task2_access_data(df):

    # Select columns as Series
    first_year = df["wage-increase-first-year"]
    second_year = df["wage-increase-second-year"]

    # Retrieve first value using iloc and loc
    print("First value using iloc:", first_year.iloc[0])
    print("First value using loc:", first_year.loc[0])

    # Display first five rows
    print("First five rows:")
    print(first_year.iloc[0:5])

    # Select two columns as a DataFrame
    selected_columns = df[
        ["wage-increase-first-year",
         "wage-increase-second-year"]
    ]

    print("Selected columns:")
    print(selected_columns)

    # Retrieve a specific value using loc
    print("Specific value:", second_year.loc[7])

    # Select multiple rows and columns using iloc
    print("Multiple rows and columns using iloc:")
    print(df.iloc[0:5, 0:2])

    # Select multiple rows and columns using loc
    print("Multiple rows and columns using loc:")
    print(df.loc[0:4, [
        "wage-increase-first-year",
        "wage-increase-second-year"
    ]])

    return selected_columns


def task3_filter_data(df):

    # Select disputes with good and bad outcomes
    good_outcome = df[df["class"] == "good"]
    bad_outcome = df[df["class"] == "bad"]

    # Wage increase greater than 2.5
    wage_filter = df[
        df["wage-increase-first-year"] > 2.5
    ]

    # Statutory holidays greater than 10
    holiday_filter = df[
        df["statutory-holidays"] > 10
    ]

    # Both conditions
    both_conditions = df[
        (df["wage-increase-first-year"] > 2.5) &
        (df["statutory-holidays"] > 10)
    ]

    # Calculate average and maximum
    average = df["wage-increase-first-year"].mean()
    maximum = df["wage-increase-first-year"].max()

    return (
        good_outcome,
        bad_outcome,
        wage_filter,
        holiday_filter,
        both_conditions,
        average,
        maximum
    )


def main():

    # Task 1
    df = task_1_load_explore()

    # Task 2
    task2_access_data(df)

    # Task 3
    results = task3_filter_data(df)

    good, bad, wage, holidays, both, average, maximum = results

    print("\nTask 3 Results")
    print("Good outcomes:", len(good))
    print("Bad outcomes:", len(bad))
    print("Wage increase > 2.5:", len(wage))
    print("Statutory holidays > 10:", len(holidays))
    print("Both conditions:", len(both))
    print("Average wage increase:", average)
    print("Maximum wage increase:", maximum)

    # Special-case tests
    print("\nOne row:")
    print(df.iloc[[0]])

    print("\nMultiple rows:")
    print(df.iloc[0:5])

    print("\nNo matching rows:")
    print(df[df["wage-increase-first-year"] > 100])

    # Missing-value test
    print("\nMissing values:")
    print(df["wage-increase-first-year"].isna().sum())

    print("\nMean with missing values:")
    print(df["wage-increase-first-year"].mean())


if __name__ == "__main__":
    main()
