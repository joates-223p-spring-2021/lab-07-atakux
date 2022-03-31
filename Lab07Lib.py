# -*- coding: utf-8 -*-
"""
Angela DeLeo
CPSC 223P-01
Wed Mar 23, 2022
atakux707@csu.fullerton.edu
"""

# Constant definition
ASCII_LOWERCASE = "abcdefghijklmnopqrstuvwxyz"
ASCII_UPPERCASE = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
DECIMAL_DIGITS = "0123456789"

# Function definitions below this line



def is_alpha(str) -> bool:
	#some letter has been found

	#parse thru the given parametre
	for letter in str:
		#if the letter is Not in the ascii letter constants, its false
		if letter not in ASCII_LOWERCASE and letter not in ASCII_UPPERCASE:
			return False
	#otherwise, its true
	return True




def is_digit(num) -> bool:
	#some digit has been found
	
	#parse thru the given parametre
	for digit in num:
		#if the digit is Not in the decimal_digits constant, its false
		if digit not in DECIMAL_DIGITS:
			return False
	#otherwise, its true
	return True




def to_lower(str) -> str:
	#converts a given string to lowercase
	lowerCased = ""
	stringLength = len(str)

	for x in range(stringLength):
		if str[x] in ASCII_UPPERCASE:
			#the index where the uppercase is located is set equal 
			#to the index in which the lowercase constant should access
			#to get the lowercase version of the uppercase letter

			lowerCaseIndex = ASCII_UPPERCASE.index(str[x])
			lowerCased += ASCII_LOWERCASE[lowerCaseIndex]
		else:
			lowerCased += str[x]
	return lowerCased




def to_upper(str) -> str:
	#converts a given string to uppercase
	upperCased = ""
	stringLength = len(str)

	for x in range(stringLength):
		if str[x] in ASCII_LOWERCASE:
			#the index where the lowercase is located is set equal 
			#to the index in which the uppercase constant should access
			#to get the uppercase version of the lowercase letter
			
			upperCaseIndex = ASCII_LOWERCASE.index(str[x])
			upperCased += ASCII_UPPERCASE[upperCaseIndex]
		else:
			upperCased += str[x]
	return upperCased




def find_chr(givenStr, findChar) -> int:
	#locates a char and returns index number
	#create list to split the given string into a list of chars
	splitUp = []
	splitUp[:] = givenStr

	#if the length is greater than one we can look for the char
	if len(findChar) != 1:
		return -1
	else:
		#parse thru the split up given string
		for char in splitUp:
			#if a char in the list matches the char we search for
			#then we print the index of that char
			if char == findChar:
				return splitUp.index(char)
	return -1




def find_str(givenStr, findStr) -> int:
	#locates a string and returns index number
	givenLength = len(givenStr)
	findLength = len(findStr)

	#parse thru the given string and look for the string we want to find
	for index in range(givenLength - findLength + 1):
		#if the slice we are parsing thru is the string we want to find return the index
		if givenStr[index : (index + findLength)] == findStr:
			return index
	#once done parsing return -1
	return -1




def replace_chr(givenChar, replaceThis, replacement) -> str:
	#replaces a given character with something else
	notDone = True
	result = givenChar #initialize result to the given char

	charIndex = find_chr(result, replaceThis)
	
	while notDone:
		#if the index is returned as -1, then we are done and 
		#return the result char
		if charIndex == -1:
			return result
		#otherwise, we keep looping and replacing
		else:
			#result = start until index then replace it then keep going until the end
			result = result[ : charIndex] + replacement + result[charIndex + len(replaceThis) : ]
		#then we do it again
		charIndex = find_chr(result, replaceThis)




def replace_str(givenStr, replaceThis, replacement) -> str:
	#replaces a given string with something else
	#replaces a given character with something else
	notDone = True
	result = givenStr #initialize result to the given char

	strIndex = find_str(result, replaceThis)
	
	while notDone:
		#if the index is returned as -1, then we are done and 
		#return the result char
		if strIndex == -1:
			return result
		#otherwise, we keep looping and replacing
		else:
			#result = start until index then replace it then keep going until the end
			result = result[ : strIndex] + replacement + result[strIndex + len(replaceThis) : ]
		#then we do it again
		strIndex = find_str(result, replaceThis)
