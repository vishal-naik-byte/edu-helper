#imports




from logging import WARNING, FileHandler,WARNING
from urllib import response
from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer
from train import *
from train1 import *
#from d.filterquestions import *
from getData import *



app = Flask(__name__)

File_Handler=FileHandler('errorlog.txt')
File_Handler.setLevel(WARNING)
#create chatbot
print("chatbot Starting...")
#read_only=True is a chatbot parameter for only read i removed that this is my note
chatbot = ChatBot("Edu-helper Chatbot", storage_adapter="chatterbot.storage.SQLStorageAdapter",logic_adapter=["chatterbot.logic.BestMatch",'chatterbot.logic.MathematicalEvaluation','chatterbot.logic.TimeLogicAdapter',{
            'import_path': 'chatterbot.logic.SpecificResponseAdapter',
            'input_text': 'Help me!',
            'output_text': 'Ok, here is a link: http://chatterbot.rtfd.org'
        }],preprocessors=['chatterbot.preprocessors.clean_whitespace'])
trainer = ChatterBotCorpusTrainer(chatbot)
#trainer.train("chatterbot.corpus.english") #train the chatter bot for english
trainer1 = ListTrainer(chatbot)
trainer1.train(data)
trainer1.train(data1)
trainer1.train(attendenceConvo)
trainer1.train(unrelateddata)

log_of_chat=['this','is','logs']
#define app routes
@app.route("/")
def index():
    return render_template("index1.html")

@app.route("/get")
#function for the bot response
def get_bot_response():
    userText = request.args.get('msg')
    log_of_chat.append(userText)
    print(str(log_of_chat))

    if userText == " ":
        return str("Please dont send blank messages")

    if userText[:8] == "rollno::" and (log_of_chat[-2] == 'ok what is your Roll No:? Format:rollno::xxxx' or log_of_chat[-2] == 'ok what is your Roll No:?Format:rollno::xxxx'):
        RollNo=userText[8:]
        attendence=get_Attendence(RollNo)
        return str(attendence)
    elif userText[:8] == "rollno::" and (log_of_chat[-2] != 'ok what is your Roll No: ? Format:rollno::xxxx' or log_of_chat[-2] != 'ok what is your Roll No:? Format:rollno::xxxx'):
        return str("Please first ask me to show your attendence")

#    elif userText not in filter:
#        return str("Sorry not in database!")

    bot_response=chatbot.get_response(userText)
    log_of_chat.append(str(bot_response))
    return str(bot_response)

if __name__ == "__main__":
    app.run()