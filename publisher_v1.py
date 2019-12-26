import os

"""Publishes multiple messages to a Pub/Sub topic with an error handler."""
## this pylint for resolve instance object has no member error
# pylint: disable=no-member
import json
import re

with open("config_pubsub.json", "r") as read_file:
    CONFIG = json.load(read_file)['config_pubsub']

from google.cloud import pubsub_v1

# TODO project_id = "Your Google Cloud Project ID"
project_id = CONFIG['project_id']
# TODO topic_name = "Your Pub/Sub topic name"
topic_name = CONFIG['topic_id']

# TODO path_name = "Your path file"
path = CONFIG['path']


if(os.path.exists(path)):
    client = pubsub_v1.PublisherClient()

    # Get Topic
    topic_path = client.topic_path(project_id, topic_name)

    with open(path) as json_file:
        data = json.load(json_file)

    # Formatting Data Format
    datas = u"{}".format(data)
    datas = re.sub("'", '"',datas)
    datas = datas.encode('utf-8')
    # Push to PubSub
    
    # TODO origin_id = "Your Origin name"
    # TODO user_id = "Your Username"
    future = client.publish(topic_path, datas, origin='origin_id', username='user_id')
    
    # delete the file
    os.remove(path)
else:
    print('No Data!!!')