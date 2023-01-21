import os
import discord
import random
from rich import print
import datetime as dt
from dotenv import load_dotenv
import pandas_datareader as web

BOT_USERNAME = "PythonBot"

client = discord.Client()
load_dotenv()
TOKEN = os.getenv('TOKEN')  # The private bot token stored in the .env file


def timestamp_now() -> str:
    """
    Returns current timestamp for the logger.
    Returns:
        str: Current timestamp formatted as HOUR:MINUTE:SECOND
    """
    now = dt.datetime.now()
    return f"{now.day:02d}/{now.month:02d}/{now.year:04d}-{now.hour:02d}:{now.minute:02d}:{now.second:02d}"

def get_stock_price(ticker) -> any:
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
async def on_message(message) -> None:    
    message.content = message.content.lower()
    if message.author == client.user:
        return
    
    print(f"{timestamp_now()} - Got a message from:\nUser ID : {message.author.id}\nUsername : {message.author.name}\nContent : {message.content}\n\n")
    if message.content.startswith('$hello'):
        await message.channel.send("Hey there! BLEEP BLOOP")
    elif message.content.startswith('$stockprice'):
        if len(message.content.split(" ")) == 2:
            ticker = message.content.split(" ")[1]
            price = get_stock_price(ticker)
            if price != "notfound":
                await message.channel.send(f"Stock price of {ticker} is {round(float(price), 3)} $")
            else:
                await message.channel.send("Stock price not found...")
        else:
            await message.channel.send("Wrong use of $stockprice\nFor more help type $help")
    elif message.content.startswith('$random'):
        if len(message.content.split(" ")) == 3:
            try:
                num1 = int(message.content.split(" ")[1])
                num2 = int(message.content.split(" ")[2])
                rand_number = random.randrange(min(num1, num2), max(num1, num2))
                await message.channel.send(f"The random number is {rand_number}")
            except ValueError:
                await message.channel.send("Wrong use of $random\nFor more help type $help")
        else:
            await message.channel.send("Wrong use of $random - you need to give me 2 numbers...\nFor more help type $help")
    elif message.content.startswith('$help'):
        await message.channel.send(get_help_string())
    elif message.content.startswith('$'):
        await message.channel.send("Type $help for help")
    


def get_help_string() -> str:
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
async def on_connect() -> None:
    print(f"{timestamp_now()} - Bot connected to the server as:\nName: {client.user.name}\nID: {client.user.id}\n")


client.run(TOKEN)