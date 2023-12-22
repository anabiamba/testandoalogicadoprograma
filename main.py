#TODO: Importar as bibliotecas
from datetime import date, time, datetime
from datetime import datetime
import telebot
import time

# TODO: Definir a variavel chave API
CHAVE_API = "6823297602:AAErOFwPtF3ZTEdF10hN_qsHtb1yrVz5o-A"

# TODO: Conexão com o BOT
bot = telebot.TeleBot(CHAVE_API)

#TODO: Definição de hora
hora = time.localtime(time.time())

# TODO: Cumprimentos
if hora.tm_hour < 12:
    cumprimento = "Bom dia"
elif 12 <= hora.tm_hour < 18:
    cumprimento = "Boa tarde"
else:
    cumprimento = "Boa noite"

#TODO: Definições de Dicionario
clientes = {
    "DUAL": {'emergencia': True},
    "MXT": {'emergencia': False},
}

comercial = {
    "hora_inicial": 8,
    "hora_final": 17,
}

com_contrato = f'''OK
'''
sem_contrato = '''Chequei seu contrato e infelizmente você não possui atendimento emergencial fora do horário comercial.

Para abrir um chamado técnico 24h por dia, todos os dias da semana, utilize um de nossos canais de atendimento no endereço abaixo:

https://vmb.global/central-de-atendimento
'''


# hoje = date.today()
# weekend = True if date.weekday(hoje) >= 5 else False




#TODO: Função verificar mensagem
def verificar(mensagem):
    return True

#TODO: Função verificar final de semana
def final_de_semana():
    hoje = date.today().weekday()
    weekend = True if hoje >= 5 else False
    return weekend

#TODO: Função verificar horario comercial
def hora_comercial():
    hcomercial = True if hora.tm_hour >= comercial["hora_inicial"] and hora.tm_hour < comercial["hora_final"] else False
    return hcomercial

@bot.message_handler(func=verificar)
def responder(mensagem):

    # TODO: Nome do cliente e Empresa
    primeiro_nome = mensagem.from_user.first_name
    cliente = mensagem.chat.title
    user_id = mensagem.from_user.id

    mensagem2 = com_contrato if clientes[cliente]['emergencia'] == True else sem_contrato

    texto1 = f"""

    {cumprimento}, {primeiro_nome}! Eu sou o BOT da VMB Tecnologia, trabalho apenas fora do horário comercial.

    Aguarde que vou checar as opções que o contrato da {cliente} oferece para este horário:"""

    bot.reply_to(mensagem, texto1)
    time.sleep(10)

    if final_de_semana():
        if clientes[cliente]['emergencia'] == True:
            bot.reply_to(mensagem, f"{cliente} {mensagem2}")
        else:
            bot.reply_to(mensagem, f"{cliente} {mensagem2}")
    elif hora_comercial() == False:
        if clientes[cliente]['emergencia'] == True:
            bot.reply_to(mensagem, f"{cliente} {mensagem2}")
        else:
            bot.reply_to(mensagem, f"{cliente} {mensagem2}")
#TODO: Código não parar de executar
bot.polling()