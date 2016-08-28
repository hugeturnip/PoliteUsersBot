Giimport praw
import time

r = praw.Reddit(user_agent = "A bot to thank users for being nice on reddit created by /u/kooldawgstar")
print("Logging in...")
r.login("USERNAME","PASSWORD", disable_warnings = True)

words_to_match = ['Please', 'thank you', 'welcome', 'You are welcome', 'May I', 'Excuse me', 'Pardon', 'sorry', 'thanks ', ' thanks']
cache = []

nice = len(cache)

def run_bot():
    print("Grabbing subreddits...")
    subreddit = r.get_subreddit("all")
    comments = subreddit.get_comments(limit=25)
    print("Grabbing comments...")
    for comment in comments:
        comment_text = comment.body.lower()
        isMatch = any(string in comment_text for string in words_to_match)
        if comment.id not in cache and isMatch:
            print("Match found! Comment ID: " + comment.id)
            comment.reply("Thank you for being a polite user on reddit! \n\n*This bot was created by [kooldawgstar](http://reddit.com/u/kooldawgstar), if this bot is an annoyance to your subreddit feel free to ban it. [Fork me on Github](http://www.github.com/kooldawgstar/PoliteUsersBot) For more information check out /r/Polite_Users_Bot!*")
            print("Reply Sucessful")
            cache.append(comment.id)
    print("Comment loop finished, bot sleeping")
while True:
    try:
        run_bot()
        time.sleep(60)
    except:
        pass
