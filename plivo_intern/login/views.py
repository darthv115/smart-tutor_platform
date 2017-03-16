from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
import plivo
import random

def index(request):
    nothing = {}
    return render(request,'land.html',context=nothing)

def sms(request):
    print "plivo"
    auth_id = "MAZDJMNGRMODVMM2NHOT"
    auth_token = "OWEwZWNkYzBhZGMxOWE5MzgzMTc5YWY3ZDU2MTIw"

    p = plivo.RestAPI(auth_id, auth_token)
    num = 2456;
    params = {
        'src': '+918897558700', # Sender's phone number with country code
        'dst' : '+919989363108', # Receiver's phone Number with country code
        'text' : u"Hello Babluuuu "+str(num)+" Ill push this much on github ... this is just sending an sms on button click, not verification code", # Your SMS Text Message - English

        'url' : "http://example.com/report/", # The URL to which with the status of the message is sent
        'method' : 'POST' # The method used to call the url
    }

    response = p.send_message(params)
    nothing = {}
    return HttpResponseRedirect('/sms/sent')

def sent(request):
    nothing = {}
    return render(request,'test.html',context=nothing)
# class PlivoTwoFactorAuth:
#     def __init__(self, credentails, appNumber):
#         self.p = plivo.RestAPI(credentails["auth_id"],
#             credentails["auth_token"])
#         self.appNumber = appNumber
#     def getVerificationCode(self, dstNumber, message="__code__"):
#         code = random.choice(xrange(100000,999999))
#         responseCode, responseData = self.p.send_message({
#             "src": self.appNumber,
#             "dst": dstNumber,
#             "text": message.replace("__code__", str(code)).strip(),
#             "type": "sms"               
#         })
#         if responseCode != 202:
#             raise Exception
#         return code

# auth_id = MAZDJMNGRMODVMM2NHOT
# auth_token = OWEwZWNkYzBhZGMxOWE5MzgzMTc5YWY3ZDU2MTIw
# number = 9989363108

# def verify():
# 	p2fa = PlivoTwoFactorAuth({
# 		"auth_id": auth_id,
# 		"auth_token": auth_token
# 		} appNumber=8897558700)
# 	code = p2fa.getVerificationCode(number, "Your verification code is __code__")  # String should be less than 160 chars
# 	r.setex("number:%s:code" % number, code, 60*15)  # Verification code is valid for 15 mins
# 	return jsonify({"status": "success", "message": "verification initiated"})