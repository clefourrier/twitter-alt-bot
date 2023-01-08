import requests
import json
import tweepy
import gradio


def generate_caption(image_url):
    space = gr.Interface.load("olivierdehaene/git-large-coco", src="spaces")
    caption = space(image_url)
    return caption


def tweet_caption(caption):
    #requests.post("url", json)
    api.update_status(status = message)


# TWEETING ##########################################################################################

def tweet(message):
    """Post a tweet"""
    from secrets import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET

    # Twitter authentication
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)

    # posting
    tagged_on = tweepy.Cursor(api.search, q='@AltImageBot1').items(1)

    for tweet in tagged_on:
        parent_tweet = api.get_status(tweet.in_reply_to_status_id)
        if 'media' in parent_tweet.entities:
            for image in parent_tweet.entities['media']:
                caption = generate_caption(image['media_url'])
                tweet_caption(caption)

if __name__ == "__main__":
    tweet(message)
    
    