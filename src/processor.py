import numpy as np
import pandas as pd
from pathlib import Path

def calc_aqi(parameter: str, concentration: int) -> None:
    """ Calculates the air quality index """
    
    breakpoints = {
        'pm25': [10, 20, 25, 50, 75],
        'pm10': [20, 40, 50, 100, 150],
        'no2':  [40, 90, 120, 230, 340],
        'o3':   [50, 100, 130, 240, 380],
        'so2':  [100, 200, 350, 500, 750]
    }

    # No AQI defintion for parameter no or co
    if parameter == 'no' or parameter == 'co':
        return {'level': np.nan, 'category': np.nan, 'color': np.nan}
    else:
        bounds = breakpoints[parameter]

    # Determine Level based on ranges
    if concentration <= bounds[0]:
        return {'level': 1, 'category': 'Good', 'color': '#50CCAA'}
    elif concentration <= bounds[1]:
        return {'level': 2, 'category': 'Fair', 'color': '#A0E632'}
    elif concentration <= bounds[2]:
        return {'level': 3, 'category': 'Moderate', 'color': '#FFD700'}
    elif concentration <= bounds[3]:
        return {'level': 4, 'category': 'Poor', 'color': '#FF6E6E'}
    elif concentration <= bounds[4]:
        return {'level': 5, 'category': 'Very Poor', 'color': '#A0004B'}
    else:
        return {'level': 6, 'category': 'Extremely Poor', 'color': '#730023'}

def map_aqi_level(levels) -> str:
    """ Maps a aqi level to verbose output """

    max_level = levels.max()

    level_map = {
        1: 'Good',
        2: 'Fair',
        3: 'Moderate',
        4: 'Poor',
        5: 'Very Poor'
    }
    
    return level_map.get(max_level, 'Extremely Poor')

if __name__ == '__main__':
    # Change work dir to top project level
    try:
        script_path = Path(__file__).resolve()
    except NameError:
        script_path = Path.cwd()

    df = pd.read_csv("data/merged_data.csv")

    df[['level', 'category', 'color']] = df.apply(lambda row: calc_aqi(row['parameter'], row['value']), axis=1, result_type='expand')

    grouped_df = df.groupby(['location_id', 'datetime'])
    max_level_per_group = grouped_df['level'].agg(map_aqi_level).rename('poorest_aqi')
    df = df.merge(max_level_per_group, 
                  on=['location_id', 'datetime'], 
                  how='left')
    
    # Fill NAs in cos level, category and color
    df['level'].fillna(value=-1, inplace=True)
    df['category'].fillna(value="No Entry", inplace=True)
    df['color'].fillna(value='#808080', inplace=True)

    print(df.head(10))
    df.to_csv("data/aq_data.csv")