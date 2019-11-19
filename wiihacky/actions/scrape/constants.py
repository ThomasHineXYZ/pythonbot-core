import praw as pr

DATA_DIR = 'data'

FILE_DELIM = '-'
FILE_SUFFIX = '.yml'

TXT_ERR_DIR = 'Could not verify directory: {}'
TXT_ERR_EXCEPT = 'An exception occurred while {}: {}'
TXT_ERR_SAVE = 'Could not save file: {}'

TXT_AUTHOR = 'author'
TXT_ID = 'id'
TXT_KARMA = 'karma'
TXT_NAME = 'name'
TXT_REPLIES = 'replies'
TXT_START = 'Scraping'
TXT_SAVING = 'Saving {} data'
TXT_SUBMISSION = 'submission'
TXT_SUBREDDIT = 'subreddit'
TXT_TYPE = 'type'
TXT_UTC_STAMP = 'utc_timestamp'

# noinspection PyUnresolvedReferences
TXT_FETCH_FUNC = pr.models.reddit.base.RedditBase._fetch.__name__

# TXT_INBOX = 'Inbox'
# TXT_COMMENT = 'comment'
# TXT_MESSAGE = 'Message'
# TXT_REDDITOR = 'redditor'
# OB_USER = 'User'
# FILE_PATH = '/'
#KEY_OWNER = 'owner'
#TYPE_COMMENT = 'Comment'
#TYPE_MULTIREDDIT = 'Multireddit'
#TYPE_SUBREDDIT = 'Subreddit'
#TYPE_USER = 'User'
# Scraper module txt constants
#SCRAPE_DEL_AUTHOR = '_author'
#SCRAPE_DEL_AWARDERS = 'awarders'
#SCRAPE_DEL_COMMENTS = '_comments'
#SCRAPE_DEL_COMMENTS_BY_ID = '_comments_by_id'
#SCRAPE_DEL_PATH = '_path'
#SCRAPE_DEL_REDDIT = '_reddit'
#SCRAPE_DEST = 'dest'
#SCRAPE_COMMENTS = 'comments'
#SCRAPE_PATH = 'path'
#SCRAPE_SUBMISSIONS = 'submissions'
#SCRAPE_SUBREDDITS = 'subreddits'