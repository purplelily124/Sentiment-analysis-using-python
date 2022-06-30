# download textblob library 
from textblob import  TextBlob
#create a function 
def sentiment_analysis():
    while True:
        print("------------WELCOME TO SENTIMENT ANAYLSIS-------")
        text=str(input("ENTER YOUR TEXT:"))
        edu=TextBlob(text)
        text2=edu.sentiment.polarity
        textsub=edu.subjectivity
        print("THE POLARITY OF THE TEXT IS", text2)
        print("THE SUBJECTIVITY OF THE TEXT IS ",textsub)
        if (text2<0):
            print("The given statement is Negative")
        elif (text2==0):
            print("The given statement is Neutral")
        elif (text2>0):
            print("The given statement is Positive")
        break
sentiment_analysis()