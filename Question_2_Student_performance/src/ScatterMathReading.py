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

# Create a scatter plot of math score versus reading score
plt.scatter(data['math score'], data['reading score'])
plt.title('Math Score vs Reading Score')
plt.xlabel('Math Score')
plt.ylabel('Reading Score')
plt.show()
plt.savefig('figures/ScatterMathReading.png')

