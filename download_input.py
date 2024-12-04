import requests
import os
import argparse
from dotenv import load_dotenv

load_dotenv()

def download_input(day: str, file_path: str):
    """Downloads the Advent of Code input for a specific year and day."""
    url = f"https://adventofcode.com/2024/day/{day}/input"
    
    session_cookie = str(os.getenv('SESSION_COOKIE'))
    cookies = {"session": session_cookie}
    response = requests.get(url, cookies=cookies)
    default_file_path = f'./input/day_{day}.txt'
    final_file_path = file_path or default_file_path

    if response.status_code == 200:
        os.makedirs(os.path.dirname(final_file_path), exist_ok=True)

        with open(final_file_path, 'w') as file:
            file.write(response.text.strip())
        
        print(f"Input for day {day} of 2024 successfully downloaded to {final_file_path}")
    else:
        print(f"Failed to download input: HTTP {response.status_code}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Download Advent of Code input.")
    
    parser.add_argument('day', type=int, help='The day of the Advent of Code challenge (e.g., 1).')
    parser.add_argument(
        '--file_path',
        type=str,
        help='The path where the input should be saved (e.g., ./inputs/day_1.txt).',
        default=None
    )
    
    args = parser.parse_args()

    download_input(args.day, args.file_path)
