from twitchio.ext import commands
from config import *
from custom_functions import *
from time import sleep

class Bot(commands.Bot):

    def __init__(self):
        super().__init__(irc_token=TOKEN, client_id=NICK, nick=NICK, prefix='!',
                         initial_channels=[CHANNEL])

    # Events don't need decorators when subclassed
    async def event_ready(self):
        print(f'Ready | {self.nick}')

    @commands.command(name='perdi')
    async def perdi_command(self, ctx):
        await ctx.send(perdi(ctx))

    @commands.command(name='commands')
    async def list_commands(self,ctx):
        await ctx.send(list_commands(ctx))

    @commands.command(name='piada')
    async def conta_piada(self,ctx):
        await ctx.send("(TiozãoBot) ->"+"perai, fi")
        piada = conta_piada(ctx)
        await ctx.send("(TiozãoBot) ->"+piada['pergunta'])
        sleep(20)
        await ctx.send("(TiozãoBot) ->"+piada['resposta'])

    @commands.command(name='fala')
    async def fala(self,ctx):
        falar(ctx)

    @commands.command(name='tcc')
    async def tcc(self,ctx):
        tcc()
    

    @commands.command(name='betocarrero')
    async def bc(self,ctx):
        mp3("beto-carrero")

    @commands.command(name='cabecada')
    async def cabecada(self,ctx):
        mp3("cabecada")

    @commands.command(name='erro')
    async def err(self,ctx):
        mp3("faustao-errou")
    

bot = Bot()
bot.run()






# @commands.command(name='CMD')
#     async def CMD_command(self, ctx):
#         await ctx.send(CMD(ctx))