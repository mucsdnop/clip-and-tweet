import tweepy
import requests
import random



#pick random line from tweet_messages.txt
def random_line(tweet_text):
    lines = open(tweet_text).read().splitlines()
    return random.choice(lines)



#send requests.get
def requests_get(get_params, get_variable):
    requests_get_result = requests.get(new_twitch_api + get_params + get_variable, headers=headers)
    return requests_get_result



#send requests.post
def requests_post(post_params, post_variable):
    requests_post_result = requests.post(new_twitch_api + post_params + post_variable, headers=headers)
    return requests_post_result



#read and load the login information for twitch and twitter
login_file = open("login_info.txt", "r") 
login_info = login_file.readlines()
for i in range(len(login_info)):
    login_info[i]=login_info[i].replace('\n','')
login_file.close()



#set variables from login_info.txt file
user_login = login_info[0]
client_id = login_info[1]
twitch_token = login_info[2]
twitter_api_key = login_info[3]
twitter_api_secret = login_info[4]
twitter_access_token = login_info[5]
twitter_access_secret = login_info[6]
new_twitch_api = "https://api.twitch.tv/helix/"



#set headers
headers = {
    'Client-ID': client_id,
    'Authorization': 'Bearer ' + twitch_token
}



#request channel info to get user id, display error if something goes wrong
try:
    user_id_data = requests_get('users?login=', user_login)
except:
    print("That didn't work.  Try updating the OAuth token.")
    input("Press Enter to continue...")
    exit()
#set user id
user_id_data = user_id_data.json()
user_id = user_id_data['data'][0]['id']



#request game id
game_id_data = requests_get('streams?user_id=', user_id)
#set game id
game_id_data = game_id_data.json()
game_id = game_id_data['data'][0]['game_id']



#request game information
game_name_data = requests_get('games?id=', game_id)
#set game name and remove spaces and colons for easier twitter hashtag use
game_name_data = game_name_data.json()
game_name = game_name_data['data'][0]['name']
game_name = game_name.replace(' ','').replace(':','')



#login to twitch with token and create clip
clip_id_data = requests_post('clips?broadcaster_id=', user_id)
#get id of the clip
clip_id_data = clip_id_data.json()
clip_id = clip_id_data['data'][0]['id']



#set twitch clip url
twitch_clip_url = f"https://www.twitch.tv/{user_login}/clip/{clip_id}"



#login to twitter
auth = tweepy.OAuthHandler(twitter_api_key, twitter_api_secret)
auth.set_access_token(twitter_access_token, twitter_access_secret)



#load twitter api and send tweet
twitter_api = tweepy.API(auth)
random_tweet_msg = random_line('tweet_messages.txt')
random_tweet_msg = random_tweet_msg.replace('CHANNELNAME', user_login).replace('GAMENAME','#' + game_name)
print(random_tweet_msg)
twitter_api.update_status(random_tweet_msg + ' ' + twitch_clip_url)



#exit
exit()
