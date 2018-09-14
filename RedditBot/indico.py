import indicoio
from config import INDICO_API_KEY
from redditbot import payload
indicoio.config.api_key = INDICO_API_KEY

# single example
print(payload)
results = indicoio.sentiment(payload)
print(results)