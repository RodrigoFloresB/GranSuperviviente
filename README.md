# GranSuperviviente

[![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=fff)](#)

> 🧟 Bot de discord para poder controlar un servidor dedicado de Project Zomboid.

## Tutorial Completo (servidor dedicado + bot de discord)
* [Link Aqui]() Tutorial completo en Youtube.
* [Comandos](Server.md) Usados para la creacion del servidor.


## Uso
El bot se usara mediante comandos que permitiran controlar el servidor dedicado.

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
* ~~[Aqui](https://www.youtube.com/watch?v=sGcSKe5olWA) Se encuentra una explacion respecto al servidor dedicado (Old).~~
* ~~[Aqui](https://www.youtube.com/watch?v=QujGCG4VMvU) Se encuentra el tutorial de la creacion de este Bot (Old).~~
* Esta pensado para su uso en Windows, no fue probado en linux y seguro necesita modificaciones para ello.
* El script granSuperviviente.py debera estar corriendo para poder hacer uso del granSuperviviente.

## Herramientas necesarias
* Preferentemente usar algun editor de codigo.
* Tener instalado python y las dependencias necesarias.

Descarga de [python](https://www.python.org/downloads/) y dependencias.

```shell
pip install --upgrade discord.py mcrcon
```

## EMPECEMOS! 🚀

* Generar [bot de discord](https://discord.com/developers/applications)
Una vez creado el bot :

Ir al menu *Installation*, en *Default Install Settings > Guild Install > Scope* : agregar bot

y en *Default Install Settings > Guild Install > Permissions* : agregar Administrador.

Luego en *Install Link* podremos invitarlo a nuestro servidor de discord.

Ir al menu *Bot > Token* y generar el token para el siguiente paso.

Tambien en el menu *Bot > Privileged Gateway Intents > Message Content Intent* : Activar esta opcion.

* Modificar granSuperviviente.py : 
```Python
# ---- Configs ----
passwordServer = "" 
passwordRcon = ""   
filePatch = ""
publicIP = ""
token = ''
```