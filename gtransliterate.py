# Google Transliteration Api
from urllib import request
from urllib.parse import quote
import json


# url = https://www.google.com/inputtools/request?text=bhaang,bhaang&ime=transliteration_en_hi&num=3
# url = "https://www.google.com/inputtools/request?text=bhaang&ime=transliteration_en_hi&num=3"

word = quote("भांग")
url = f"https://www.google.com/inputtools/request?text={word}&ime=transliteration_hi_en&num=3"


response = request.urlopen(url).read()
response = json.loads(response)
print(response)
