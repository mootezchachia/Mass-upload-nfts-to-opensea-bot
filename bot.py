import requests
from PIL import Image

# Set your OpenSea API key
api_key = 'your_api_key'

# Set the URL of the OpenSea API
api_url = 'https://api.opensea.io/api/v1/'

# Set the directory where your NFT images are stored
nft_dir = 'C:/Users/User/Desktop/NFTs/'

# Iterate over the files in the NFT directory
for file in os.listdir(nft_dir):
    # Use Pillow to open the image file
    img = Image.open(file)

    # Generate a unique ID for the NFT
    nft_id = uuid.uuid4()

    # Set the metadata for your NFT
    metadata = {
        'name': file,
        'description': 'This is my NFT',
        'external_url': 'http://www.example.com/nft/' + str(nft_id),
        'image_url': 'http://www.example.com/nft/' + file,
    }

    # Set the contract address and token ID for the NFT
    nft = {'contract_address': '0x12345...', 'token_id': nft_id}

    # Set the URL for the OpenSea API endpoint
    url = api_url + 'assets/'

    # Set the headers for the request
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + api_key,
    }

    # Set the data for the request
    data = {
        'asset': {
            'contract_address': nft['contract_address'],
            'token_id': nft['token_id'],
            'metadata': metadata,
        }
    }

    # Use requests to make a POST request to the OpenSea API
    r = requests.post(url, headers=headers, json=data)

    # Print the response
    print(r.json())
