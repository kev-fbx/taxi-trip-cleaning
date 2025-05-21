import pandas as pd
import matplotlib.pyplot as plt


def start_hour(date):

    datetime = pd.to_datetime(date, dayfirst=True)
    return datetime.hour


def isweekend(date):

    # read in dataframe and acquire datetime object.
    datetime = pd.to_datetime(date, dayfirst=True)

    # check if it is weekday (<6)(0) or weekend (1).
    if datetime.day_of_week < 6:
        return 0
    else:
        return 1


def task5():

    df = pd.read_csv('trips_january.csv')

    df['hour'] = df['lpep_pickup_datetime'].apply(start_hour)
    df['isWeekend'] = df['lpep_pickup_datetime'].apply(isweekend)

    trips_weekend = df[df['isWeekend'] == 1]
    trips_weekday = df[df['isWeekend'] == 0]

    bins = [0, 7, 9, 12, 16, 20, 24]

    # weekend plot
    plt.figure()
    plt.hist(trips_weekend['hour'], bins=bins)
    plt.title('Histogram of Green Taxi trip start times\
 in January 2023 weekends')
    plt.xlabel('Trip Start Time (H)')
    plt.ylabel('Frequency')
    plt.xticks(bins)
    plt.savefig('output/task5_histogram_weekend.png', format='PNG')

    # weekday plot
    plt.figure()
    plt.hist(trips_weekday['hour'], bins=bins)
    plt.title('Histogram of Green Taxi trip start times\
 in January 2023 weekdays')
    plt.xlabel('Trip Start Time (H)')
    plt.ylabel('Frequency')
    plt.xticks(bins)
    plt.savefig('output/task5_histogram_weekday.png', format='PNG')

    return