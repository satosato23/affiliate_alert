
from amazon_paapi import AmazonApi
import tweepy
import datetime
import time
import requests



AMAZON_ACCESS_KEY = "api_key"
AMAZON_SECRET_KEY = "api_secret"
AMAZON_ASSOC_TAG    = "access_tag"
COUNTRY=""

amazon = AmazonApi(AMAZON_ACCESS_KEY, AMAZON_SECRET_KEY, AMAZON_ASSOC_TAG, COUNTRY)


#twitter api
consumer_key=""
consumer_secret=""
access_key=""
access_secret=""

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_key,access_secret)
api = tweepy.API(auth)

def amazon_blue_ray():
    #products = amazon.search_items(keywords='speaker',item_count=10)
    products = amazon.search_items(browse_node_id='403507011',item_count=10,sort_by="Featured")
    

    x=0
    stop=1
    while x <10:
        try:
            #asin     = products["data"][0].asin
            price    = products["data"][x].offers.listings[0].price.amount
            price = int(price)
            url      = products["data"][x].detail_page_url
            title    = products["data"][x].item_info.title.display_value
            actor = products["data"][x].item_info.by_line_info.contributors[0]
            actor = actor.replace(" ","")
            todaydetail = datetime.datetime.now()
            now = todaydetail.strftime('%H時%M分 ')
            x+=1
            print(title+actor.name+url)
           
          
        except Exception as e:
            print(e)
            x+=1
            

def rakute_aff():
   
    url = 'https://app.rakuten.co.jp/services/api/IchibaItem/Search/20140222'

    payload = {
        'applicationId': [],
        'affiliateId':[],
        'keyword': '',
        'shopCode': '',
        'genreId': '101070',
        'hits': 10,
        'sort': '+reviewAverage',
        }
    # +affiliateRate,+reviewCount,+reviewAverage,+itemPrice,+updateTimestamp
    r = requests.get(url, params=payload)

    resp = r.json()
    #print ("num of kensaku =",resp['count'])
    print ('-'*40)

    for i in resp['Items']:
        item = i['Item']
        #api.update_status(item["shopName"]+":"+item['itemName']+":大人気発売中！\n"+item["affiliateUrl"])
        api.update_statu(":\n"+item['itemName']+"\n大人気発売中！"+item["affiliateUrl"])

        print ('-'*40)
        time.sleep(600)