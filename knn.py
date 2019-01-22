import pandas as pd
import numpy
import math
from collections import Counter

point =[6,6]
data = pd.read_csv("k_set.csv")
print(data)

distances= []

def euclidean_distance(x1, y1, x2, y2):
	return(math.sqrt((y2-y1)**2 + (x2-x1)**2))

k = input("Enter no. of neighbours")

print(data.shape)
label = list(data["class"])
for i in range(data.shape[0]):
	distances.append(euclidean_distance(data['x_term'][i], data['y_term'][i], point[0],point[1]))

print(distances)

def sort_list(distances,label):
	n = len(distances)
 
    # Traverse through all array elements
	for i in range(n):
 
# Last i elements are already in place
		for j in range(0, n-i-1):
			if distances[j] > distances[j+1] :
				distances[j], distances[j+1] = distances[j+1], distances[j]
				label[j], label[j+1] = label[j+1], label[j]

sort_list(distances,label)


print(distances,label)

label_knn = label[0:k]

x= Counter(label_knn).most_common(1)
print("Predicted class =",x[0][0])


