from django.shortcuts import render, redirect
from django.views.generic import View
import json
from alexaweb_django.cred import *
from requests import Request

# Create your views here.


class StartAuthView(View):

	def get(self, request):
		scope_data = {
    					"alexa:all": {
        				"productID": PRODUCT_ID,
        				"productInstanceAttributes": {
            			"deviceSerialNumber": "12345"
        				}
    				}
				}
		scope_data = json.dumps(scope_data)
		url = "https://www.amazon.com/ap/oa"
		path = 	"http" + "://" + request.META["HTTP_HOST"]

		callback = path + '/code'
		payload = {
			"client_id": CLIENT_ID,
			"scope": "alexa:all",
			"scope_data": scope_data,
			"response_type": "code",
			"redirect_uri": callback
		}

		req = Request('GET', url, params=payload)
		req_prepared = req.prepare()
		return redirect(req_prepared.url)


class CodeAuthView(View):

	def get(self, request):
		code = request.GET["code"]
		path = request.protocol + "://" + request.host
		callback = path + "/code"
		payload = {
			"client_id": CLIENT_ID,
			"client_secret": CLIENT_SECRET,
			"code": code,
			"grant_type": "authorization_code",
			"redirect_uri": callback
		}
		url = "https://api.amazon.com/auth/o2/token"
		res = requests.post(url, data=payload)
		print res.text
