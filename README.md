# clip-and-tweet
This was created to be run on a Stream Deck, by using the launch application feature.  Create a button that launches the clipandtweet.exe  The application will close once it's completed so that multiple instances do not occur. No performance hit has been noticed while using while live on stream.

Other ways of running the script have not been tested, but should be equally as viable, and we're interested to see what you come up with!

# Setup
This script was made using Python 3.8.2.  If you do not have Python it can be found at https://www.python.org/
You'll also need to download Requests https://pypi.org/project/requests/ which can be installed through pip.  After you've installed Python, open command prompt and type 'pip install requests' to download.
And Tweepy http://docs.tweepy.org/en/latest/install.html which can be installed through pip the same way by using 'pip install tweepy'
The final part I used to make it into an executable file is PyInstaller https://pypi.org/project/PyInstaller/ by using 'pip install pyinstaller'

After you've acquired all of these pieces you can create the executable file by going to the folder containing the script in command prompt and typing 'pyinstaller --onefile clipandtweet.py' 
After a brief moment it will create several files and folders but you will find the finished exe file in the 'dist' folder which will be created where you ran the compiler.

This script will require an app from Twitch to access a Client-ID (I've provided one) which you can make your own at
https://dev.twitch.tv/console/apps
and that you create an app on Twitter for access to the necessary keys to send messages
https://developer.twitter.com/en/apps

If you want to use the script as is you'll need to create a text file called "login_info.txt" as well as "tweet_messages.txt" with the following information.  Each number represents a new line created within the file itself which you can see on the examples.

# login_info.txt
1. Channel name (i.e. cdnkrimsonkitty)
2. Twitch app client-id (e6xflds53ifrbx6eya8xyf3rg5fj4a)
3. Twitch token obtained by going to
-- https://id.twitch.tv/oauth2/authorize?client_id=e6xflds53ifrbx6eya8xyf3rg5fj4a&redirect_uri=http://localhost&response_type=token&scope=clips:edit --
The website will time out but the access token will be in the browser URL bar and you place it on the third line.
4. Twitter API key (all of the Twitter pieces will be found at https://developer.twitter.com/en -- dropdown and click Apps)
5. Twitter API secret
6. Twitter access token
7. Twitter access secret

# tweet_messages.txt

CHANNELNAME will become the same as the channel name in login_info.txt (cdnkrimsonkitty)
GAMENAME will become the game the script finds your channel to be playing at the time it ran.
A line will be randomly selected and it shouldn't matter how many there are.

# Further info and donations

This project is the combined effort of mucsdnop and KrimsonKitty.  You are free to use, modify, and distribute it as you see fit, but we do ask that any redistributions include this file so that proper credit is given.

For those who would like to support the creators, you can donate by using the link below.  If you'd like to support but are unable to donate, follows on Twitch or Twitter are also much appreciated.

[![paypal](https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif)](https://www.paypal.com/cgi-bin/webscr?cmd=_donations&business=PSKWJM6424KC8&currency_code=USD&source=url)

Twitter: @mucsdnop & @cdnkrimsonkitty
Twitch: http://twitch.tv/mucsdnop & http://twitch.tv/cdnkrimsonkitty

Also feel free to join our discord! https://discord.gg/nVfWHWK or send an e-mail if you have further questions to cdnkrimsonkitty@gmail.com
