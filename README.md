# Discord Bot
- A simple discord bot using the `discord.py` API
- I will also show you how to host the bot on a raspberry pi

## Discord API Setup

- Go to `discord.com/Developers`
- Create a new application and click on "Add bot"
- Go to "Bot" in settings
- Give him permissions to read & send messages
- Reveal your private token and save it
- Put it in a `.env` file in `src/` folder  

## Python Setup

- Install Python 3.8
- Install the pip packages:

    `pip install -r requirements.txt`

- Run the script:
    
    `python runDiscordBot.py`

- Wait for the message : `Bot connected to the server!`
- Then you should see your bot online in your discord server

## Bot features
```
Type $hello to say hello to the bot
Type $random to get a random number between the range specified
    usage: $random [NUM1] [NUM2]
Type $stockprice to get a price of a stock
    usage: $stockprice TSLA -> stock price of Tesla company
Type $help to view this menu
```

## Host the bot on a Raspberry Pi

- Set up a raspberry pi with the raspbian OS
- Connect the raspberry pi to the internet with RJ45 or wifi (save password!)
- Edit the rc.local file to run the script so when the pi boots up it will automatically run the script:
    
    `sudo nano /etc/rc.local`
- Add a line above the `exit 0` command that runs the script (with the full path):

    `python3 /home/pi/src/runDiscordBot.py &`

- Now you can reboot the raspberry pi:

    `sudo reboot`

- The bot will be online after reboot

## Optional - Connect to the Raspberry Pi with SSH
- If you give the pi power and just connect it to the internet you don't have any control of it 
- SSH will be a good solution 
- Get your raspberry pi IP address (or set it static)
- Enable SSH in the raspberry pi configuraion under `Interfacees` tab
- Connect it from your computer:

    `ssh pi@192.168.XXX.XXX`
- Enter your pi password
- Now you have a full control of your pi

### Enjoy the bot!
© 2021 Daniel Kirshner. All rights reserved.
