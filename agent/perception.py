import json

def read_post_history(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data
