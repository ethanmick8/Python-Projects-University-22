# Author: Ethan Mick
# Instructor: Dale Musser
# Explanation: This program simulates a very simplistic version of the social media
# platform known as Twitter. It allows uses to make tweets, view recent tweets,  and 
# search tweets. Tweets are stored as objects using the class defined in Tweet.py.

import TweetManager.Tweet as tweet # import Tweet.py module to allow creation of tweets
import pickle # import module to allow us to serialize tweet data
from os import path # used to check if "tweets.dat" exists

# Here, I've defined a specific error to be raised when user input for the tweet menu is an
# integer, but not 1, 2, 3, or 4.
class Error(Exception):
    pass
class OutOfRangeError(Error):
    pass

# Before commencing with the program, we must check to see if any previous tweets were
# stored in tweets.dat, the designated data file for storing user-created tweets made with
# this program. If so, the program's list of tweets will include those previously-made
# tweets, so that even if this program is run multiple times, old tweets can still be searched
# for, displayed, etc.
tweet_list = [] # define an empty list to hold tweets that are made
filename = "tweets.dat"
if(path.exists(filename)): # check if the file storing previous tweets exists
    with open(filename, "rb") as infile:
        tweet_list = pickle.load(infile) # load stored data into tweet_list using pickle module

def main():
    while(True):
        print("Tweet Menu")
        print("------")
        print("1. Make a Tweet")
        print("2. View Recent Tweets")
        print("3. Search Tweets")
        print("4. Quit")
        while(True): # loop until user enters a valid integer from the menu
            try:
                choice = int(input("\nWhat would you like to do? "))
                if choice < 1 or choice > 4:
                    raise OutOfRangeError
                break
            except:
                print("Please select a valid option\n")

        if(choice == 1): # make a new tweet
            name = input("\nWhat is your name? ")
            length_tester = True
            while(length_tester):
                text = input("What would you like to tweet? ")
                if(len(text) > 140): # tweets cannot be larger than 140 characters
                    print("Tweets can only be 140 characters!")
                    continue # prompt user for a tweet again
                else:
                    break # tweet meets guidelines
            new_tweet = tweet.Tweet(name, text) # create the tweet
            tweet_list.append(new_tweet) # add the new tweet to the list
            print(name + ", your tweet has been saved.\n")

        if(choice == 2): # browse recent tweets
            print("Recent Tweets")
            print("------")
            if(len(tweet_list) == 0): # if no tweets have been made
                print("There are no recent Tweets.\n")
            else:
                min = len(tweet_list) - 6 # variable used to restrict how many tweets are displayed
                for i in range(len(tweet_list)-1, min, -1): # traverse list in reverse order to get most recent
                    print(tweet_list[i])

        if(choice == 3): # search all tweets for a query
            if(len(tweet_list) == 0):
                print("\nThere are no tweets to search. Try tweeting something!\n")
            else:
                query = input("What would you like to search for? ")
                print("\nSearch Results")
                print("------")
                checker = 0 # variable to check whether or not any match was found
                for j in range(len(tweet_list)-1,-1,-1): # traverse list backwards
                    if query in tweet_list[j].get_text(): # if the tweet is found
                        checker = 1 # success, a tweet was found with query in it
                        print(tweet_list[j])
                if(checker == 0): # no tweet was found
                    print("No tweets contained" + query + "\n")

        if(choice == 4): # end the program, saving all new tweets from this use to the outfile using pickle
            with open("tweets.dat", "wb") as outfile:
                pickle.dump(tweet_list, outfile) # use pickle module to serialize data
            print("Thank you for using the Tweet Manager!")
            break # end the program

main()
                    


            

