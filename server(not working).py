from flask import Flask, request

app = (__name__)

FB_API_URL = "https://graph.facebook.com/v2.6/me/messages"
VERIFY_URL = ""
PAGE_ACCESS_TOKEN = "EAADpMcQ7tPUBAOr3mZAfZC4xYw2pP5DKQibb6zgRvw1oEiMByZAPZARrTVp0VqZAg1e52rfw3y1Ru5kDRL6Gbtpq9CvZA44ZAKDIHJWrelWfOH7ByZAQs6U9UZB9j4ip0D9qHAaJUcJXJC52Vwrs5X9qgqO9m91X0JGdnY5aAwFn8Hs0voIJoRXRE"

def get_bot_response(message):
	return "This is a dummy response to {}".format(message)

def verify_webhook(req):
	if req.args.get("hub.verify_token")== VERIFY_TOKEN:
		return req.args.get("hub.challenge")
	else:
		return "incorrect"

def respond(sender, message):
	response = get_bot_response(message)
	send_message(sender, response)

def is_user_message(message):
	return (message.get("message") and
            message["message"].get("text") and
            not message["message"].get("is_echo"))

@app.route("/webhook")
def listen():
	if request.method == "GET":
		return verify_webhook(request)

	if request.method == "POST":
		payload = request.json
		event = payload["entry"][0]["messaging"]
		for x in event:
			if is_user_message(x):
				text = x["message"]["text"]
				sender_id = x["sender"]["id"]
				respond(sender_id, text)
		
		return "ok"

def send_message(recipient_id, text):
	payload = {
		"message" : {"text":text},
		"recipient": {"id":recipient_id},
		"notification_type": "regular"
	}

	auth = {
		"access_token":PAGE_ACCESS_TOKEN
	}

	response =requests.post(
		FB_API_URL, params = auth, json = payload
	)
	
	return response.json()
	

