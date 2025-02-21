# QUESTION 1
def computePower(x, y):
    base = 1
    for i in range(y):
        base = base * x
    return base
x = 2
y = 3
(computePower(x, y))

# QUESTION 2
def temperatureRange(temps):
    temps_range = tuple([max(temps), min(temps)])
    return temps_range

readings = [15, 14, 17, 20, 23, 28, 20]
(temperatureRange(readings))

# QUESTION 3
def isWeekend(day_num):
    if day_num <= 5: 
        weekend = False
    else: 
        weekend = True
    return weekend

day = 6
isWeekend(day)

# QUESTION 4
def fuel_efficiency(distance, fuel):
    return round(distance/fuel, 2)

distance = 70
fuel = 21.5
fuel_efficiency(distance, fuel)

# QUESTION 5
n = 12345
def decodeNumbers(n):
    last_digit = n % 10 
    number = n // 10 
    final_number = str(last_digit) + str(number)
    return final_number

decodeNumbers(n)

# QUESTION 6

# 6.1
nums = [2024, 98, 131, 2, 3, 72]
def find_min_with_for_loops(nums):
    minimum = nums[0]
    for i in nums: 
        if i < minimum:
            minimum = i
    return minimum

def find_max_with_for_loops(nums):
    maximum = nums[0]
    for i in nums: 
        if i > maximum:
            maximum = i
    return maximum

find_min_with_for_loops(nums)
find_max_with_for_loops(nums)

# 6.2 
def find_min_with_while_loop(nums):
    i = 0
    minimum = nums[0]
    while i < len(nums):
        if nums[i] < minimum:
            minimum = nums[i]
        i += 1
    return minimum 

def find_max_with_while_loop(nums):
    i = 0
    minimum = nums[0]
    while i < len(nums):
        if nums[i] > minimum:
            minimum = nums[i]
        i += 1
    return minimum 

find_min_with_while_loop(nums)
find_max_with_while_loop(nums)


# QUESTION 7
def vowel_and_consonant_count(text):
    vowel_count = 0
    consonant_count = 0
    for character in text: 
        if character.isalpha() and (character == "a" or character == "A" or
                                    character == "e" or character == "E" or 
                                    character == "i" or character == "I" or
                                    character == "o" or character == "O" or 
                                    character == "u" or character == "U"):
            vowel_count +=1
        elif character.isalpha(): 
            consonant_count +=1
    return (vowel_count, consonant_count)

text = "UC Berkeley, founded in 1868!"
vowel_and_consonant_count(text)

# QUESTION 8
def digital_root(num):
    sum = 0
    string_num = str(num)
    for i in string_num:
        digit = int(i)
        sum = sum + digit
    return sum

num = 2468
digital_root(num)

