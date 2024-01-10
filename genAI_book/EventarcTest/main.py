from cloudevents.http import from_http
from flask import Flask, request

app = Flask(__name__)

# This handler is triggered by storage events
@app.route('/api/post', methods=['POST'])
def process_event():
    event = from_http(request.headers, request.data)
    event_id = event['id']
    event_type = event['type']
    bucket_name = event.data['bucket']
    filepath = event.data['name']
    filesize = event.data['size']
    content_type = event.data['contentType']

    print('Event contents: {}'.format(event))
    print('Event ID: {}'.format(event_id))
    print('Event type: {}'.format(event_type))
    print('Butcket name: {}'.format(bucket_name))
    print('Filepath: {}'.format(filepath))
    print('File size: {}'.format(filesize))
    print('Content type: {}'.format(content_type))

    return ('Succeeded', 200)
