# This file will be reomved later, is here for testing of various functionalities before it is introduced to the main
# program.

# TODO : All other types of classifiers, to detect all sentiments in a sentence.
import textblob
from textblob import TextBlob
from textblob.classifiers import NaiveBayesClassifier
from textblob.np_extractors import ConllExtractor

train_depressed = [("I feel sad", 'dep'),
                   ("I dont feel alright", 'dep'),
                   ("I dont look forward to tomorrow", 'dep'),
                   ("I wish I werent here", 'dep'),
                   ("I want all of this to end", 'dep'),
                   ("I don't know what I am living for", 'dep'),
                   ("I am very happy with the way things are", 'happy'),
                   ("I am ok, still alive", 'dep'),
                   ("I am feeling good", 'happy'),
                   ("I never do enough", 'dep'),
                   ("I should be better", 'dep'),
                   ("I am fine", 'happy'),
                   ("I am look forward to tomorrow", 'happy'),
                   ("This is great", 'happy'),
                   ("Things aren't great", 'dep'),
                   ("Things could be better", 'dep'),
                   ("I dont want to wake up tomorrow", 'dep'),
                   ("I cant wait for tomorrow", 'happy'),
                   ("I am tired of life", 'dep'),
                   ("Life is amazing", 'happy'),
                   ("This is intriguing", 'happy'),
                   ("I feel very tired", 'dep'),
                   ("I feel alone", 'dep'),
                   ("I am feeling blesses", 'happy'),
                   ("There is too much work", 'dep'),
                   ("there isnt enough work", 'dep'),
                   ("I cant make this work", 'dep'),
                   ("I can do anything", 'happy'),
                   ("There is always a way", 'happy'),
                   ("I feel better than before", 'happy'),
                   ("I am sad", 'dep'),
                   ("Life is pointless", 'dep'),
                   ("Life is beautiful", 'happy'),
                   ("There is nothing more to life", 'dep'),
                   ("There is more to life than I can understand", 'happy'),
                   ("I don't want to do this anymore", 'dep'),
                   ("I wish I could be better", 'dep'),
                   ("I have never been better", 'happy'),
                   ("This is the worst", 'dep'),
                   ("This is the best", 'happy'),
                   ("I am not happy", 'dep'),
                   ("I am sad", 'dep'),
                   ("I feel alone", ' dep'),
                   ("This is the best", 'happy'),
                   ("This is not good", 'dep'),
                   ("I am unhappy", 'dep'),
                   ("I don't think I can feel better", 'happy'),
                   ("I keep blaming myself", 'dep'),
                   ("If I was a lot better, I could have saved the day", 'dep'),
                   ("I did a decent job", 'happy'),
                   ("I did awesome", 'happy'),
                   ("I am great at this", 'happy'),
                   ("Wish I could have been better", 'dep'),
                   ("I should have done a better job on my content theory", 'dep'),
                   ("I could have done a lot better", 'dep'),
                   ("If only I was better", 'dep'),
                   ("I wish I did better", 'dep'),
                   ("I wish I did better on this subject", 'dep')
                   ]

test_depressed = [("I don't want to do this anymore", 'dep'),
                  ("I wish I could be better", 'dep'),
                  ("I have never been better", 'happy'),
                  ("This is the worst", 'dep'),
                  ("This is the best", 'happy'),
                  ("I am not happy", 'dep'),
                  ("I am sad", 'dep'),
                  ("I feel alone", ' dep'),
                  ("This is the best", 'happy'),
                  ("This is not good", 'dep'),
                  ("I am unhappy", 'dep'),
                  ("I don't think I can feel better", 'happy'),
                  ("I am not happy", 'dep'),
                  ("I am sad", 'dep'),
                  ("I feel alone", ' dep'),
                  ("This is the best", 'happy'),
                  ("This is not good", 'dep'),
                  ("I am unhappy", 'dep'),
                  ("I don't think I can feel better", 'happy'),
                  ("I keep blaming myself", 'dep'),
                  ("If I was a lot better, I could have saved the day", 'dep'),
                  ("I did a decent job", 'happy'),
                  ("I should have done a better job on my content theory", 'dep'),
                  ("I could have done a lot better", 'dep'),
                  ("If only I was better", 'dep'),
                  ("I wish I did better", 'dep'),
                  ("I wish I did better on this subject", 'dep')
                  ]

train_selfesteem = [("I feel happy and content", 'highselfesteem'),
                    ("I feel respected", 'highselfesteem'),
                    ("I don't like myself", 'lowselfesteem'),
                    ("I can do anything", 'highselfesteem'),
                    ("I can't do anything", 'lowselfesteem'),
                    ("There isn't anything I can do about it, I don't feel in control", 'lowselfesteem'),
                    ("I will do something about it", 'highselfesteem'),
                    ("I cannot handle this", 'lowselfesteem'),
                    ("I am useless", 'lowselfesteem'),
                    ("I am trash", 'lowselfesteem'),
                    ("I am the best", 'highselfesteem'),
                    ("I did really well, I can do no wrong", 'highselfesteem')
                    ]


# Common function for all possible training samples, this is the API provided to other classes
def traintestclassifier(train_dataset, test_dataset, classifystring):
    # Trains a NaiveBayesClassifier
    classifier = NaiveBayesClassifier(train_dataset)
    prob_dist = classifier.prob_classify(classifystring)
    positive_prob = round(prob_dist.prob("dep"), 2)
    negative_prob = round(prob_dist.prob("happy"), 2)
    print(positive_prob, "is the probability of this sentence being depressing")
    print(negative_prob, "is the probability of this sentence being happy")
    print(classifier.accuracy(test_dataset), "Is the accuracy")
    return classifier


# Common function to find the main actor in a sentence or the subject that sentence is about
def findreason(sentence):
    reason = list()
    reasonExtractor = TextBlob(sentence)
    for reasonInstance in reasonExtractor.noun_phrases:
        print(reasonInstance)
        reason.append(reasonInstance)
    if len(reason) == 0:
        reason.append([sentence])
    print(len(reason))
    return reason


def main():
    tempsentence = "Vini killed my dog and made me sad"
    print("The sentence to be checked is : ", tempsentence)
    depressed_classifier = traintestclassifier(train_depressed, test_depressed, tempsentence)
    # The reason is to be returned to the agent to be added to list of reasons for feeling a particular way.
    print("The reason for my depression ->", findreason(tempsentence))


if __name__ == "__main__":
    main()
