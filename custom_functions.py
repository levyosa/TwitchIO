from random import randint
import requests
import json
import os
from gtts import gTTS
from playsound import playsound




def limpar_msg(messsage_content):
    atributos = messsage_content.split(' ')
    return atributos
    
def perdi(ctx):
    print('perdi chamado')
    print(limpar_msg(ctx.message.content))
    return ctx.author.name+' perdeu o Jogo.'

def list_commands(ctx):
    print('list commands chamado')
    return('Commands: !sr, !perdi, !erro, !piada, !tcc ')

def conta_piada(ctx):
    print('piada chamado')
    response = requests.get('https://us-central1-kivson.cloudfunctions.net/charada-aleatoria', headers={ 'Accept': 'application/json'})
    piada = json.loads(response.content.decode('utf-8'))
    return(piada)

def falar(ctx):
    atributos = ctx.message.content
    fala = atributos.replace('!fala','')
    vozTTS(fala)

    
    
def tcc():
    vozTTS("E o TCC? Já fez, gajo?")
    pass

def mp3(file_name):
    os.system( "mpg321"+' ./mp3/'+file_name+'.mp3')

def vozTTS(fala):
    gttsobj = gTTS(text=fala, lang='pt-PT', slow=False)
    gttsobj.save("./mp3/ultimaFalaTwitch.mp3")
    os.system("mpg321 ./mp3/ultimaFalaTwitch.mp3") 
    



# def CMD(ctx):
#     print('CMD CALLED')
#     return('CMD REPLY')

