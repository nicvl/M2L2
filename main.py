import discord
from discord.ext import commands
import random
from dotenv import load_dotenv
import os

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()

bot = commands.Bot(command_prefix="$", intents=intents)

@bot.event
async def on_ready():
    print(f"El bot inicio sesión como:{bot.user}")

consejos = [
        "Apaga las luces cuando salgas de una habitación.",
        "Usa bolsas reutilizables.",
        "Evita usar botellas de plástico.",
        "Recicla papel, vidrio y plástico.",
        "Evita dejar los aparatos enchufados si no los usas."
    ]

objetos = {
        "botella": "🍼 Una botella de plástico tarda hasta **450 años** en desaparecer. ¡Increíble, ¿no?! 😱",
        "chicle": "🍬 El chicle que tirás al suelo tarda **5 años** en degradarse... ¡mejor usar el tacho! 🗑️",
        "lata": "🥫 Una lata de aluminio puede estar **200 años** dando vueltas por ahí... 😬",
        "papel": "📄 Buenas noticias: el papel tarda solo **2 a 6 semanas**. ¡Reciclalo igual! ♻️",
        "pañal": "👶 Los pañales descartables tardan hasta **500 años**... 😨 Mejor si podés usar opciones reutilizables.",
        "colilla": "🚬 Una colilla de cigarro tarda **10 años**. ¡Nunca la tires al piso! 🌱"
    }

@bot.command()
async def consejo(ctx):
    await ctx.send(random.choice(consejos))

@bot.command()
async def degradacion(ctx, objeto, str):
    objeto = objeto.lower()

    if objeto in objetos:
        await ctx.send(objetos[objeto])
    else:
        await ctx.send("No se cuanto trada en degradrse este objeto")

bot.run(TOKEN)
    
