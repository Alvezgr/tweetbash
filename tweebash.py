"""module for tweepy app"""

import sys
import tweepy
from read import get_pass


# Accessing twitter
def access_twitter():
    """method for authenticate in twitter"""

    consumer_key = get_pass('consumer_key')
    consumer_secret = get_pass('consumer_secret')

    access_token = get_pass('access_token')
    access_token_secret = get_pass('access_token_secret')

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)

    return api


def update_status():
    """method for update the status in 240 chars"""

    tweet = access_twitter()

    try:
        twit = str(sys.argv[1])
        if len(twit) > 238:
            return 'Tweet to long'

    except IndexError:
        return 'Non tweet to update'

    tweet.update_status(twit)
    return f'Tweett published, all ok! tweet: {twit}'


if __name__ == '__main__':
    print(update_status())
