import pandas as pd
import matplotlib.pyplot as plt


def start_time_sort(date):

    start_time = pd.to_datetime(date, dayfirst=True)
    start_hour = start_time.hour

    if 7 <= start_hour <= 11:
        return '07:00 - 11:00'
    elif 12 <= start_hour <= 15:
        return '12:00 - 15:00'


def task3():

    df = pd.read_csv('trips_january.csv')
    df['Start Time'] = df['lpep_pickup_datetime'].apply(start_time_sort)

    df.boxplot(column='total_amount',
               by='Start Time',
               figsize=(10, 8))

    plt.title('Boxplot comparing Green Taxi trip fares in January\n\
starting in the morning or afternoon')
    plt.xlabel('Trip Start Time (HH:MM)')
    plt.ylabel('Price ($)')
    plt.savefig('output/task3_boxplot.png', format='PNG')

    return