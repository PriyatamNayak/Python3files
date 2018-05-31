# -*- coding: utf-8 -*-
"""
Created on Tue May 22 12:28:32 2018

@author: Amit
"""

# =============================================================================
#                               1. echo bot 
# =============================================================================
bot_template = "Bot: {0}"
user_template = "User: {0}"

# def respond(message):
#     bot_message = "hii, you said " + message
#     return bot_message
# 
# def send_message(message):
#     print(user_template.format(message))
#     response = respond(message)
#     print(bot_template.format(response))
#     
# send_message("hello")
# 
# =============================================================================
#                               2. chitchat 
# =============================================================================
name = "Amit"
weather = "hot"

# time = "not so good may be"
# 
# responses = {
#         "what is your name?": "My name is {0}".format(name),
#         "How's the weather?": "It's {0}".format(weather),
#         "what's going on?":"{0}".format(time),
#         "default":"Don't no why i can't answer this... "
#         }
# 
# def respond(message):
#     if message in responses:
#         bot_message = responses[message]
#     else:
#         bot_message = responses["default"]
#     return bot_message
# 
# def send_message(message):
#     print(user_template.format(message))
#     response = respond(message)
#     print(bot_template.format(response))
#
#send message("what is your name?")
#
# =============================================================================
#                      3. chitchat with random answers
# =============================================================================

import random

# Define a dictionary containing a list of responses for each message
# responses = {
#   "what's your name?": [
#       "my name is {0}".format(name),
#       "they call me {0}".format(name),
#       "I go by {0}".format(name)
#    ],
#   "what's today's weather?": [
#       "the weather is {0}".format(weather),
#       "it's {0} today".format(weather)
#     ],
#   "default": ["default message"]
# }
# 
# # Use random.choice() to choose a matching response
# def respond(message):
#     # Check if the message is in the responses
#     if message in responses:
#         # Return a random matching response
#         bot_message = random.choice(responses[message])
#     else:
#         # Return a random "default" response
#         bot_message = random.choice(responses["default"])
#     return bot_message
# 
# def send_message(message):
#     print(user_template.format(message))
#     response = respond(message)
#     print(bot_template.format(response))
#
#send message("what's your name?")
#send message("what's your name?")
#send message("what's your name?")
#
# =============================================================================
#               4. ELIZA 1: asking Questions
# =============================================================================

# import random
# 
# responses = {
#         "question":["I don't know :(", 
#                     "you tell me!"
#                    ],
#         "statement":["tell me more!",
#                      "why do you think that?",
#                      "how long have you felt this way?",
#                      "I find that extremely interesting",
#                      "can you back that up?",
#                      "oh wow!",
#                      ":)"
#                     ],
#         "default":["sorry ,don't know about it",
#                    "it's not our business",
#                   ]
#             }
# 
# 
# def respond(message):
#     # Check for a question mark
#     if message.endswith('?'):
#         # Return a random question
#         return random.choice(responses["question"])
#     # Return a random statement
#     return random.choice(responses["statement"])
# 
# def send_message(message):
#     print(user_template.format(message))
#     response = respond(message)
#     print(bot_template.format(response))
# 
# send_message("what's today's weather?")
# send_message("what's today's weather?")


# =============================================================================
#                    5. ELIZA II :Extracting key phrases
# =============================================================================

# import re
# rules = { 'I want (.*)': ['What would it mean if you got {0}',
#                         'Why do you want {0}',
#                         "What's stopping you from getting {0}"],
#           'do you remember (.*)': ['Did you think I would forget {0}',
#                                "Why haven't you been able to forget {0}",
#                                "What about {0}",
#                                'Yes .. and?'],
#           'do you think (.*)': ['if {0}? Absolutely.', 'No chance'],
#           'if (.*)': ["Do you really think it's likely that {0}",
#                       'Do you wish that {0}',
#                       'What do you think about {0}',
#                       'Really--if {0}']
#         }
# # Define match_rule()
# def match_rule(rules, message):
#     response, phrase = "default", None
#     
#     # Iterate over the rules dictionary
#     for pattern, responses in rules.items():
#         # Create a match object
#         match = re.search(pattern,message)
#         if match is not None:
#             # Choose a random response
#             response = random.choice(responses)
#             if '{0}' in response:
#                 phrase = match.group(1)
#     # Return the response and phrase
#     return response, phrase
# 
# # Test match_rule
# print(match_rule(rules, "do you remember your last birthday"))
# 
# =============================================================================
#                       6. ELIZA IV: pronouns
# =============================================================================

