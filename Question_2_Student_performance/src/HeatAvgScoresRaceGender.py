import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import json
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

# Calculate the average scores by race and gender
avg_scores = data.groupby(['race/ethnicity', 'gender'])[['math score', 'reading score', 'writing score']].mean()

# Create a heatmap of the average scores
sns.heatmap(avg_scores, annot=True, cmap='coolwarm', fmt='.1f')
plt.title('Average Scores by Race and Gender')
plt.show()
plt.savefig('figures/HeatAvgScoresRaceGender.png')
