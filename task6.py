import pandas as pd
import matplotlib.pyplot as plt


def dayname(date):
    datetime = pd.to_datetime(date, dayfirst=True)
    return datetime.dayofweek


def mean_stats(df):
    mean_distance = df['trip_distance'].mean()
    mean_cost = df['total_amount'].mean()
    return pd.Series({'mean_distance': mean_distance,
                      'mean_cost': mean_cost})


def task6():

    df = pd.read_csv('trips_january.csv')

    df['dayofweek'] = df['lpep_pickup_datetime'].apply(dayname)

    daily_average = df.groupby('dayofweek').apply(mean_stats)

    legend = ['Monday', 'Tuesday', 'Wednesday',
              'Thursday', 'Friday', 'Saturday', 'Sunday']

    plt.figure(figsize=(6, 6))

    for day_index, day_name in zip(daily_average.index, legend):
        plt.scatter(x=daily_average.loc[day_index, 'mean_cost'],
                    y=daily_average.loc[day_index, 'mean_distance'],
                    label=day_name)

    plt.title('Scatter Plot of Mean Trip Distance\n\
Against Mean Trip Cost for each Weekday')
    plt.xlabel('Mean Trip Cost ($)')
    plt.ylabel('Mean Trip Distance (mi)')
    plt.legend(legend)
    plt.xlim(21.5, 22.2)
    plt.savefig('output/task6_scatter.png', format='PNG')

    return