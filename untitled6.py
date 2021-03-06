# -*- coding: utf-8 -*-
"""Untitled6.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/17pHUBMP_3iZvvndWXcNv8phIFCruCjcP

***Creating a word acronym Generator ***
before we started we will need a pharse for the for the user so that it will be easy to enter the word choice of there own and we can do this by declaring a variable that can take in input data
"""

user_input = input("Enter a Phrase:")

"""We have stored the user input in a user_input variable.

Now we must ignore words like 'of' from the user input as most of the time, 'of' is not considered for acronyms.

Also, we need to separate each word and store it individually in a form of a list so that we can easily iterate through it.
"""

phrase = (user_input.replace('of',"")).split()

"""Here in user_input.replace('of', '') we are using .replace() function to ignore 'of' from the input, if any.

And then we are using .split() function to break down the string into individual words and store them as a list in phrase variable.

We need an empty string variable to store our acronym. Let's quickly create one. ..
"""

acronyms = ""

"""Now let's create a for loop which will iterate through phrase variable."""

for word in phrase:
    acronyms = acronyms + word[0].upper()

"""Here in acronym = acronym + word[0], we are slicing off the first letter of words stored in phrase using slicing operator and adding it to our acronym variable.

We are also using .upper() function to capitalize the acronyms.

Finally, just add a print statement which will print out the acronym on the console.
"""

print(f'Acronyms of {user_input} is {acronyms}')

"""Awesome now let's try running our code with different inputs"""

user_input = input("Enter a Phrase:")
phrase = (user_input.replace('of',"")).split()
acronyms = ""
for word in phrase:
    acronyms = acronyms + word[0].upper()
print(f'Acronym of {user_input} is {acronyms}')