import requests
import json

class SmsAPI():
    
    def __init__(self, api_key:str, sender_id:int, callback_url: str=None):
        try:
            self.api_key =api_key
            self.sender_id = sender_id
        except Exception as error:
            pass
        

    def send_sms(self, recipient_number: str, message: str):
        try:
            url= "https://sms.blessedtexts.com/api/sms/v1/sendsms"
            payload = {
                "api_key": self.api_key,
                "sender_id": self.sender_id,
                "message": message,
                "phone": recipient_number
            }
            response = requests.post( url, json=payload)
            response.raise_for_status()
            response_data = response.json()

            if isinstance(response_data, list):
                response_data = response_data[0]


                if response_data.get("status_code") == "1000":
                    return {
                        "message_id": response_data.get("message_id"),
                        "cost": response_data.get("message_cost")
                    }
            else:
                print(response_data)
                return{"error": "unknown error" }
        except requests.exceptions.RequestException as error:
            return { "error": str(error)}
        except Exception as error:
            return { "error": str(error)}


    def send_bulk_sms(self, recipient_numbers: list, message: str):
        '''
            to be implemented
        '''
        try:
            pass
        except Exception as error:
            pass

    def credit_balance(self,):
        try:
            url = "https://sms.blessedtexts.com/api/sms/v1/credit-balance"
            payload ={
                "api_key": self.api_key
            }
            response = requests.post( url, json=payload )
            response = response.json()
            
            if response['status_code']==str(1000):
                return {"balance": response['balance'] }
        except requests.exceptions.RequestException as error:
            return { "error": str(error)}
        except Exception as error:
            return { "error": str(error)}



