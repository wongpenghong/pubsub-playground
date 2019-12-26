import time
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
subscription_name = CONFIG['sub_id']

subscriber = pubsub_v1.SubscriberClient()
subscription_path = subscriber.subscription_path(
    project_id, subscription_name)

def callback(message):
    print('Received message: {}'.format(message.data))
    if message.attributes:
        print('Attributes:')
        for key in message.attributes:
            value = message.attributes.get(key)
            print('{}: {}'.format(key, value))
    message.ack()

subscriber.subscribe(subscription_path, callback=callback)

# The subscriber is non-blocking, so we must keep the main thread from
# exiting to allow it to process messages in the background.
print('Listening for messages on {}'.format(subscription_path))
# while True:
#     time.sleep(60)