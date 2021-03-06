import tweepy
from textblob import TextBlob
import matplotlib.pyplot as plt

#token for accessing the twitter app
api_key = ""
api_secret = ""
bearer_token = ""
access_key = ""
access_secret =  ""

#authenticataion for accessing twitter
auth = tweepy.OAuthHandler(api_key, api_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)

#does sentiment analysis on text take in the argument and prints the
# subjectivity and positivity
def SentimentAnalysis(userInput):
    blob = TextBlob(userInput)
    if blob.sentiment.polarity<-.75:
        print("Extremely Negative")
    elif blob.sentiment.polarity<-.25:
        print("Moderately Negative")
    elif blob.sentiment.polarity<0:
        print("Slightly Negative")
    elif blob.sentiment.polarity==0:
        print("Neutral")
    elif blob.sentiment.polarity<.25:
        print("Slightly Positive")
    elif blob.sentiment.polarity<.75:
        print("Moderately Positive")
    else:
        print("Extremely Positive")
    print("Positivity is ", blob.sentiment.polarity)

    if blob.sentiment.subjectivity<.17:
        print("Extremely Objective")
    elif blob.sentiment.subjectivity<.33:
        print("Moderately Objective")
    elif blob.sentiment.subjectivity<.5:
        print("Slightly Objective")
    elif blob.sentiment.subjectivity==.5:
        print("Neutral")
    elif blob.sentiment.subjectivity<.67:
        print("Slightly Subjective")
    elif blob.sentiment.subjectivity<.85:
        print("Moderately Subjective")
    else:
        print("Extremely Subjective")
    print("Subjectivity is ", blob.sentiment.subjectivity)

#pulls input from twitter by using the twitter username and calls the sentiment 
# analysis function to do sentiment analysis function on the tweets
def analyse_tweets(user_id, number_of_tweets = 1):
    count = 0
    tweets = api.user_timeline(user_id, count = number_of_tweets)
    for tweet in tweets:
        text = tweet.text
        print("The tweet contains: ", text)
        SentimentAnalysis(text)
        print()
        print()

#calculates the average polarity and subjectivity 
# over a certain num of tweets of a certain twitter user
def average_vibes(user_id, num):
    sumPolarity = 0
    sumSubjectivity = 0
    tweets = api.user_timeline(user_id, count = num)
    for tweet in tweets:
        text = TextBlob(tweet.text) #() instead of .
        sumPolarity += float(text.sentiment.polarity)
        sumSubjectivity += float(text.sentiment.subjectivity)
    avgPolarity = float(sumPolarity)/float(num)
    avgSubjecticity = float(sumSubjectivity)/float(num)
    print("The average polarity is ", avgPolarity)
    if avgPolarity<-.75:
        print("Extremely Negative")
    elif avgPolarity<-.25:
        print("Moderately Negative")
    elif avgPolarity<0:
        print("Slightly Negative")
    elif avgPolarity==0:
        print("Neutral")
    elif avgPolarity<.25:
        print("Slightly Positive")
    elif avgPolarity<.75:
        print("Moderately Positive")
    else:
        print("Extremely Positive")
    print("The average subjectivity is ", avgSubjecticity)
    if avgSubjecticity<.17:
        print("Extremely Objective")
    elif avgSubjecticity<.33:
        print("Moderately Objective")
    elif avgSubjecticity<.5:
        print("Slightly Objective")
    elif avgSubjecticity==.5:
        print("Neutral")
    elif avgSubjecticity<.67:
        print("Slightly Subjective")
    elif avgSubjecticity<.85:
        print("Moderately Subjective")
    else:
        print("Extremely Subjective")

#Plot tweets pulled polarity and subjectivity on a graph 
def plot2(user_id, num):
    ypoints = []
    xpoints = []
    tweets = api.user_timeline(user_id, count = num)
    for tweet in tweets:
        text = TextBlob(tweet.text)
        xpoints.append(float(text.sentiment.polarity))
        ypoints.append(float(text.sentiment.subjectivity))
    plt.plot(xpoints, ypoints, "o")
    plt.ylabel('subjectivity')
    plt.xlabel('polarity')
    plt.savefig("plot2.jpg")
    plt.show()

#main menu
def mainMenu():
    print("1. Type in texts")
    print("2. Pull from Twitter")
    print("3. Exit")

#menu loop which gives the options and calls the function
loop = True

while loop:

    mainMenu()
    option = input("Please Enter your option \n")

    if option == "1":
        print("Option 1 selected")
        userInput = input("Please Enter your text. \n")
        SentimentAnalysis(userInput)
        p = []
        s = []
        p.append(float(TextBlob(userInput).sentiment.polarity))
        s.append(float(TextBlob(userInput).sentiment.subjectivity))
        plt.plot(p, s, 'o')
        plt.xlabel('polarity')
        plt.ylabel('subjectivity')
        plt.savefig("plot1.jpg")
        plt.show()
        nextOption = input("Would you like to enter another text? Enter yes or no: \n")
        while nextOption == "yes":
            nextInput = input("Please enter your text: \n")
            SentimentAnalysis(nextInput)
            p.append(float(TextBlob(nextInput).sentiment.polarity))
            s.append(float(TextBlob(nextInput).sentiment.subjectivity))
            plt.plot(p, s, 'o')
            plt.xlabel('polarity')
            plt.ylabel('subjectivity')
            plt.savefig("plot1.jpg")
            plt.show()
            nextOption = input("Would you like to enter another text? Enter yes or no: \n")
        print("Thank you!")
                    

    elif option == "2":
        print("Option 2 selcted")
        uid = input("Enter username: ")
        tweetcount = input("How many tweets do you want to analyse? ")
        analyse_tweets(uid,tweetcount)
        choice = input("Do you want your average polarity and subjectivity feeback? Enter yes or no: \n")
        if choice == "yes":
            average_vibes(uid, tweetcount)
        else:
            print("Thank you!")
            
        plot2(uid, tweetcount);

    elif option == "3":
        print("Option 3 selected")
        confirmation = input("Are you sure you want to exit? Enter yes or no: \n")
        if confirmation.lower() == "yes":
            loop = False
        elif confirmation.lower() == "no":
            loop = True

    else:
        print
        print("Invalid option selected. Stop fat fingering")
        print("Choose again.")
 
   

    
