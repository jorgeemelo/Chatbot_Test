
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
from time import sleep

bot = ChatBot('Mark 01',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    database_uri='sqlite:///database.sqlite3',
    logic_adapters=[
        'chatterbot.logic.BestMatch',
        'chatterbot.logic.MathematicalEvaluation']
)

bot = ChatBot('Mark 01')

def botLoop():
    while True:
        try:
            resposta = bot.get_response(input("Usuario: "))
            if float(resposta.confidence) > 0.8:
                print("Mark 01: ", resposta)
            else:
                print("Mark 01: Não sei o que dizer sobre isso...")
        except(KeyboardInterrupt, EOFError, SystemExit):
            break

botLoop()
