
def largest_element(lst):
    biggest = lst[0] 
    for num in lst:
        if num > biggest:
            biggest = num  
    return biggest
print(largest_element([1, 5, 3, 9, 2]))  
print("="*45)
def reverse_list(lst):
    return lst[::-1]  
print(reverse_list([1, 2, 3, 4]))  
print("="*45)

def element_in_list(lst, element):
    for item in lst:
        if item == element:
            return True  
    return False 
print(element_in_list([1, 2, 3, 4], 3)) 

print("="*45)
def odd_position_elements(lst):
    return [lst[i] for i in range(0, len(lst), 2)]
print(odd_position_elements([1, 2, 3, 4, 5]))  
print("="*45)
def even_position_elements(lst):
    return [lst[i] for i in range(1, len(lst), 2)]
print(even_position_elements([1, 2, 3, 4, 5])) 

print("="*45)
def running_total(lst):
    total = 0
    result = []
    for num in lst:
        total += num
        result.append(total)
    return result
print(running_total([1, 2, 3, 4]))  

print("="*45)
def is_palindrome(s):
    return s == s[::-1]  
print(is_palindrome("racecar")) 

print("="*45)
def sum_for_loop(lst):
    total = 0
    for num in lst:
        total += num
    return total
print(sum_for_loop([1, 2, 3]))

print("="*45)
def sum_while_loop(lst):
    total = 0
    i = 0
    while i < len(lst):
        total += lst[i]
        i += 1
    return total
print(sum_while_loop([1, 2, 3])) 

print("="*45)
def concatenate_lists(lst1, lst2):
    return lst1 + lst2  
print(concatenate_lists(['a', 'b', 'c'], [1, 2, 3]))

print("="*45)
def alternate_merge(lst1, lst2):
    result = []
    length = min(len(lst1), len(lst2))  
    for i in range(length):
        result.append(lst1[i])
        result.append(lst2[i])
    result.extend(lst1[length:] + lst2[length:])  
    return result
print(alternate_merge(['a', 'b', 'c'], [1, 2, 3])) 

print("="*45)
def digits_of_number(n):
    return [int(digit) for digit in str(n)]
print(digits_of_number(2342))  

