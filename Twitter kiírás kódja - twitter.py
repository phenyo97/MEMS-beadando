import tweepy
from datetime import datetime

TW_API_KEY = 'YOUR API KEY' #Twitter által megadott API kulcs
TW_API_SEC = 'YOUR API SECRET' #Twitter által megadott titkosított API
TW_ACC_TOK = 'YOUR ACCESS TOKEN' #Twitter által megadott hozzáférési jegy
TW_ACC_TOK_SEC = 'YOUR ACCESS TOKEN SECRET' #Twitter által megadotttitkosított hozzáférési jegy

auth = tweepy.OAuthHandler(TW_API_KEY, TW_API_SEC)
auth.set_access_token(TW_ACC_TOK, TW_ACC_TOK_SEC)
api = tweepy.API(auth)

tempf = open("/sys/bus/w1/devices/00-800000000000/w1_slave")
thetext = tempf.read()
tempf.close()
tempdta = thetext.split("\n")[1].split(" ")[9]
temper = float(tempdta[2:])
temper = str(temper / 1000)

thetime = datetime.now().strftime('%-I:%M%P on %d-%m-%Y')

api.update_status(temper + " C at " + thetime)
