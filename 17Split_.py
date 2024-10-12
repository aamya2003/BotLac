

# # split

# ++++| split(separator, maxsplit) |++++#

# *** 1- separator => Optional. Specifies the separator to use when splitting the string.
#              By default any whitespace is a separator

# *** 2- maxsplit =>	Optional. Specifies how many splits to do.
#               Default value is -1, which is "all occurrences"


#  -----         
# str.split(sep=None, maxsplit=-1)
#  -----     


# Example 1: Splitting a Simple Text

# text = "I love programming in Python"

# words = text.split(" ")
# print(words)


# Example 2: Using a Custom Delimiter

# data = "name,age;city"
# fields = data.split(";")
# print(fields)

# String_name = fields[0].split(",")
# n1 = String_name[0]

# print(n1)




# Example with maxsplit

# text = "I love programming in Python and Java"
# limited_split = text.split(" ", 2)
# print(limited_split)