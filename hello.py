#. Write a Python program to get a single string from two given strings, separated 
#by a space, and swap the first two characters of each string
def swap_string_chars(str1, str2):
    new_str1 = str2[:2] + str1[2:]
    new_str2 = str1[:2] + str2[2:]
    final_str = new_str1 + ' ' + new_str2
    
    return final_str
print(swap_string_chars('Emmily', 'Stephanie'))

#  Write a Python function that takes a list of words and returns the longest word and 
#the length of the longest one
def longest_word(words):
    longest = ""
    length = 0
    for word in words:
        if len(word) > length:
            longest = word
            length = len(word)
    return longest, length
print(longest_word(["Akirachix","students","stephanie","developer"]))


#Write a Python program that accepts a comma-separated sequence of words as input and prints the
#  distinct words in sorted form (alphanumerically).
words = input("hello emmily,emmily how are you: ")

word_list = words.split(",")

my_words = (set(word_list))
print(", ".join(my_words))

#Write a Python function that takes two lists and returns True if they have at least one common member.
list1 = ["emmie",24,2002,"akirachix"]
list2 = ["stephanie",20,2002,"akirachix"]
def has_common_element(list1,list2):
    for item in list1:
        if item in list2:
            return True
    return False
print(has_common_element(list1,list2))

#Write a Python program to convert a list to a list of dictionaries.
#Sample lists: ["Black", "Red", "Maroon", "Yellow"], ["#000000", "#FF0000", "#800000", "#FFFF00"]
list1 = ["Black", "Red", "Maroon", "Yellow"]
list2 = ["#000000", "#FF0000", "#800000", "#FFFF00"]
def convert_list_to_dictionary():
    new_dict = dict(zip(list1, list2))
    print(new_dict)


# Write a Python program to check whether all dictionaries in a list are empty or not
def check_empty_dict(lst):
    for ele in lst:
        if bool(ele):
            return "True"
    return "False"
lst = [{},{"fruits"},{},{1000}]
lst = [{},{},{}]
print(check_empty_dict(lst))


#Given a list of numbers, use list comprehension to remove all odd numbers from the list:
numbers = [3,5,45,97,32,22,10,19,39,43]
odd_numbers = [n for n in numbers if n %2 !=0]
print(odd_numbers)

#Find the common numbers in two lists (without using a tuple or set) 
list_a = [1, 2, 3, 4,] 
list_b = [2, 3, 4, 5]
common_element = []
for element in list_a:
    if element in list_b and element not in common_element:
        common_element.append(element)
print(common_element)

#Use a nested list comprehension to find all of the numbers from 1-1000 that are divisible by any single 
# digit besides 1 (2-9)
numbers = list(range(1,1000))
divisors = list(range(2,10))

result = [n for n in numbers if any ([n%d ==0 for d in divisors])]
print(result)

#. Write a Python function to remove all vowels in a string
def remove_vowels(string):
    vowels = "aeiouAEIOU"
    return  "".join([char for char in string if char not in vowels])
print(remove_vowels("InterNtioNal"))



