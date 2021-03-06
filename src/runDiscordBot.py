import os
import discord
import random
from dotenv import load_dotenv
import pandas_datareader as web

client = discord.Client()
load_dotenv()
TOKEN = os.getenv('TOKEN')  # The private bot token stored in the .env file


def get_stock_price(ticker):
    """
    Search for a stock price in yahoo and returns the price of the ticker
    """
    try:
        data = web.DataReader(ticker, 'yahoo')
        price = data['Close'].iloc[-1]
    except Exception:
        return "notfound"
    return price


@client.event
async def on_message(message):
    message.content = message.content.lower()
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send("Hey there! BLEEP BLOOP")
    if message.content.startswith('$stockprice'):
        if len(message.content.split(" ")) == 2:
            ticker = message.content.split(" ")[1]
            price = get_stock_price(ticker)
            if price != "notfound":
                await message.channel.send(f"Stock price of {ticker} is {round(float(price), 3)} $")
            else:
                await message.channel.send("Stock price not found...")
        else:
            await message.channel.send("Wrong use of $stockprice\nFor more help type $help")
    if message.content.startswith('$random'):
        if len(message.content.split(" ")) == 3:
            try:
                num1 = int(message.content.split(" ")[1])
                num2 = int(message.content.split(" ")[2])
                rand_number = random.randrange(min(num1, num2), max(num1, num2))
                await message.channel.send(f"The random number is {rand_number}")
            except ValueError:
                await message.channel.send("Wrong use of $random\nFor more help type $help")
        else:
            await message.channel.send("Wrong use of $random\nFor more help type $help")
    if message.content.startswith('$help'):
        await message.channel.send(get_help_string())


def get_help_string():
    """
    returns a help menu for the user
    """
    title = '========= Python Discord Bot ========='
    hello_help = 'Type $hello to say hello to the bot'
    random_help = 'Type $random to get a random number between the range specified'
    random_usage = '    usage: $random [NUM1] [NUM2]'
    stockprice_help = 'Type $stockprice to get a price of a stock'
    stockprice_example = '    usage: $stockprice TSLA -> return the stock price of tesla company'
    help_help = 'Type $help to view this menu'
    return f"```{title}\n\n{hello_help}\n{random_help}\n{random_usage}\n{stockprice_help}\n{stockprice_example}\n{help_help}```"

@client.event
async def on_connect():
    print("Bot connected to the server!")


client.run(TOKEN)