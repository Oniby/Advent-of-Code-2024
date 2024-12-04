import re
import utils

file_str = utils.read_full_input(1,'A')

pattern = re.compile(r'(\d+)\s+(\d+)\s?')
m = re.findall(pattern, file_str)

listA = sorted([int(a) for (a,b) in m])
listB = sorted([int(b) for (a,b) in m])
distance = 0
for i in range(len(listA)):
    distance += (abs(listA[i] - listB[i]))

print(f"Distance = {distance}")

count_dict = {}
similarity = 0
for elem in listA:
    if elem in count_dict.keys():
        similarity += elem*count_dict[elem]
    else:
        count = 0
        for elemB in listB:
            if elemB == elem:
                count+=1
        count_dict.update({elem:count})
        similarity += elem * count_dict[elem]

print(f"Similarity = {similarity}")