# import re
# 
# # Define replace_pronouns()
# def replace_pronouns(message):
# 
#     message = message.lower()
#     if 'me' in message:
#         # Replace 'me' with 'you'
#         return re.sub('me','you', message)
#     if 'my' in message:
#         # Replace 'my' with 'your'
#         return re.sub('my','your', message)
#     if 'your' in message:
#         # Replace 'your' with 'my'
#         return re.sub('your','my', message)
#     if 'your' in message:
#         # Replace 'your' with 'our'
#         return re.sub('your','our', message)
#     if 'you' in message:
#         # Replace 'you' with 'I'
#         return re.sub('you','I', message)
#     if 'our' in message:
#         # Replace 'our' with 'your'
#         return re.sub('our','your', message)
#     if 'your' in message:
#         # Replace 'your' with 'mine'
#         return re.sub('your','mine', message)
#     if 'mine' in message:
#         # Replace 'mine' with 'your'
#         return re.sub('mine','your', message)
#     if 'i' in message:
#         # Replace 'I' with 'you'
#         return re.sub('i','you', message)
#     
#     return message
# 
# print(replace_pronouns("my last birthday"))
# print(replace_pronouns("when you went to Florida"))
# print(replace_pronouns("I am amit"))
#
# =============================================================================
#               7. ELIZA complete
# =============================================================================

import re
rules = { 'I want (.*)': ['What would it mean if you got {0}',
                         'Why do you want {0}',
                         "What's stopping you from getting {0}"],
           'do you remember (.*)': ['Did you think I would forget {0}',
                                "Why haven't you been able to forget {0}",
                                "What about {0}",
                                "Yes .. why?"],
           'do you think (.*)': ["if {0}? Absolutely.", "No chance"],
           'if (.*)': ["Do you really think it's likely that {0}",
                       "Do you wish that {0}",
                       "What do you think about {0}",
                       "Really--if {0}"]
         }
 # Define match_rule()  
def match_rule(rules, message):
    response, phrase = "default", None
     
     # Iterate over the rules dictionary
    for pattern, responses in rules.items():
         # Create a match object
        match = re.search(pattern,message)
        if match is not None:
             # Choose a random response
            response = random.choice(responses)
            if '{0}' in response:
                phrase = match.group(1)
     # Return the response and phrase
    return response, phrase
 
def replace_pronouns(message):
     message = message.lower()
     if 'me' in message:
         # Replace 'me' with 'you'
         return re.sub('me','you', message)
     if 'my' in message:
         # Replace 'my' with 'your'
         return re.sub('my','your', message)
     if 'your' in message:
         # Replace 'your' with 'my'
         return re.sub('your','my', message)
     if 'your' in message:
         # Replace 'your' with 'our'
         return re.sub('your','our', message)
     if 'you' in message:
         # Replace 'you' with 'I'
         return re.sub('you','I', message)
     if 'our' in message:
         # Replace 'our' with 'your'
         return re.sub('our','your', message)
     if 'your' in message:
         # Replace 'your' with 'mine'
         return re.sub('your','mine', message)
     if 'mine' in message:
         # Replace 'mine' with 'your'
         return re.sub('mine','your', message)

     return message


# Define respond()
def respond(message):
    # Call match_rule
    response, phrase = match_rule(rules, message)
    if '{0}' in response:
        # Replace the pronouns in the phrase
        phrase = replace_pronouns(phrase)
        # Include the phrase in the response
        response = response.format(phrase)
    return response

def send_message(message):
    print(user_template.format(message))
    response = respond(message)
    print(bot_template.format(response))


# Send the messages
send_message("do you remember your last birthday")
send_message("do you think humans should be worried about AI")
send_message("I want a robot friend")
send_message("what if you could be anything you wanted")
 