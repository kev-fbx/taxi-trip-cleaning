import pandas as pd
import json


def isweekend(date):

    # read in dataframe and acquire datetime object.
    datetime = pd.to_datetime(date, dayfirst=True)

    # check if it is weekday (<6)(0) or weekend (1).
    if datetime.day_of_week < 6:
        return 0
    else:
        return 1


def task4():

    df = pd.read_csv('trips_january.csv')

    df['isWeekend'] = df['lpep_pickup_datetime'].apply(isweekend)

    percentage = (df['isWeekend'].sum()/len(df)) * 100

    json_dict = {'Percentage of weekend trips in January': 0}
    json_dict['Percentage of weekend trips in January'] = round(percentage, 2)

    with open('output/task4_summary.json', 'w') as output:
        json.dump(json_dict, output)

    return