# Read an integer that denotes the length of the list which is returned as the output of the algorithm
length_of_circular_linked_list = int(input())
# Read space-separated integers that denote the elements of the listT which is returned as the output of the algorithm
circular_linked_list = list(map(int,input().strip().split(" ")))

# Write your code here
actual_list = []
index = 0
while len(actual_list) < length_of_circular_linked_list and index < len(circular_linked_list):
    element = circular_linked_list[index]
    if element not in actual_list:
        actual_list.append(element)
    index += 1

print(" ".join(str(num) for num in actual_list))
