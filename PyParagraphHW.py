import re

with open ('/Users/hanna/Downloads/paragraph_2.txt') as f: 
    data = f.read()
    
data 
data.replace("\n", " ")
sents = re.split("\.|\?|!", data) 
sents = [x.strip() for x in sents if len(x) > 2]
for s in sents:
    print(s)
    print()
    
words = list(data.split(" "))
sent_length = [len(sents.replace(' ','')) for sents in data]
words_sents = [sents.split(' ') for sents in data]

print("Paragraph Analysis")

print("Approximate Word Count: {}".format(len(words)))
print("Approximate Sentence Count: {}".format(len(sents)))
print("Average Letter Count: {}".format(len(data)/float(len(words))))
print ("Average sentence length: {}". format(len(words)/float(len(sents))))