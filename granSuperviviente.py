from discord.ext import commands
from mcrcon import MCRcon
import asyncio
import subprocess
import discord


# Definir los intents requeridos
intents = discord.Intents.default()
intents.message_content = True
server_process = None

# Crear el bot con prefix "!"
bot = commands.Bot(command_prefix='!', intents=intents)

# Comandos
@bot.command()
async def info(ctx):
    await ctx.send("INFO DEL SERVER")
    await ctx.send("IP : Mi ip") # Mi IP
    await ctx.send("PORT : 16261")
    await ctx.send("Password : demo") # Password del servidor

@bot.command()
async def start(ctx):
    global server_process
    try:
        if server_process is not None and server_process.poll() is None:
            await ctx.send("⚠️ El servidor ya esta en funcionamiento.")
            return

        file_path = "C:\\pzserver\\StartServer64.bat"   # Ruta del ejecutable del servidor
        server_process = subprocess.Popen([file_path], shell=True)
        await ctx.send("🚀 Iniciando servidor.")

    except Exception as e:
        await ctx.send(f"❌ Error al iniciar el servidor: {e}")

@bot.command()
async def stop(ctx):
    global server_process
    try:
        if server_process is not None and server_process.poll() is None:
            server_process.terminate()
            await ctx.send("🚩 Apagando servidor.")
        else:
            await ctx.send("⚠️ El servidor no esta en ejecucion.")

    except Exception as e:
        await ctx.send(f"❌ Error al detener el servidor: {e}")

@bot.command()
async def restart(ctx):
    await ctx.send("🔁 Reiniciando el servidor...")
    await stop(ctx)
    await asyncio.sleep(15)  # Espera un poco antes de volver a iniciar
    await start(ctx)

@bot.command()
async def players(ctx):
    host = "127.0.0.1"
    port = 27015
    password = "4356"

    try:
        with MCRcon(host, password, port) as mcr:
            response = mcr.command("players")
            await ctx.send(f"👥 Jugadores conectados:\n{response}")
    except Exception as e:
        await ctx.send(f"❌ Error al consultar jugadores: {e}")


# Token
bot.run('') # Token generado por el bot