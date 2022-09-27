from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
app = Flask(__name__)
#create chatbot
# bot = ChatBot('Buddy', read_only = True)
englishBot = ChatBot("Chatterbot", storage_adapter="chatterbot.storage.SQLStorageAdapter")
trainer = ChatterBotCorpusTrainer(englishBot)
trainer.train("chatterbot.corpus.english") #train the chatter bot for english
# trainer = ListTrainer(bot)
# trainer.train([
#     "Hi, can I help you",
#     "Who are you?",
#     "I am your virtual assistant. Ask me any questions...",
#     "Where do you operate?",
#     "We operate from Singapore",
#     "What payment methods do you accept?",
#     "We accept debit cards and major credit cards",
#     "I would like to speak to your customer service agent",
#     "please call +65 3333 3333. Our operating hours are from 9am to 5pm, Monday to Friday"
#
# ])
# trainer.train([
#     "What payment methods do you offer?",
#     "We accept debit cards and major credit cards",
#     "How to contact customer service agent",
#     "please call +65 3333 3333. Our operating hours are from 9am to 5pm, Monday to Friday"
#
# ])





#define app routes
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get")
#function for the bot response
def get_bot_response():
    userText = request.args.get('msg')
    return str(englishBot.get_response(userText))

if __name__ == "__main__":
    app.run()