from twilio.rest import TwilioRestClient
 
# Find these values at https://twilio.com/user/account
account_sid = 'AC25ef232740072dc660a9b676d9e5c992'
auth_token = 'ff5269d59167dedf051268d5ef3e4b91'
client = TwilioRestClient(account_sid, auth_token)
 
message = client.sms.messages.create(to="+16314134223", from_="+13473086943",
                                     body="Hello there!")