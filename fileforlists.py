import requests

responses = ['It is certain',
 'It is decidedly so', 
 'Without a doubt', 
 'Yes – definitely', 
 'You may rely on it',
  'As I see it, yes', 
  'Most likely', 
  'Outlook good', 
  'Yes Signs point to yes', 
  'Reply hazy', 
  'try again', 
  'Ask again later', 
  'Better not tell you now', 
  'Cannot predict now', 
  'Concentrate and ask again', 
  'Dont count on it', 
  'My reply is no', 
  'My sources say no', 
  'Outlook not so good', 
  'Very doubtful']


username_list = []
comments_list = []
comments_and_username_list = []

def url_giver(url1):
    url = url1
    reddit_url = url + '.json'
    global r
    r = requests.get(reddit_url, headers={'user-agent': 'Mozilla/5.0'})


def usernames():
    for post in r.json():
        for datas in post['data']['children']:
            for keys in datas['data']:
                if keys == "author":
                    username_list.append(datas['data'][keys])
    username_list.pop(0)
    return username_list

def comments():
    for post2 in r.json():
        for datas2 in post2['data']['children']:
            for keys2 in datas2['data']:
                if keys2 == "body":
                    comments_list.append(datas2['data'][keys2])
    return comments_list

def comment_and_name_shower():
    comments()
    usernames()
    for i in range(len(comments_list)):
        comments_and_username_list.append(str(f"Comment made by u/{username_list[i]} = {comments_list[i]}"))





