from django.core.exceptions import ObjectDoesNotExist
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import phoneModel
import requests

class getPhoneNumberRegistered(APIView):
# Get to Create a call for OTP
    @staticmethod
    def get(request, phone):
        global msg, response
        msg = "false"
        try:
            Mobile = phoneModel.objects.get(Mobile=phone)  # if Mobile already exist alert
            return Response({"exist":"true"} , status=409)
        except ObjectDoesNotExist:
            # Using Multi-Threading send the OTP Using Messaging Services like Twilio or Fast2sms
            url = "https://gurubrahma-smsly-sms-to-india-v1.p.rapidapi.com/otp/generate/"+str(phone)

            querystring = {"getOTP":"true","duration":"100","digits":"5","message":"Your LobPay verification code is OTP_VALUE"}

            headers = {
                'x-rapidapi-host': "gurubrahma-smsly-sms-to-india-v1.p.rapidapi.com",
                'x-rapidapi-key': "a8e07551f2msh8f97f4821a0a0c5p1afdbbjsn23fb1d0d27ed"
            }

            response = requests.request("GET", url, headers=headers, params=querystring)
            if 'errorCode' in response.json():
                msg = "false"
            else:
                msg = "true"
        return Response({"success":msg} , status=200)

    # This Method verifies the OTP
    @staticmethod
    def post(request, phone):
        OTP = response.json()["OTP"]
        if ('otp' in request.data) and (OTP == request.data["otp"]):  # Verifying the OTP
            return Response({"verified":"true"}, status=200)
        return Response({"verified":"false"}, status=400)

class getMerchantRegistered(APIView):
    @staticmethod
    def post(request):
        OTP = response.json()["OTP"]
        if ('otp' in request.data) and (OTP == request.data["otp"]):  # Verifying the OTP
            return Response({"verified":"true"}, status=200)
        return Response({"verified":"false"}, status=400)
