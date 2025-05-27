# GranSuperviviente

[![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=fff)](#)

> 🧟 Bot de discord para poder controlar un servidor dedicado de Project Zomboid 

## Uso
El bot se usara mediante comandos que permitiran controlar el servidor dedicado

```
👶 Usuario : !start
🧟‍♂️ Bot : 🚀 Iniciando servidor.
👶 Usuario : !stop
🧟‍♂️ Bot : 🚩 Apagando servidor.
```

Comandos: 
```
!info // Informacion necesaria para unirse
!start // Iniciar servidor
!stop // Detener servidor
!restart // Reiniciar servidor
!players // Jugadores en linea
```

## Cosas a tener en cuenta
* [Aqui](link) Se encuentra el tutorial para crear el servidor dedicado.
* [Aqui](Link) Se encuentra el tutorial de la creacion de este Bot.
* Esta pensado para su uso en Windows, no fue probado en linux y seguro necesita modificaciones para ello.
* El script bot.py debera estar corriendo para poder hacer uso del granSuperviviente.

## Herramientas necesarias

* Tener instalado python y las dependencias necesarias.

Descarga de [python](https://www.python.org/downloads/) y dependencias

```shell
pip install --upgrade discord.py mcrcon
```

## EMPECEMOS! 🚀

* Generar [bot de discord](https://discord.com/developers/applications)

Una vez creado ir al menu Bot > Token y generar el token para el siguiente paso.

Tambien podemos ir al menu Installation, en Default Install Settings > Guild Install > Scope : agregar bot

 y en Default Install Settings > Guild Install > Permissions : agregar Administrador

Luego en Install Link podremos invitarlo a nuestro servidor de discord.

* Modificar bot.py : 
```Python
@bot.command()
async def info(ctx):
    await ctx.send("INFO DEL SERVER")
    await ctx.send("IP : ") # Nuestra IP publica
    await ctx.send("PORT : 16261")
    await ctx.send("Password : ") # Nuestra password
```

```Python
async def start(ctx):
    global server_process
    try:
        if server_process is not None and server_process.poll() is None:
            await ctx.send("⚠️ El servidor ya esta en funcionamiento.")
            return

        file_path = "C:\\pzserver\\StartServer64.bat"   # Path de StartServer
        server_process = subprocess.Popen([file_path], shell=True)
        await ctx.send("🚀 Iniciando servidor.")

    except Exception as e:
        await ctx.send(f"❌ Error al iniciar el servidor: {e}")
```

```Python
bot.run('tokenDeMiBot')
```
