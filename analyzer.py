import nltk
from nltk.classify import NaiveBayesClassifier

# nltk.download('punkt')

def format_sentence(sent):
    return({word: True for word in nltk.word_tokenize(sent)})

print("loading data set")
 
pos = []
with open("./sample_dataset/pos.txt") as f:
    for i in f: 
        pos.append([format_sentence(i), 'pos'])
 
neg = []
with open("./sample_dataset/neg.txt") as f:
    for i in f: 
        neg.append([format_sentence(i), 'neg'])
 
# next, split labeled data into the training and test data
training = pos[:int((.8)*len(pos))] + neg[:int((.8)*len(neg))]

print ("commencing trianing")
classifier = NaiveBayesClassifier.train(training)
print ("classifier trained")

def analyze(s):
    res = ""
    x = classifier.labels()
    if len(x)>0:
        res = classifier.classify(format_sentence(s))
    return res
