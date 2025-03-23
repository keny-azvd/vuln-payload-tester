import requests
from colorama import Fore, Style, init

init(autoreset=True)

def get_base_url():
    base_url = input("Please enter the BASE_URL (default: http://rescued-float.picoctf.net:57310/): ")
    return base_url if base_url else 'http://rescued-float.picoctf.net:57310/'


def get_paths():
    choice = input("Do you want to load paths from a file or enter them manually? (file/manual): ").strip().lower()

    if choice == "file":
        #
        file_path = input("Please enter the path to the file: ")
        try:
            with open(file_path, 'r') as f:
                paths = f.read().splitlines()  
            print(f"Loaded paths from {file_path}: {paths}")
        except FileNotFoundError:
            print(f"Error: The file '{file_path}' was not found.")
            return []
    else:
        
        paths = []
        while True:
            path = input("Enter a path (or press Enter to stop): ")
            if not path:
                break
            paths.append(path)
        print(f"Paths entered: {paths}")
    
    return paths


BASE_URL = get_base_url()
PATHS = get_paths()

print(f"BASE_URL: {BASE_URL}")
print(f"PATHS: {PATHS}")

print('Scanning the web site, looking for SSTI vits!')
print(' ')

#change this format next time

DATA = [
    {'content': "{{7*7}}"},
    {'content': "{{7*'7'}}"},
    {'content': "a{*coment*}b}"},
    {'content': '${"z".join("ab")}'}
]

for data in DATA:
    for path in PATHS:
        response = requests.post(BASE_URL + path, data=data)

        if response.status_code == 200:
            print(f"{Fore.GREEN}Successfully posted {data} into the form! Used path: {path}")
            print(f"{Style.DIM}{response.text}{Style.RESET_ALL}")
            print()
        else:
            print(f"{Fore.RED}Failed to post {data} into the form at path: {path}. Status code: {response.status_code}")
            print()
