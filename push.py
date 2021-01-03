
import os
import argparse
import urllib.request
from urllib.parse import quote
import re

ap = argparse.ArgumentParser()
ap.add_argument("-t", "--token", required=True, help="Telegram Bot token")
ap.add_argument("-c", "--chat", required=True, help="Chat id to notify")
ap.add_argument("-m", "--message", required=True, help="Text of the message")
args = vars(ap.parse_args())

url = "https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={message}".format(
	token = args["token"],
	chat_id = args["chat"],
	message = quote(args["message"]))

print(url)
urllib.request.urlopen(url).read()


def encode_url(b):
    return re.sub('[\x80-\xFF]', lambda c: '%%%02x' % ord(c.group(0)), b)