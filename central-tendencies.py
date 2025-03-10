import math
import collections
data = [2, 4, 3, 6, 4, 5]
n = len(data)
# Central tendancy Measures 
#Mean
sum = 0
for i in data: 
    sum += i
    mean = sum / n 
print('Mean: ', mean)
#Median
data_sort = sorted(data) 
if n%2 == 0:
    median = (data_sort[(n//2)-1] + data_sort[n//2])/2 
else:
    median = data_sort((n//2)-1) 
print('Median: ',median)
#Mode
mode = collections.Counter(data).most_common(1)[0][0] 
print('Mode: ', mode)
#Dispersion Measures 
#Variance
sum_var = 0 
for i in data:
    sum_var += math.pow(i - mean, 2) 
    var = sum_var / (n-1)
print('Variance: ', round(var,2))
#Standard deviation
std = round(math.sqrt(var),2) 
print('Standard Deviation', std)