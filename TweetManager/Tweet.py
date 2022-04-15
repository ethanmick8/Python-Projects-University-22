# Author: Ethan Mick
# Instructor: Dale Musser
# Explanation: This program defines a class that stores data regarding a "Tweet" message
# that the program "twitter.py" will use. As the names suggest, the programs will outline
# a simple representation of the way the social media platform Twitter operates.

import time; # time module for use with tweet age

class Tweet(object):
    def __init__(self, author, text):
        self.__author = author
        self.__text = text
        self.__age = time.time()

    # method to retrieve the author of the tweet
    def get_author(self):
        return self.__author

    # retrieve tweet text
    def get_text(self):
        return self.__text

    # retreive age of tweet (operates up to 24h)
    def get_age(self):
        current_time = time.time()
        net_time = int(current_time - self.__age)
        if(net_time >= 0 and net_time < 60): # tweet is 1-59 seconds old
            return str(net_time) + "s"
        elif(net_time >= 60 and net_time < 3600): # tweet is some number of minutes old (< 1h)
            return str(int(net_time/60)) + "m"
        elif(net_time >= 3600 and net_time < 86400): # tweet is some # of hours old (< 1d)
            return str(int(net_time/3600)) + "h"

    # string method defined to simplify storage of object in display-friendly form
    # (in "twitter.py", tweets that are made will be stored to a list and they will
    # default to being stored in the format outlined by this method; it gets around
    # privately stored attributes like __author not being retrievable and such)
    def __str__(self):
        return self.__author + " - " + self.get_age() + "\n" + self.__text + "\n"