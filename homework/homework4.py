# 2.1
one_through_twenty = list(range(0,21))
print(one_through_twenty)

# 2.2
def square_list(list):
    list_squared = []
    for i in list:
        list_squared.append(i**2)
    return list_squared

one_through_twenty_squared = square_list(one_through_twenty)
one_through_twenty_squared

# 2.3 
def first_fifteen_elements(list):
    return list[:15:1]

first_fifteen_elements(one_through_twenty_squared)

# 2.4 
def every_fifth_element(list):
    return list[4::5]
every_fifth_element(one_through_twenty_squared)

# 2.5 
def fancy_function(list):
    return list[::-3]
fancy_function(one_through_twenty_squared)

# 3.1 
def create_2D_list():
    new_matrix = []
    num = 1
    for i in range(5):
        row = []
        for j in range(5):
            row.append(num)
            num += 1
        new_matrix.append(row)
    return new_matrix
matrix = create_2D_list()
matrix
# While I didn't run into an error with this one, I had a lot of trouble figuring out how to make it work properly. At first I made the range in the second for loop 25 but that made every list within the larger list go to 25 so i had five lists of 0-24. I then fixed it to only make j iterate through a list of length 5 but each list was still 0-4 so I added a num counter to start at 1 and not zero and then increase with each iteration so that I could append the num counter to the matrix rather than a value directly from the range the loops were iterating through. 

# 3.2 
def modified_2D_list(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] % 3 == 0:
                matrix[i][j] = "?"
    return matrix
modified_2D_list(matrix)
# I kept getting an error that said "list" object cannot be interpreted as an integer whenever I tried to call the function. I fixed this by making the for loops iterate through the length of the matrix rather than just the matrix itself. 
# I also had to look up a few things about matrices such as how to acess a particular value from the matrix and not just one of the lists. 

# 3.3 
matrix_modified = modified_2D_list(matrix)
def sum_non_question_marks(matrix):
    sum = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] != "?":
                sum = sum + matrix[i][j]
    return sum

sum_non_question_marks(matrix_modified)


