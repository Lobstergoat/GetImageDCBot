import os
import discord

from selenium import webdriver
import time, requests
from selenium.webdriver.chrome.options import Options

from dotenv import load_dotenv
from discord.ext import commands
from discord.ext.commands import Bot

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

bot = commands.Bot(command_prefix='>')

@bot.event
async def on_ready():
    for guild in bot.guilds:
        if guild.name == GUILD:
            break

    print(
        '\n'
        f'{bot.user} is connected to the following server:\n'
        f'{guild.name}(id: {guild.id})\n'
        ' -- Bot Ready -- '
    )

global on
on = False

@bot.event
async def on_message(message):
    global on
    input_words = message.content.lower().split()
    author = message.author

    if on == True:
        if message.content == ">stop":
            await message.channel.send('I Have Stopped')
            on = False
            print("Stopped")
        elif author == bot.user:
            return 
        elif message.content.lower() in ["liam neeson pees his pants", "liam neeson pisses his pants", "liam neeson urinates his pants", "Liam neeson pisses his pants", "liamneesonpeeshispants"]:
            kick(message.author)
            while True:
                time.sleep(1)
                msg = await message.author.send("Liam neeson does NOT pee his pants")
        elif message.content == message.content:
            await message.channel.send(message.content)
  
    elif message.content == ">begin":
        await message.channel.send('I Have Begun')
        print("Begun")
        on = True

    await bot.process_commands(message)

@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(member):
    await bot.kick(member)

@bot.command(name='bwa')
async def bwa(ctx):
    print("Spam begun")

    while True:
        time.sleep(1)
        msg = await ctx.author.send("Shut up")

@bot.command(name='find')
async def find(ctx):

    print("")
    print("searching for:",ctx.message.content[6:])
    await ctx.send("One second, grabbing the image...")

    options = Options()
    options.headless = True
    browser = webdriver.Chrome(options=options, executable_path="D:\Program Files (x86)\chromedriver.exe")

    search_url = f"https://www.google.com/search?site=&tbm=isch&source=hp&biw=1873&bih=990&q={ctx.message.content[6:]}"
    browser.get(search_url)

    elements = browser.find_elements_by_class_name('rg_i')

    count = 0
    for e in elements:
        e.click()
        time.sleep(1)
        element = browser.find_elements_by_class_name('v4dQwb')

        if count == 0:
            big_img = element[0].find_element_by_class_name('n3VNCb')
        else:
            big_img = element[1].find_element_by_class_name('n3VNCb')

        image_url = big_img.get_attribute("src")

        count += 1
        if count == 1:
            break
    try:    
        await ctx.send(image_url)
    except:
        await ctx.send("Cannot send this image beacuse the image link is longer than 2000 characters")
        
    print()
    print("Image found and printed")

bot.run(TOKEN)
