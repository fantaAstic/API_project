import json
import requests
from pyyoutube import Api

# Initialize the API instance with your API key
api = Api(api_key="CLASSIFIED")

# Send a GET request to retrieve playlists by channel ID
channel_id = "UC_x5XG1OV2P6uZZ5FSM9Ttw"
response = api.get_playlists(channel_id=channel_id)

# Access the playlists
playlists = response.items
for playlist in playlists:
    print(playlist.id)

# Print the JSON response
response_dict = response.to_dict()
response_json = json.dumps(response_dict, indent=2)
print(response_json)
