import wiihacky
import random

if __name__ == "__main__":
    wh = wiihacky.WiiHacky()
    subreddit = wh.reddit.subreddit('wiihacks')
    comment = random.choice(list(subreddit.comments()))
    message = random.choice(list(wh.reddit.inbox.messages()))
    ac = wiihacky.actions.ScrapeMessage(wh.log, message)
