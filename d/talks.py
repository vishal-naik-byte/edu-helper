from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
from train import train1

# Create a new chat bot named Charlie
chatbot = ChatBot(
    "My ChatterBot",
    logic_adapters=[
        {
            'import_path': 'chatterbot.logic.SpecificResponseAdapter',
            'input_text': 'Help me!',
            'output_text': 'Ok, here is a link: http://chatterbot.rtfd.org'
        },{
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'I am sorry, but I do not understand.',
            'maximum_similarity_threshold': 0.90
        }
    ]
)

trainer = ListTrainer(chatbot)

trainer1 = ChatterBotCorpusTrainer(chatbot)

trainer2 = ListTrainer(chatbot)

trainer.train([
    "hey",
    "hi",
    "How are you?",
    "I am good what about you?",
    "That is good to hear.",
    "ok",
    "ok",
    "Thank you",
    "You are welcome.",
])

trainer1.train(
    "chatterbot.corpus.english"
)

trainer2.train(train1)

#while True:
#    try:
#        user_input = input("You:")
#
#        bot_response = chatbot.get_response(user_input)
#
#        print("bot:",bot_response)
#
    # Press ctrl-c or ctrl-d on the keyboard to exit
#    except (KeyboardInterrupt, EOFError, SystemExit):
#        break
