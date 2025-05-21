import pandas as pd
import matplotlib.pyplot as plt


def dayname(date):
    datetime = pd.to_datetime(date, dayfirst=True)
    return datetime.dayofweek


def mean_duration_calc(df):
    return df['trip_duration'].mean()


def task7():

    df = pd.read_csv('trips_january.csv')

    df['dayofweek'] = df['lpep_pickup_datetime'].apply(dayname)

    df['lpep_pickup_datetime'] = pd.to_datetime(df['lpep_pickup_datetime'],
                                                dayfirst=True)

    df['lpep_dropoff_datetime'] = pd.to_datetime(df['lpep_dropoff_datetime'],
                                                 dayfirst=True)

    df['trip_duration'] = (df['lpep_dropoff_datetime']
                           - df['lpep_pickup_datetime'])

    mean_duration = df.groupby('dayofweek') .apply(mean_duration_calc)

    legend = ['Monday', 'Tuesday', 'Wednesday',
              'Thursday', 'Friday', 'Saturday', 'Sunday']

    fig, ax = plt.subplots(figsize=(6, 6))

    ax.pie(mean_duration,
           labels=legend,
           autopct='%.2f%%')

    ax.set_title('Pie Chart of Mean Trip Duration for Each Day of the Week')
    plt.savefig('output/task7_pie.png', format='PNG')

    return