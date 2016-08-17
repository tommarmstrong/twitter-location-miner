# Twitter Location Stream Miner

Pipes location based live stream of tweets to stdout which can be piped to a text file to save tweets.

e.g. ```python main.py > tweets.txt```

## Installation & Config
- ```pip install -r requirements.txt```
- Create a Twitter app and access token
- Clone ```.env.example``` into ```.env```
- Populate ```.env``` with your credentials and the locations you want to search within

Tip: see the [Twitter Docs](https://dev.twitter.com/streaming/overview/request-parameters#locations) for more info on the location parameter