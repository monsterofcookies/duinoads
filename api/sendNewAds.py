import requests as rq
import os 
from dotenv import load_dotenv

load_dotenv()
disauth = os.getenv('disauth')


channel = 'https://discord.com/api/v9/channels/1243880227470442529/messages'

payload = {
    'content':'content'
}

header ={ 
    'authorization':f'{disauth}'
}

rq.post(channel, data=payload, headers=header)