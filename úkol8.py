"""Task 1
There are four lists of integers. Combine them in the
fifth list. Sort the result in ascending or descending order based on the user’s choice. Find a value entered by the user using a linear search."""
list1 = [1, 2, 3]
list2 = [3, 4, 3]
list3 = [2, 6, 8]
list4 = [4, 5, 8]

list5 = list1+list2+list3+list4

user_choice = input("Pro zatřídění vzestupně zadej A, pro zatřídění sestupně zadej B: ")

if user_choice == "A":
  print(sorted(list5))
elif user_choice == "B":
  print(sorted(list5, reverse=True))
else:
  print("Zadána špatná hodnota.")

key = int(input("Zadej hledané číslo: "))
if key in list5:
  print(key)
else:
  print("Není v seznamu.")

#Task 2
#There are four lists of integers. Combine only the elements unique to each list in the fifth list. Sort the result in ascending or descending order based on the user’s choice. Find a value entered by the user using a binary search.

list1 = [1, 2, 3]
list2 = [3, 4, 3]
list3 = [2, 6, 8]
list4 = [4, 5, 8]

list5 = list1+list2+list3+list4

unique_list = list(set(list5))

user_choice = input("Pro zatřídění vzestupně zadej A, pro zatřídění sestupně zadej B: ")

if user_choice == "A":
  print(sorted(unique_list))
elif user_choice == "B":
  print(sorted(unique_list, reverse=True))
else:
  print("Zadána špatná hodnota.")

"""key = int(input("Zadej hledané číslo: "))
if key in unique_list:
  print(key)
else:
  print("Není v seznamu.")"""

key = int(input("Zadej hledané číslo: "))

def binary_search(unique_list, key):
  L = 0
  R = len(unique_list) - 1
  m = 0
  while(L<=R):
    m = (L+R)//2
    if unique_list[m] < key:
      L = m + 1
    elif unique_list[m] > key:
      R = m - 1
    else:
      return m

  return -1

result = binary_search(unique_list, key)
if result != -1:
  print("Číslo nalezeno")
else:
  print("Číslo nenalezeno")