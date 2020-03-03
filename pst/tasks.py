# Create your tasks here
from __future__ import absolute_import, unicode_literals
from celery import shared_task


@shared_task
def test(arg):
    print(arg)


@shared_task
def fetchSexistTweets():
    from pst.tweet_handling.fetchTweets import fetchTweets
    from .models import Politician
    politician_ids = Politician.objects.values_list('id', flat=True)
    fetchTweets(politician_ids, True)


@shared_task
def fetchAllTweets():
    from pst.tweet_handling.fetchTweets import fetchTweets
    from .models import Politician
    politician_ids = Politician.objects.values_list('id', flat=True)
    fetchTweets(politician_ids, False)


@shared_task
def updateTweetToxicity():
    from .models import Politician, Tweet
    from pst.tweet_handling.perspectiveapi import get_and_update_toxicity
    politician_ids = Politician.objects.values_list('id', flat=True)
    for pid in politician_ids:
        recent_tweets = Tweet.objects.filter(politician_id=pid).filter(toxicity__isnull=True).order_by('-date')[:10]
        for tweet in recent_tweets:
            get_and_update_toxicity(tweet)
