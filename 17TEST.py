

## split

#++++| split(separator, maxsplit) |++++#

#*** 1- separator => Optional. Specifies the separator to use when splitting the string.
#              By default any whitespace is a separator

#*** 2- maxsplit =>	Optional. Specifies how many splits to do.
#               Default value is -1, which is "all occurrences"




# Exam 1:

# txt = "welcometothejungle"

# x = txt.split("t")


# print(type(txt))
# print(x)
# print(type(x))






# Exam 2:

# txt = "hello, my name is Peter, I am 26 years old"

# x = txt.split(", ")

# print(x)





# Exam 3:

# txt = "apple#banana#cherry#orange"

# x = txt.split("#")

# print(x)





# Ques:

# 1

# txt = '1,,2'

# splitedtxt = txt.split(",,")

# print(splitedtxt)





# 2

# txt = ' 1  2   3  '

# splitedtxt = txt.split("   ")

# print(splitedtxt)





# Exam 4:

# txt = "apple#banana#cherry#orange"

# # setting the maxsplit parameter to 1, will return a list with 2 elements!
# x = txt.split("#", 2)

# print(x)




# Exam 5:

# books_data = "Python Basics, 250, Data Science Essentials, 300, Machine Learning, 400"

# first_parts = books_data.split(', ', 2)
# print(first_parts)








# text = "Hello World!\nWelcome to Python.\nEnjoy coding!"

# print(text)

# lines_with_ends = text.split("\n")

# print(lines_with_ends)









# splitlines(keepends=True)
#   keepends => Optinal, Used For Show Users This Word is line




# text = "Hello World!\nWelcome to Python.\nEnjoy coding!"

# print(text)

# lines_with_ends = text.splitlines(keepends=True)

# print(lines_with_ends)







txt = """Hi
Ahmed
How 
Are 
You ?"""


print(txt)

spLi = txt.splitlines()

print(spLi)
