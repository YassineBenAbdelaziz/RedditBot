import praw 

reddit = praw.Reddit('bot1')
try :
    for submission in reddit.subreddit("testsubxxx").stream.submissions() :
        if submission.link_flair_text == "Serious " :
            comment = submission.reply("This is a serious post, only serious replies are allowed.")
            comment.mod.distinguish(how="yes", sticky=True)
            comment.mod.lock()
except KeyboardInterrupt :
    print("Over")


