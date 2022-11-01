def Average(lst):
    sum_of_list = 0
    for i in range(len(lst)):
        sum_of_list += lst[i]
    average = sum_of_list/len(lst)
    return average

list = [15, 9, 55, 41, 35, 20, 62, 49]
average = Average(list)

for i in range(list):
  list[i] -= average
  print(list)
