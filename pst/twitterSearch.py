from TwitterSearch import TwitterSearchOrder, TwitterSearchException, TwitterSearch
from .config import CONFIG
import logging
from .models import Politician
import os

def getTweets(politician_id):
	try:

		politician = Politician.objects.get(id=politician_id)

		politician_names = [politician.first_name + " " + politician.last_name, politician.last_name, politician.username]
	
		tso = TwitterSearchOrder()			
		sexistWords = ['bitch', 'skank', 'rape']
		searchTerms = []

		for word in sexistWords:
			for politician_name in politician_names:
				searchTerms.append(word + ' ' + politician_name)
		
		tso.set_keywords(searchTerms, or_operator=True)
		tso.set_language("en")
		tso.set_include_entities(False)
		querystr = tso.create_search_url()
		tso.set_search_url(querystr + "&tweet_mode=extended")

		ts = TwitterSearch(
            consumer_key = os.environ.get('CONSUMER_KEY', CONFIG['CONSUMER_KEY']),
            consumer_secret = os.environ.get('CONSUMER_SECRET', CONFIG['CONSUMER_SECRET']),
            access_token = os.environ.get('ACCESS_TOKEN', CONFIG['ACCESS_TOKEN']),
            access_token_secret = os.environ.get('ACCESS_TOKEN_SECRET', CONFIG['ACCESS_TOKEN_SECRET'])
        )
		
		tweets = ts.search_tweets_iterable(tso)
		print("Got tweets for " + str(politician.first_name + " " + politician.last_name))
		return tweets

	except TwitterSearchException as e:
		logging.exception("Unable to get new tweets because of"  + str(e))

# if __name__ == "__main__":
#     getTweets()