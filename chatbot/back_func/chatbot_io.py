import chatterbot
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from back_func import dict

bot = ChatBot(
    'Norman',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    database_uri='sqlite:///database.sqlite3'
)

trainer = ListTrainer(bot)

x = trainer.train([
    'How are you?',
    'I am good.',
    'That is good to hear.',
    'Thank you',
    'You are welcome.',
    'Bye',
    'Have a Good Day',
    'Hi',
    'Hello'
])

y = trainer.train(dict.L)
def working(a):
    ans = bot.get_response(a)
    return ans

# This is your Python script

# Assume you have a Python variable that you want to pass to the JavaScript file
# Now you can open the HTML file in a web browser, and it will execute the JavaScript code with the Python variable
