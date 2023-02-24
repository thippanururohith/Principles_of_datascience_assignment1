import pandas as pd
import matplotlib.pyplot as plt
import json
# import dataFile name form config file
# config is in the parent directory of the current directory
import sys
sys.path.append('../')

dataFile = ""
# imort rawDataFile from config
with open ('config.json') as config_file:
    config = json.load(config_file)

if config and config.get('rawDataFile'):
    dataFile = config.get('rawDataFile')
else:
    print('Error: config file is missing or invalid')
    sys.exit(1)



# Load the data from the CSV file
data = pd.read_csv(dataFile)

# Calculate the average math score for each race
avg_math_by_race = data.groupby('race/ethnicity')['math score'].mean()

# Create a bar chart of the average math score by race
plt.bar(avg_math_by_race.index, avg_math_by_race)
plt.title('Average Math Score by Race')
plt.xlabel('Race')
plt.ylabel('Average Math Score')
plt.show()
plt.savefig('figures/BarChartRaceAvgMathScore.png')
