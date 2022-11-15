# ---------------------------------Meta characters-----------------------------
# [] A set of characters
# . Any character (except newline character)
# ^ Starts with
# $ Ends with
# * Zero or more occurrences        # any of the characters in string
# + One or more occurrences         # Exact word to search
# {} Exactly the specified number of occurrences
# | Either or
# () Capture and group      # if used with {} Then only the specified amount of times it is repeated can be found

# -------------------------------Special Sequences-------------------------------
#               Primary ones to know:
# \A Returns a match if the specified characters are at the beginning of the string
# \b Returns a match where the specified characters are at the beginning or at the end of a word r” ain\b.”
# \B Returns a match where the specified characters are present, but NOT at the beginning (or at the end) of a word

#               Secondary ones:
# \d Returns a match where the string contains digits (numbers from 0-9)
# \D Returns a match where the string DOES NOT contain digits
# \s Returns a match where the string contains a white space character
# \S Returns a match where the string DOES NOT contain a white space character
# \W Returns a match where the string DOES NOT contain any word characters
# \Z Returns a match if the specified characters are at the end of the string


import re   # re means regular expressions

my_string = '''Tata Limited
Dr. David Landsman, executive director
18, Grosvenor Place
London SW1X 7HSc
Phone: +44 (20) 7235 8281
Fax: +44 (20) 7235 8727
Email: tata@tata.co.uk
Website: www.europe.tata.com
Directions: View map

Tata Sons, North America
1700 North Moore St, Suite 1520
Arlington, VA 22209-1911
USA
Phone: +1 (703) 243 9787
Fax: +1 (703) 243 9791
66-66
455-4545
Email: northamerica@tata.com 
Website: www.northamerica.tata.com and
Irfan is the best programmer to ever live on this planet aiaiaiiiai
Irfans Phone = +971-05595-77017'''

Things_to_search = [r'\bPhone', r'planet\b', r'.SA', r'^Tata', r'planet$', r'is{1}', r'one+',
                    r'.com|Email', r'(ai){1}', r'(ai){2}', r'.ai', r'27\b', r'\d{5}-\d{4}',
                    r'\d{3}-\d{5}-\d{5}']


# searching = re.compile(r'\bPhone')         # r means raw string where /n or /t e.t.c are ignored
# matches = searching.finditer(my_string)      # first is what to search and in brackets where to search
# for items in matches:
#     print(items)

for items in Things_to_search:

    search_item = re.compile(items)
    match = search_item.finditer(my_string)

    for result in match:
        print(f'{items} =  {result}')











