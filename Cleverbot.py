import re
import cleverbot
import traceback

WORDS = ["CLEVERBOT", "BOT"]
PATTERN = r"\b(cleverbot|bot)\b"

def handle(text, mic, profile):
    """
        Responds to user-input, typically speech text, starting a conversation with cleverbot

        Arguments:
        text -- user-input, typically transcribed speech
        mic -- used to interact with the user (for both input and output)
        profile -- contains information related to the user (e.g., phone number)
    """
    mic.say('Starting clever bot')
    exit = False
    bot = cleverbot.Cleverbot()
    errors = 0
    while not exit:
        try:
            question = mic.activeListen()
            if is_exit(question):
                break
            answer = bot.ask(question)
            mic.say(answer)
        except Exception as e:
          mic.say('Oops')
          print traceback.format_exc()
          errors += 1
          if errors > 5:
              break

    mic.say('Stopping clever bot')


def is_exit(text):
    return bool(re.search(r"(exit|quit|stop)", text, re.IGNORECASE))

def isValid(text):
    return bool(re.search(PATTERN, text, re.IGNORECASE))
