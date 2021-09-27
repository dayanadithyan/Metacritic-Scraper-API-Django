
import psaw
from psaw import PushshiftAPI
import pandas as pd
import numpy as np

# # deps: psaw, pandas, numpy

## define the class

class RedditScraper(object):
    
    
    def __init__(self, subred, queries):
        
        self.subr = subred
        
        self.subq = queries
        
        self.reddit_api = PushshiftAPI()
        
        
    def extract_threads(self):
        
       '''
       
       '''
       
       ls = []
       
       for channel in self.subr:

           for query in self.subq:

               generator_obj_1 = self.reddit_api.search_comments(q=query, subreddit=channel)

               submissions = pd.DataFrame([comment.d_ for comment in generator_obj_1])

               submissions['Search_Term'] = query

               submissions['Search_Subreddit'] = channel

               ls.append(submissions)

               #print('Comment extraction complete for {} in {}'.format(query,channel)) ## find a way to log to user


       df = pd.concat(ls)

       return df.to_csv('RedditComments-8-24.csv')

##############
       
    def extract_comments(self):
       
       
       ls = []
       
       
       for channel in self.subr:

           for query in self.subq:

               generator_obj = self.reddit_api.search_submissions(q=query, subreddit=channel)

               submissions = pd.DataFrame([submission.d_ for submission in generator_obj])

               submissions['Search_Term'] = query

               submissions['Search_Subreddit'] = channel

               ls.append(submissions)

               #print('Thread extraction complete for {} in {}'.format(query,channel))


       df = pd.concat(ls)
       
       return df.to_csv('RedditThreads-8-24.csv')
   
   
    def run_scraper(self):
        
        self.extract_threads()
        
        self.extract_comments()
        
        return None
        
       
###########       

if __name__ == "__main__":

    pass
