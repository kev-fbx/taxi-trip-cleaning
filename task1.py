import pandas as pd
import json


def task1():

    total_trip_time = 0
    trip_duration = []
    json_dict = {'Number of records in January': 0,
                 'Mean trip duration in January': 0}

    df = pd.read_csv('trips_january.csv')

    for time in range(len(df)):

        # Find each trip's start and end times.
        trip_start = df.loc[time, 'lpep_pickup_datetime']
        trip_end = df.loc[time, 'lpep_dropoff_datetime']

        # Convert the times into datetime objects.
        start = pd.to_datetime(trip_start, dayfirst=True)
        end = pd.to_datetime(trip_end, dayfirst=True)

        # Convert the calculated duration into minutes.
        duration = end - start
        duration_minutes = duration.total_seconds() / 60

        # Append the duration_minutes to the trip_duration list.
        trip_duration.append(duration_minutes)

        # Sum up all trip times to find the average.
        total_trip_time += duration_minutes

    df['trip_duration'] = trip_duration

    json_dict['Number of records in January'] = len(df)
    json_dict['Mean trip duration in January'] = round(
        total_trip_time / len(df), 2)

    with open('output/task1_summary.json', 'w') as output:
        json.dump(json_dict, output)

    return