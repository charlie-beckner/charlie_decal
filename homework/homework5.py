# PART 1
# 1.1 pwd

# 1.2 ls

# 1.3 
#   cd ..
#   cd brianna_repo
#   git pull origin main/master

# 1.4 
#   cp homework.py ../python_decal/judy_decal/homework

# 1.5 
#   cat homework.py

# 1.6 
#   nano homework.py

# 1.7
#   git add
#   git commit -m "Adding homework message"
#   git push origin main/master

# 1.8
#   The homework.py file in brianna.repo has changes on it that were not pulled from the remote repository onto Judy's local repository so there is a mismatch between the local and remote that has to be fixed first. Judy should pull homework.py from brianna.repo to make sure all the changes are up to date and then edit the file so that she can push it to her own repository. 

# 1.9 
#   ~/Recent

# PART 2
# 2.1 
def checkDataType(data):
    return type(data)

# 2.2
def evenOrOdd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"
    
# PART 3
def sumWithLoops(list):
    sum = 0 
    for i in list:
        sum = sum + i
    return sum
    
# PART 4
# 4.1
def duplicateList(list):
    newList = []
    for i in list:
        newList = newList + [i] + [i]
    return newList

duplicateList(['a', 'b', 'c'])

# 4.2
# Needs a colon : after the defintion statement 
def square(num):
    return num * num
