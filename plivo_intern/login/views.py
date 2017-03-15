from django.shortcuts import render
from django.http import HttpResponse
import plivo
import random

def index(request):
    nothing = {}
    return render(request,'land.html',context=nothing)


class PlivoTwoFactorAuth:
    def __init__(self, credentails, appNumber):
        self.p = plivo.RestAPI(credentails["auth_id"],
            credentails["auth_token"])
        self.appNumber = appNumber
    def getVerificationCode(self, dstNumber, message="__code__"):
        code = random.choice(xrange(100000,999999))
        responseCode, responseData = self.p.send_message({
            "src": self.appNumber,
            "dst": dstNumber,
            "text": message.replace("__code__", str(code)).strip(),
            "type": "sms"               
        })
        if responseCode != 202:
            raise Exception
        return code

auth_id = MAZDJMNGRMODVMM2NHOT
auth_token = OWEwZWNkYzBhZGMxOWE5MzgzMTc5YWY3ZDU2MTIw
number = 9989363108

def verify():
	p2fa = PlivoTwoFactorAuth({
		"auth_id": auth_id,
		"auth_token": auth_token
		} appNumber=8897558700)
	code = p2fa.getVerificationCode(number, "Your verification code is __code__")  # String should be less than 160 chars
	r.setex("number:%s:code" % number, code, 60*15)  # Verification code is valid for 15 mins
	return jsonify({"status": "success", "message": "verification initiated"})