#############################
## -- PROBLEM 1 Solution-- ##
#############################


# arrayCheck([1, 1, 2, 3, 1]) → True
# arrayCheck([1, 1, 2, 4, 1]) → False
# arrayCheck([1, 1, 2, 1, 2, 3]) → True

def arrayCheck(nums):
    for i in range(len(nums)-2):
        if nums[i] == 1 and nums[i+1] == 2 and nums[i+2] == 3:
            return True
        return False


print(arrayCheck([1, 1, 2, 3, 1]))
print(arrayCheck([1, 1, 2, 3, 1]))
print(arrayCheck([1, 1, 2, 1, 2, 3]))


#############################
## -- PROBLEM 2 Solution-- ##
#############################


def stringBits(str):
    end = len(str)
    SlicedString = str[0:end:2]
    return SlicedString


print(stringBits('Hello'))
print(stringBits('Hi'))
print(stringBits('Heeololeo'))


#############################
## -- PROBLEM 3 Solution-- ##
#############################

def end_other(a, b):
    a = a.lower()
    b = b.lower()
    if a.endswith(b) or b.endswith(a):
        return True
    return False


print(end_other('abc', 'abXabc'))
print(end_other('AbC', 'HiaBc'))
print(end_other('Hiabc', 'abc'))
print(end_other('Hiabcd', 'abc'))


#############################
## -- PROBLEM 4 Solution-- ##
#############################

def doubleChar(str):
    str1 = ''
    end = len(str)
    for i in range(0, end):
        str1 = str1+str[i]*2
    print(str1)


doubleChar('The')
doubleChar('AAbb')
doubleChar('Hi-There')


#############################
## -- PROBLEM 5 Solution-- ##
#############################


def no_teen_sum(a, b, c):
    sum = fix_teen(a)+fix_teen(b)+fix_teen(c)
    print(sum)


def fix_teen(n):

    if (13 <= n < 19):
        if (n != 15 and n != 16):
            return 0
    return n


no_teen_sum(1, 2, 3)
no_teen_sum(2, 13, 1)
no_teen_sum(2, 1, 14)


#############################
## -- PROBLEM 6 Solution-- ##
#############################


def count_evens(nums):
    count = 0
    for i in nums:
        if i % 2 == 0:
            count = count+1
    return count


count_evens([2, 1, 2, 3, 4])
count_evens([2, 2, 0])
count_evens([1, 3, 5])

print(count_evens([2, 1, 2, 3, 4]))
print(count_evens([2, 2, 0]))
print(count_evens([1, 3, 5]))
