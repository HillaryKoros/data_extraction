import requests
import pandas as pd
import json
from bs4 import BeautifulSoup as bs

# Function to fetch JSON data
def fetch_json_data(url, headers):
    """
    Fetch JSON data from a given URL and headers.
    
    Parameters:
        url (str): The URL to fetch data from.
        headers (dict): The headers to use for the request.
        
    Returns:
        dict: The parsed JSON data.
    """
    # Send a GET request to the URL with the provided headers
    response = requests.get(url, headers=headers)
    
    # Parse the response content using BeautifulSoup
    soup = bs(response.text, "html.parser")
    
    # Find the script tag containing the JSON data
    script_tag = soup.find('script', id='__NEXT_DATA__')
    
    if script_tag:
        # Load and return the JSON data
        data = json.loads(script_tag.string)
        return data
    return None

# Function to convert JSON data to DataFrame
def json_to_dataframe(json_data):
    """
    Convert JSON data to a DataFrame.
    
    Parameters:
        json_data (dict): The JSON data to convert.
        
    Returns:
        DataFrame: A DataFrame containing the JSON data.
    """
    # Extract the results from the JSON data
    results = json_data.get('props', {}).get('pageProps', {}).get('data', {}).get('results', [])
    
    # Convert the results list to a DataFrame
    df = pd.DataFrame(results)
    return df

# Define the base URL for fetching data, with a placeholder for page numbers
base_url = "https://kmhfr.health.go.ke/public/facilities?page={}"

# Generate a list of URLs for each page from 1 to 494
urls = [base_url.format(page) for page in range(1, 495)]

# Define headers for HTTP requests to mimic a browser request
HEADERS = {
    "accept": "*/*",
    "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "en-US,en;q=0.9,fr;q=0.8",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36"
}

# Initialize an empty DataFrame to accumulate all the fetched data
all_data = pd.DataFrame()

# Loop through each URL and fetch data
for url in urls:
    data = fetch_json_data(url, HEADERS)
    if data:
        # Convert JSON data to DataFrame
        df = json_to_dataframe(data)
        # Append the DataFrame to the accumulated data
        all_data = pd.concat([all_data, df], ignore_index=True)

