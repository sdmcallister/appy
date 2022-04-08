from datetime import datetime, timedelta

ROUTINE = ['Day1', 'Cardio', 'Day2', 'Cardio', 'Day3', 'Opt', 'Opt']
PLATEPAIRS = [35, 25, 25, 10, 10, 10, 10, 5, 2.5]
REPPERWEEK = [5, 6, 7, 8, 9, 10]
EXERCISES = ['Front Squat', 'Press', 'Deadlift']

startdate = datetime.strptime('2022-04-04', '%Y-%m-%d')
# day 1, 2, 3
pushups = [18, 14, 16]
chinups = [8, 6, 7]
sets = [3, 5, 4]
maxlifts = [120.0, 85.0, 185.0]


def toPlates(weight, platepairs, holder=45, increment=5.0):
    """Calculate needed plates based on weight for one side."""
    weight = weight - (weight % increment)
    oneside = (weight - holder) / 2
    result = ['--']
    for plate in platepairs:
        if plate > oneside:
            continue
        else:
            result.append(str(plate))
            oneside -= plate
    if oneside > 0:
        print("Warning. Leftover Weight=", oneside)
    if len(result) == 0:
        return 'bar'
    else:
        return "|".join(result)


d = {}
for reps in REPPERWEEK:
    for day in ROUTINE:
        date_str = startdate.strftime('%Y-%m-%d')
        d[date_str] = [f'Date: {date_str}\n']
        startdate = startdate + timedelta(days=1)
        if day == 'Cardio':
            d[date_str
              ].append('Go Running or Biking! 20-30 Min.')
        elif day == 'Opt':
            d[date_str
              ].append('Rest or Cross Training.')
        else:
            if day == 'Day1':
                idx = 0
            elif day == 'Day2':
                idx = 1
            else:
                idx = 2
            d[date_str].append(
                f'{EXERCISES[idx]} - Working Set: {maxlifts[idx]} for {reps} reps.')
            d[date_str
              ].append(f'Warmup 1: {toPlates(maxlifts[idx] * 0.50,PLATEPAIRS)}')
            d[date_str
              ].append(f'Warmup 2: {toPlates(maxlifts[idx] * 0.75,PLATEPAIRS)}')
            d[date_str
              ].append(f'Working Set: {toPlates(maxlifts[idx],PLATEPAIRS)}')
            d[date_str
              ].append(f'Chinups: {sets[idx]} sets of {chinups[idx]}')
            d[date_str
              ].append(f'Pushups: {sets[idx]} sets of {pushups[idx]}')
