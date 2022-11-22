# Problem Statement:-
# You are given few sentences as a list (Python list of sentences).
# Take a query string as an input from the user.
# You have to pull out the sentences matching this query inputted by the user in decreasing order of relevance after
# converting every word in the query and the sentence to lowercase.
# The most relevant sentence is the one with the maximum number of matching words with the query.
#
# Given:
# Sentences = [“Python is cool”, “python is good”, “python is not python snake”]
#
# Input:
# Please input your query string
# “Python is”
#
# Output:
# 3 results found:
#
# python is not python snake
# python is good
# Python is cool

'''
author = Mohammed Irfan
date = 22 September 2022
purpose = Practice
'''


def query(searchlist):
    search = input('Search:\t').lower()
    found = []
    result = 0

    for items in searchlist:
        items = items.lower()
        count = items.count(search)     # Checks amount of times the word matched to sort by most relevant one
        if search in items:
            found.append([items, count])        # adds sentence to found
            result += 1     # How many results are found

    # checks for the 2 variable of every list and reverses them to descending
    found.sort(key= lambda count: count[1], reverse=True)
    print(f'{result} results are found regarding - {search}')
    return found

if __name__ == '__main__':
    sentence_list = ["Python is cool", "python is good", "python is not python snake", 'python plus python == python', 'list']
    for item in query(sentence_list):
        print(item[0])

# Another solution = https://youtu.be/VkH1B0EAhfU
# Logic used there = Will match word by word
# logic used here  = Will match letter by letter
# Both logics depends on use cases







