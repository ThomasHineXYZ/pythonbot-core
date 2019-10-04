"""Scrapper Module."""

import logging as lg
import time as tm
import praw as pr


import wiihacky.const as const

lg.basicConfig(
    level=lg.INFO,
    format=const.LOG_FORMAT_STRING)


class Scraper:
    """Scrape data from reddit to dict format."""

    def __init__(self):
        """Initialize the scraper."""
        # Logger
        self.log = lg.getLogger(self.__class__.__name__)

    def scrape(self, target):
        """Scrape object.

        A general scrape function. It can be given a single or list or tuple
        of praw objects and it will return either a single dict, or a list
        of dicts if more than one object was given.
        """
        if isinstance(target, (list, tuple)):
            return [self.scrape(item) for item in target]

        if isinstance(target, pr.models.user.User):
            return self.scrape_user(target)

        self.log.error(const.SCRAPE_TYPE_UNSUPPORTED, type(target))
        return []

    def scrape_inbox(self, inbox):
        """Scrape inbox.

        This function will scrape the inbox and make sure it is up to date.

        Return
        ------
        This will return a dictionary with all inbox data.

        """
        # Log
        info = self.log.info
        info(const.SCRAPE_INBOX)
        info(const.SCRAPE_COMPLETE)

    def scrape_user(self, user):
        """Scrape user.

        This function will scrape the user and update the user record.

        Return
        ------
        This will return a dictionary with all user data.

        """
        # Log
        info = self.log.info

        info(const.SCRAPE_USER)
        blck = list(user.blocked())
        frnd = list(user.friends())
        mods = list(user.moderator_subreddits())
        mult = list(user.multireddits())
        subs = list(user.subreddits())
        output = {
            const.SCRAPE_UTC_STAMP: int(tm.time()),
            const.SCRAPE_TYPE: user.__class__.__name__,
            const.SCRAPE_ID: user.me().id,
            user.blocked.__name__: [a.id for a in blck],
            user.friends.__name__: [a.id for a in frnd],
            user.karma.__name__: user.karma(),
            user.moderator_subreddits.__name__: [a.id for a in mods],
            user.multireddits.__name__: [a.name for a in mult],
            user.preferences.__class__.__name__: dict(user.preferences()),
            user.subreddits.__name__: [a.id for a in subs]}
        self.scrape([blck, frnd, mods, mult, subs])
        info(const.SCRAPE_COMPLETE)
        return output
