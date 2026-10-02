## 1. Write a program to print the frequency of each element in a list.
# Elements_number = int(input("Enter the number of elements:"))
# Elements = []
# for i in range(Elements_number):
#     value = input("Enter the elements:")
#     Elements.append(value)
# print(Elements)
# for i in range(Elements_number):
#     count = 0
#     for j in range(Elements_number):
#         if Elements[i]==Elements[j]:
#             count+=1
#     already_counted = False
#     for k in range(i):
#         if Elements[i] == Elements[k]:
#             already_counted = True
#             break
#     if not already_counted:
#         if count == 1:
#             print(Elements[i],"occurs",count,"times")
#         else:
#             print(Elements[i],"occurs",count,"times")
        

## 2. Write a program to separate the even and odd elements of a list into two separate lists.
# Elements_number = int(input("Enter the number of elements:"))
# Elements = []
# for i in range(Elements_number):
#     value = int(input("Enter the elements:"))
#     Elements.append(value)
# print(Elements)
# Even = []
# Odd = []

# for i in range(Elements_number):
#     if Elements[i]%2==0:
#         Even.append(Elements[i])
#     else:
#         Odd.append(Elements[i])
# print(f"Even elements:{Even}")
# print(f"Odd elements:{Odd}")


## 3. Write a program to print all the unique elements in a list.
# Elements_number = int(input("Enter the number of elements:"))
# Elements = []
# for i in range(Elements_number):
#     value = int(input("Enter the elements:"))
#     Elements.append(value)
# print(Elements)
# for i in range(Elements_number):
#     count = 0
#     for j in range(Elements_number):
#         if Elements[i]==Elements[j]:
#             count+=1
#     if count == 1:
#         print(Elements[i])


## 4. Write a program to count the total number of duplicate elements in a list.
# Elements_number = int(input("Enter the elements number:"))
# Elements = []
# for i in range(Elements_number):
#     value = int(input("Enter the elements:"))
#     Elements.append(value)
# print(Elements)
# duplicate_count = 0
# for i in range(Elements_number):
#     count = 0
#     for j in range(Elements_number):
#         if Elements[i] == Elements[j]:
#             count += 1
#     if count > 1:
#         already_counted = False
#         for k in range(i):
#             if Elements[i] == Elements[k]:
#                 already_counted = True
#                 break
#         if not already_counted:
#             duplicate_count += 1
# print("Total duplicate elements:", duplicate_count)


## 5. Write a program to count and print the total number of positive and negative elements in a list.
# Elements_number = int(input("Enter the elements number:"))
# Elements = []
# for i in range(Elements_number):
#     value = int(input("Enter the elements:"))
#     Elements.append(value)
# print(Elements)
# Positive_elements = []
# Negative_elements = []
# Positive_count = 0
# Negative_count = 0
# for i in range(Elements_number):
#     if Elements[i]>0:
#         Positive_count += 1
#         Positive_elements.append(Elements[i])
#     else:
#         Negative_count += 1
#         Negative_elements.append(Elements[i])
# print(f"Total positive elements:{Positive_count}")
# print(f"Positive elements:")
# for k in range(Positive_count):
#     print(Positive_elements[k],end=" ")
# print()
# print(f"Total Negative elements:{Negative_count}")
# print(f"Negative elements:")
# for j in range(Negative_count):
#     print(Negative_elements[j],end=" ")


## 1. Write a program to find the length of a string.
# name = input("Enter your name:")
# count = 0
# for chr in name:
#     count+=1
# print(count)


## 2. Write a program to copy one string to another string.
# name  = input("Enter your name:")
# name_copy=name
# print(name,name_copy)


## 3. Write a program to concatenate two strings.
# str1 = input("Enter a string:")
# str2 = input("Enter a string:")
# str = str1 +" "+ str2
# print(str)


## 4. Write a program to compare two strings.
# str1 = input("Enter a string:")
# str2 = input("Enter a string:")
# if str1==str2:
#     print("strings are equal")
# else:
#     print("strings are not equal")


## 5. Write a program to convert lowercase string to uppercase.
# str1 = input("Enter a string:")
# result = ""
# for ch in str1:
#     if "a"<= ch <="z":
#         result += chr(ord(ch)-32)
#     else:
#         result+=ch
# print(result)


## 6. Write a program to convert uppercase string to lowercase.
# str1 = input("Enter a string:")
# result = ""
# for ch in str1:
#     if "A"<= ch <="Z":
#         result += chr(ord(ch)+32)
#     else:
#         result+=ch
# print(result)


## 7. Write a program to find the total number of alphabets, digits, or special characters in a string.
# text = input("Enter a string: ")
# letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
# digits = "0123456789"
# alphabets = 0
# numbers = 0
# special = 0
# for ch in text:
#     found = False
#     for letter in letters:
#         if ch == letter:
#             alphabets += 1
#             found = True
#             break
#     for digit in digits:
#         if ch == digit:
#             numbers += 1
#             found = True
#             break
#     if found == False and ch != " ":
#         special += 1
# print("Alphabets:", alphabets)
# print("Digits:", numbers)
# print("Special characters:", special)


## 8. Write a program to count the total number of vowels and consonants in a string.
# text = input("Enter a string:")
# vowels = "aeiouAEIOU"
# letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
# c=0
# v=0
# for ch in text:
#     for letter in letters:
#         if ch==letter:
#             if ch in vowels:
#                 v+=1
#             else:
#                 c+=1
# print(v,c)

## 9. Write a program to count the total number of words in a string.
# text = input("Enter a string: ")
# count = 1
# for ch in text:
#     if ch == " ":
#         count+=1
# print(count)

# 1. Write a recursive program to count the number of digits in a given positive integer.
# def digit_count(n):
#     if n<10:
#         return 1
#     else:
#         return 1 + digit_count(n//10)
# num = int(input("Enter digit:"))
# print(digit_count(num))


## 2. Write a recursive program to count the number of even digits in a given integer.
# def count_the_even(n):
#     if n == 0:
#         return 0
#     digit = n%10
#     if digit%2 == 0:
#         return 1+count_the_even(n//10)
#     else:
#         return count_the_even(n//10)
# num = int(input("Enter digit:"))
# print(count_the_even(num))


## 3. Write a recursive program to return the nth Fibonacci number (0-indexed).
# def fibonachi(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fibonachi(n-1) + fibonachi(n-2)

# num = int(input("Enter n:"))
# for i in range(num):
#     print(fibonachi(i),end=" ")
    
  
## 4. Write a recursive program to compute the GCD of two positive integers using the subtraction-based Euclidean algorithm.
# def gcd(a,b):
#     if a==b:
#         return a
#     elif a>b:
#         return gcd(a-b,b)
#     else:
#         return gcd(a,b-a)  
# a = int(input("Enter first positive integer: "))
# b = int(input("Enter second positive integer: "))
# print("GCD:", gcd(a, b))


## 6. Write a recursive program to compute the sum of the series: x + x^2 + x^3 + ... + x^n for given x and n. Take user input for x and n.
# def series_sum(x, n):
#     if n == 1:
#         return x
#     else:
#         return x ** n + series_sum(x, n - 1)
# x = int(input("Enter x: "))
# n = int(input("Enter n: "))

# print("Sum:", series_sum(x, n))