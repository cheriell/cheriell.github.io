import pandas as pd
from collections import Counter
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style("darkgrid")
import numpy as np

def get_composer_count(metadata_file):
    metadata = pd.read_csv(metadata_file)
    composer_count = Counter(metadata["composer"])
    return composer_count

composer_count_D = get_composer_count("distinct_pieces.csv")
composer_count_R = get_composer_count("metadata_R.csv")
composer_count_S = get_composer_count("metadata_S.csv")
composer_count_A = dict([(composer, composer_count_R[composer] + composer_count_S[composer]) for composer in composer_count_D.keys()])

# sort composers order
composer_count_list = [(composer, count) for composer, count in composer_count_A.items()]
composer_count_list.sort(key=lambda x: x[1])
composer_list = [composer for composer, count in composer_count_list]

# get counts by composer order
count_D = [composer_count_D[composer] for composer in composer_list]
count_R = [composer_count_R[composer] for composer in composer_list]
count_S = [composer_count_S[composer] for composer in composer_list]
count_A = [composer_count_A[composer] for composer in composer_list]

# create bar plot
fig, ax = plt.subplots(figsize=(10,30))    
width = 0.18 # the width of the bars 
ind = np.arange(len(composer_list))  # the x locations for the groups
bar_D = ax.barh(ind, count_D, width, color='blue')
bar_R = ax.barh(ind-width, count_R, width, color='purple')
bar_S = ax.barh(ind-width*2, count_S, width, color='red')
bar_A = ax.barh(ind-width*3, count_A, width, color='orange')
for i in range(len(composer_list)):
    ax.text(count_D[i]+0.5, i-0.1, str(count_D[i]), color='black')#, fontweight='bold')
    ax.text(count_R[i]+0.5, i-0.1-width, str(count_R[i]), color='black')#, fontweight='bold')
    ax.text(count_S[i]+0.5, i-0.1-width*2, str(count_S[i]), color='black')#, fontweight='bold')
    ax.text(count_A[i]+0.5, i-0.1-width*3, str(count_A[i]), color='black')#, fontweight='bold')
ax.set_yticks(ind-width*2)
ax.set_yticklabels(composer_list, minor=False)
ax.legend((bar_D[0], bar_R[0], bar_S[0], bar_A[0]), ("Distinct Pieces", "Real Recording Subset", "Synthetic Subset", "All"))

plt.title('Music pieces by composer')
plt.xlabel('number of pieces')
plt.savefig('composer_distribution.png')