import json
import uuid

import openrtb
import geoip2.database

from django.shortcuts import HttpResponse
from django.conf import settings

def test_blank(request):
    return HttpResponse('', content_type='application/json')

def test_json(request):
    request_dict = json.loads(request.body)
    response_string = json.dumps(request_dict)
    return HttpResponse('', content_type="application/json")

def test_openrtb(request):
    request_dict = json.loads(request.body)
    bidrequest = openrtb.request.BidRequest.deserialize(request_json)
    openrtb.serialize(request_dict)

    return HttpResponse('', content_type="application/json")

def test_uuid(request):
    test_id = uuid.uuid1()
    return HttpResponse('', content_type="application/json")

def test_geoip(request):
    reader = geoip2.database.Reader('/usr/local/share/maxmind/GeoCity.dat')
    response = reader.city('54.164.138.201')
    return HttpResponse('', content_type="application/json")

def test_kafka(request):
    KAFKA_BROKER_URL    = "127.0.0.1:9092"
    KAFKA_TIMEOUT       = 5
    kafka_client = KafkaClient(KAFKA_BROKER_URL, timeout = KAFKA_TIMEOUT)
    kafka_producer = SimpleProducer(kafka_client)
    kafka_producer.send_messages("dummy_test", outcome_json)
    return HttpResponse('', content_type="application/json")
