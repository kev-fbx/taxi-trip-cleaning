import pandas as pd
import json


def task2():

    json_dict = {'Percentage of abnormal trip distance records': 0}

    df = pd.read_csv('trips_january.csv')

    abormal_percent = round(((df['trip_distance'] <= 0.1) |
                            (df['trip_distance'] >= 17.3)).mean() * 100, 2)

    json_dict['Percentage of abnormal trip distance records'] = abormal_percent

    with open('output/task2_summary.json', 'w') as output:
        json.dump(json_dict, output)

    return