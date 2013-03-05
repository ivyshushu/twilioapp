# Create your views here.
from sms.models import Contacts
from django.http import Http404, HttpResponse
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from twilio.rest import TwilioRestClient

def index(request):
	return render(request, 'index.html')


def send(request):
	number = request.GET['send_to']
	account_sid = 'AC25ef232740072dc660a9b676d9e5c992'
	auth_token = 'ff5269d59167dedf051268d5ef3e4b91'
	client = TwilioRestClient(account_sid, auth_token)
	message = client.sms.messages.create(to=number, from_="+13473086943", body="Hello there!")
	return HttpResponse("Text sent to" + number)


def search_friends(request):
	name = request.GET['name']
	try:
		friend = Contacts.objects.get(friend_name=name)
	except:
		raise Http404
	number = "+1" + friend.get_phone_number()
	return render_to_response('results.html', {'object':friend, 'number':number}, RequestContext(request))
	



    

