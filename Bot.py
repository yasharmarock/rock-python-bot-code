import discord
from discord.ext import commands
client = commands.Bot(command_prefix='rc ')


@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.idle, activity=discord.Activity(type=discord.ActivityType.listening, name="यश Rock"))
    print('We have logged in as {0.user}'.format(client))


def check(author):
    def inner_check(message):
        return message.author == author

    return inner_check
    # This line works the commands & all


@client.command()
async def hi(ctx):
    await ctx.send("Hello")


@client.command()
async def info(ctx):
    await ctx.send(embed=discord.Embed(title="Name:- ROCK", description="USER_NAME:- ROCK#1184 \nID:-790216138180263936 \nRegistered:- Sun, Dec 20, 2020 8:56 AM", color=0))


@client.command()
async def bot(ctx):
    await ctx.send(embed=discord.Embed(title="Hello I'm ROCK#1184 the discord bot", description="This command is in work in progress!", color=0))


@client.command()
async def ping(ctx):
    await ctx.send('Pong! {0}'.format(round(bot.latency, 1)))


@client.command()
async def game(ctx):
    await ctx.send(embed=discord.Embed(title="This is gonna be the boald title", description="This is gonna be the discorption", color=0))

    # This line is personal ping command to ping someone


@client.command()
async def pj(ctx, arc):
    if arc.lower() == "<@!743853026569355324>":
        await ctx.send(embed=discord.Embed(description="<@!743853026569355324><@!743853026569355324><@!743853026569355324><@!743853026569355324><@!743853026569355324><@!743853026569355324><@!743853026569355324><@!743853026569355324><@!743853026569355324><@!743853026569355324><@!743853026569355324><@!743853026569355324><@!743853026569355324><@!743853026569355324><@!743853026569355324><@!743853026569355324><@!743853026569355324><@!743853026569355324><@!743853026569355324><@!743853026569355324><@!743853026569355324><@!743853026569355324><@!743853026569355324><@!743853026569355324><@!743853026569355324><@!743853026569355324><@!743853026569355324><@!743853026569355324><@!743853026569355324><@!743853026569355324><@!743853026569355324><@!743853026569355324><@!743853026569355324><@!743853026569355324><@!743853026569355324><@!743853026569355324><@!743853026569355324><@!743853026569355324><@!743853026569355324><@!743853026569355324><@!743853026569355324><@!743853026569355324><@!743853026569355324><@!743853026569355324><@!743853026569355324><@!743853026569355324><@!743853026569355324><@!743853026569355324><@!743853026569355324><@!743853026569355324><@!743853026569355324><@!743853026569355324><@!743853026569355324><@!743853026569355324><@!743853026569355324><@!743853026569355324><@!743853026569355324><@!743853026569355324><@!743853026569355324><@!743853026569355324><@!743853026569355324><@!743853026569355324><@!743853026569355324><@!743853026569355324><@!743853026569355324><@!743853026569355324><@!743853026569355324><@!743853026569355324><@!743853026569355324><@!743853026569355324><@!743853026569355324><@!743853026569355324><@!743853026569355324><@!743853026569355324><@!743853026569355324><@!743853026569355324><@!743853026569355324><@!743853026569355324><@!743853026569355324><@!743853026569355324><@!743853026569355324><@!743853026569355324><@!743853026569355324><@!743853026569355324><@!743853026569355324><@!743853026569355324><@!743853026569355324><@!743853026569355324><@!743853026569355324><@!743853026569355324>", color=0))

        # This line makes all caps wrk on the bot


@client.event
async def on_message(message):
    message.content = message.content.lower()
    await client.process_commands(message)
    # This is the TOKEN to make bot work on

client.run('Bot_token_here')
