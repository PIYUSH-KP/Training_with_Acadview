import re

# Q.1- Extract the user id, domain name and suffix from the following email addresses.
# emails = "zuck26@facebook.com" "page33@google.com"
# "jeff42@amazon.com"
# desired_output = [('zuck26', 'facebook', 'com'), ('page33', 'google', 'com'), ('jeff42', 'amazon', 'com')]
print('__'*50,'\nSOLUTION 1\n','__'*50)


emails = "zuck26@facebook.com"" \
""page33@google.com"" \
""jeff42@amazon.com"

a = re.findall(r'(\w+)@([A-Z0-9]+)\.([A-Z]{2,4})', emails, flags=re.I)
print(a)

print('\n\n')
#Q.2- Retrieve all the words starting with ‘b’ or ‘B’ from the following text.
#text = "Betty bought a bit of butter, But the butter was so bitter, So she bought some better butter, To make the bitter butter better."
print('__'*50,'\nSOLUTION 2\n','__'*50)

text = "Betty bought a bit of butter, But the butter was so bitter, So she bought some better butter, To make the bitter butter better."
b = re.findall(r'\bB\w+', text, flags=re.I)
print(b)
print('\n\n')
#Q.3- Split the following irregular sentence into words
#sentence = "A, very very; irregular_sentence"
#desired_output = "A very very irregular sentence"
print('__'*50,'\nSOLUTION 3\n','__'*50)


sentence = "A, very very; irregular_sentence"
c = re.split('[;,\s_]+', sentence)
s = " "
print(s.join(c))



print('\n\n')
#Q.1- Clean up the following tweet so that it contains only the user’s message. That is, remove all URLs, hashtags, mentions, punctuations, RTs and CCs.
#tweet = '''Good advice! RT @TheNextWeb: What I would do differently if I was learning to code today http://t.co/lbwej0pxOd cc: @garybernhardt #rstats'''
#desired_output = 'Good advice What I would do differently if I was learning to code today'
print('__'*50,'\nSOLUTION OPTIONAL\n','__'*50)
"""
in this tweet we have to remove many things
1. RT
2. cc
3. url : http://t.co/lbwej0pxOd
4. # tags
5. mentions: @
6. puntuations
"""

tweet = "Good advice! RT @TheNextWeb: What I would do differently if I was learning to code today http://t.co/lbwej0pxOd cc: @garybernhardt #rstats"
print(tweet)
print('\n\n')

tweet = re.sub('RT|cc', '', tweet)  # remove RT and cc

print(tweet)
print('\n\n')

tweet = re.sub('http\S+\s*', '', tweet)  # remove URL

print(tweet)
print('\n\n')

tweet = re.sub('@\S+', '', tweet)  # remove mentions

print(tweet)
print('\n\n')

tweet = re.sub('#\S+', '', tweet)  # remove hashtags

print(tweet)
print('\n\n')

tweet = re.sub('[%s]' % re.escape("""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""), '', tweet)  # remove punctuations

print(tweet)
print('\n\n')

tweet = re.sub('\s+', ' ', tweet)  # remove extra spaces

print("USER'S MESSAGE:\n"+tweet)
