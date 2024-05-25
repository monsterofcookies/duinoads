import requests as rq

channel = 'https://discord.com/api/v9/channels/1243880227470442529/messages'

payload = {
    'content':'content'
}

header ={ 
    'authorization':''
}

rq.post(channel, data=payload, headers=header)