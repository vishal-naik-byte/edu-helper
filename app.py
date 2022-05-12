#imports



from logging import WARNING, FileHandler,WARNING
from urllib import response
from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer
from registeration import *
from train import *
from train1 import *
from getData import *
from registeration import *



app = Flask(__name__)

File_Handler=FileHandler('errorlog.txt')
File_Handler.setLevel(WARNING)
#create chatbot
print("chatbot Starting...")
#read_only=True is a chatbot parameter for only read i have removed that this is my note
chatbot = ChatBot("Edu-helper Chatbot", storage_adapter="chatterbot.storage.SQLStorageAdapter",
            logic_adapter=["chatterbot.logic.BestMatch",'chatterbot.logic.MathematicalEvaluation',
            'chatterbot.logic.TimeLogicAdapter',{
        }],preprocessors=['chatterbot.preprocessors.clean_whitespace'])
trainer = ChatterBotCorpusTrainer(chatbot)
#trainer.train("chatterbot.corpus.english") #train the chatter bot for english

trainer1 = ListTrainer(chatbot)
trainer1.train(data)
trainer1.train(data1)
trainer1.train(attendenceConvo)
trainer1.train(unrelateddata)
trainer1.train(resultConvo)
trainer1.train(noticeConvo)
trainer1.train(ExamTimetable)
#trainer1.train(data_of_human)



combined_data=data+data1+attendenceConvo+resultConvo+noticeConvo+ExamTimetable+unrelateddata+data_of_human

limit=True

log_of_chat=['this','is','logs']
#define app routes
@app.route("/")
def index1():
    return render_template("index.html")

@app.route("/bot")
def bot():
    return render_template("index3.html")

@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/forgot")
def forgot():
    return render_template("forgot.html")

@app.route("/reset")
def reset():
    return render_template("reset.html")

@app.route("/about_us")
def about_us():
    return render_template("about_us.html")

@app.route("/cources")
def cources():
    return render_template("cources.html")

@app.route("/blog")
def blog():
    return render_template("blog.html")

@app.route("/contact_us")
def contact_us():
    return render_template("contact_us.html")

@app.route('/register', methods =['GET', 'POST'])
def register_data():
    if request.method == 'POST' and 'name' in request.form and 'email' in request.form and 'password' in request.form:
        name=request.form['name']
        email=request.form['email']
        password=request.form['password']
        print(email)
        print(password)
        print(name)
        post_data=postData(name,email,password)
        print(post_data)
        if post_data:
            msg01="Registration Completed"
            return render_template('register.html')
        

@app.route('/login', methods =['GET', 'POST'])
def check_login_details():
    if request.method == 'POST' and 'email' in request.form and 'password' in request.form:
        email=request.form['email']
        password=request.form['password']
        print(email)
        print(password)
        check_data=check_login(email,password)
        if check_data:
            return render_template('index1.html')

@app.route("/get")
#function for the bot response
def get_bot_response():
    userText = request.args.get('msg')
    userText = userText.lower()
    print(userText)
    userText = userText.replace("?","")
    striper=userText.strip()
    splitter=striper.split(" ")
    print(splitter)

    if 'gmfc' in splitter and 'email' in splitter:
        userText="gmfc email"
    elif 'gmfc' in splitter and 'website' in splitter:
        userText="gmfc website"
    elif 'attendence' in splitter or 'attendance' in splitter or 'attandance' in splitter:
        userText = "show my attendence"
    elif 'notice' in splitter:
        userText = "notice"
    elif 'result' in splitter:
        userText = "result"
    elif 'timetable' in splitter or ('examination' in splitter and 'timetable' in splitter):
        userText = "examination timetable"
    elif 'your' in splitter and 'name' in splitter:
        userText = "what is your name"
    elif 'help' in splitter or 'info' in splitter or 'more' in splitter:
        userText = "help"
    elif 'courses' in splitter:
        userText = "courses"
    elif 'hi' in splitter or 'hi' in splitter or 'hii' in splitter or 'hiii' in splitter:
        userText = "hi"
    
    print(userText)

    if limit==True:
        log_of_chat.append(userText)
        print(str(log_of_chat))
        if userText == " ":
            return str("Please dont send blank messages")
        
        if userText[:11] == "complaint::":
            complaint_message=userText[11:]
            file1=open("complaint.txt","a")
            file1.write(complaint_message+"\n")
            file1.close()
            return str("Thank you your complaint is registered")

        if userText[:11] == "att:rollno:":
            RollNo=userText[11:]
            attendence=get_Attendence(RollNo)
            return str(attendence)
        
        if userText[:14] == "result:rollno:":
            RollNo=userText[14:]
            result=get_Result(RollNo)
            return str(result)

        if userText not in combined_data:
            if userText.capitalize() not in combined_data:
                #return str("If you giving new input than its good but first get the permission to add your new input")
                user_message=userText
                file2=open("user_did_not_get_answer.txt","a")
                file2.write(user_message+"\n")
                file2.close()
                return str("This type of input is not present in our database so i din't understand it")


        bot_response=chatbot.get_response(userText)

        if bot_response in not_to_reply:
            return str("If this input is correct than Sorry i am still learning")
        log_of_chat.append(str(bot_response))
        return str(bot_response)
    else:
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


        bot_response=chatbot.get_response(userText)
        if bot_response in not_to_reply:
            return str("If this input is correct than Sorry i am still learning")
        log_of_chat.append(str(bot_response))
        return str(bot_response)



if __name__ == "__main__":
    app.run()