import pandas as pd
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

# Calculate the number of students in each gender and score group
math_counts = data.groupby(['gender', pd.cut(data['math score'], bins=[0, 40, 60, 80, 100])]).size().unstack()
reading_counts = data.groupby(['gender', pd.cut(data['reading score'], bins=[0, 40, 60, 80, 100])]).size().unstack()
writing_counts = data.groupby(['gender', pd.cut(data['writing score'], bins=[0, 40, 60, 80, 100])]).size().unstack()

# Create a stacked bar chart of scores by gender
fig, axs = plt.subplots(3, 1, figsize=(8, 12))
math_counts.plot(kind='bar', stacked=True, ax=axs[0])
reading_counts.plot(kind='bar', stacked=True, ax=axs[1])
writing_counts.plot(kind='bar', stacked=True, ax=axs[2])
plt.tight_layout()
plt.show()
plt.savefig('figures/StackedScoresRangeGender.png')
