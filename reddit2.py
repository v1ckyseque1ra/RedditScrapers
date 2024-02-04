#[[[[SCRAPPING REDDIT POST]]]]]

#2 libraries
#praw to access Reddit
#Pandas to tabulate the data and clean it

import pandas as pd
import praw
from praw.models import MoreComments

#create a Reddit object where we inset the credentials created
#when reggistered for the Reddit app

reddit = praw.Reddit(user_agent="Comment Extraction (by /u/DataScrapingEurope)",
                     client_id="pXtqtGWntXaqdOra0-mFeg", client_secret="DVNG7SKt8LjPZTqMPEvuej_tpZBoGw")

#pick up a post to scrape

url = "https://www.reddit.com/r/SpainPolitics/comments/18wshxc/nace_izquierda_espa%C3%B1ola_un_nuevo_partido_de/"
submission = reddit.submission(url=url)


posts = []
for top_level_comment in submission.comments[1:]:
    if isinstance(top_level_comment, MoreComments):
        continue
    posts.append(top_level_comment.body)
posts = pd.DataFrame(posts,columns=["body"])
indexNames = posts[(posts.body == '[removed]') | (posts.body == '[deleted]')].index
posts.drop(indexNames, inplace=True)
print(posts)

#CLEANING DATA (remove eliminated posts)
indexNames = posts[(posts.body == '[removed]') | (posts.body == '[deleted]')].index

posts.drop(indexNames, inplace=True)