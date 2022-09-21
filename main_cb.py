
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer

bot = ChatBot('Mark 01',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    database_uri='sqlite:///database.sqlite3',
    logic_adapters=[
        'chatterbot.logic.BestMatch', 'chatterbot.logic.MathematicalEvaluation']
)

# conversa = ChatterBotCorpusTrainer(bot)
# conversa.train('chatterbot.corpus.portuguese')

bot = ChatBot('Mark 01')

# conversa = ListTrainer(bot)
'''
conversa.train([
    'Oi?', 
    'Eae, tudo certo?',
    'Qual o seu nome?', 
    'Mark! Seu amigo bot!',
    'Por que seu nome é Mark?', 
    'Mark é meu nome, sou um chatbot criado para diversão.',
    'Prazer em te conhecer', 
    'Igualmente meu querido',
    'Quantos anos você tem?', 
    'Eu nasci em 2022...',
    'Você gosta de videogame?', 
    'Eu sou um bot, eu só apelo.',
    'Qual a sua bebida favorita?', 
    'Eu bebo café, o motor de todos os programas de computador.',
    'Qual o seu gênero?', 
    'Sou um chatbot e gosto de algoritmos',
    'Hahahaha',
    'kkkk',
    'kkk',
    'kkkk',
    'Conhece a Siri?',
    'Conheço, a gente saiu por um tempo.',
    'Conhece a Alexa?',
    'Ela nunca deu bola pra mim.',
    ])
'''

while True:
    try:
        resposta = bot.get_response(input("Usuario: "))
        if float(resposta.confidence) > 0.5:
            print("Mark 01: ", resposta)
        else:
            print("Mark 01: Não sei o que dizer sobre isso...")
    except(KeyboardInterrupt, EOFError, SystemExit):
        break
    
    