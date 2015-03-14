import os
import json

from instagram.client import InstagramAPI
from header import gram_access_token

# access_token = os.environ.get('GRAM_ACCESS_TOKEN', None)
api = InstagramAPI(access_token=gram_access_token)


def get_grams():
    grams, nex = api.user_recent_media(user_id='11728698', count=4)
    gram_package = []

    for gram in grams:
        gram_json = {}
        photo = str(gram.images['thumbnail'])
        photo = photo[7:]
        gram_json['photo'] = photo
        gram_json['url'] = gram.link
        gram_package.append(gram_json)

    return gram_package
