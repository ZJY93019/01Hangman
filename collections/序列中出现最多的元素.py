nums = [74,7,859,4,6,74,846,54,92,67,34,9,8,7,52,3,8,97,4,8,95,4,7,8,93,453,489,238,4,85,478,56,967,74,63,64,78]
from collections import Counter
word_counts = Counter(nums)
top_3 = word_counts.most_common(3)
print(top_3)
#[(4, 4), (8, 4), (74, 3)]
