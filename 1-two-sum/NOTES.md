O(n): The value we are looking for is the difference between the target and element
for index, element in enumerate(arrayName):
check if the difference[ target- value] is present in the array
if target-value in hashmap:
return indices of the two numbers:
return [ hashmap[target-value] , index ]
in the hashmap, we are gonna map the key = value to the index
hashmap = {}
hashmap[value] = index