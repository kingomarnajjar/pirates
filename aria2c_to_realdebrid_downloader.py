#!/usr/bin/python3

import requests
import subprocess
import os

# Real-Debrid API URL for getting the user's downloads list
API_URL = "https://api.real-debrid.com/rest/1.0/downloads"
# Path to save downloads
DOWNLOAD_PATH = "C:\\Users\\Dell\\Downloads"

# Your Real-Debrid API token
API_TOKEN = "GKJVDETFWMVK2EG43NZ2LSL7ZUQPMKIWPJGQJEZ22RUKRP6AG3TQ"

def get_realdebrid_links():
    """Fetches download links from Real-Debrid account"""
    headers = {"Authorization": f"Bearer {API_TOKEN}"}
    response = requests.get(API_URL, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to get links: {response.status_code}")
        return []

def download_with_aria2c(links):
    """Downloads files using aria2c from a list of links"""
    for link in links:
        # Command to download file using aria2c
        command = ["aria2c", "--dir", DOWNLOAD_PATH, link['download']]
        try:
            print(f"Downloading {link['filename']}...")
            subprocess.run(command, check=True)
        except subprocess.CalledProcessError as e:
            print(f"Failed to download {link['filename']}: {e}")

def main():
    links = get_realdebrid_links()
    if links:
        download_links = [link for link in links if link.get('download')]  # Filter out links without a download URL
        download_with_aria2c(download_links)
    else:
        print("No links to download.")

if __name__ == "__main__":
    main()
