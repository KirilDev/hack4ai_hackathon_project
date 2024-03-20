from openai import OpenAI
import json
def read_config():
        with open('/home/kirildev/ProjectsStore/hack4ai_Project/python_listfile/credentials.json') as config_file:
            config = json.load(config_file)
            return config
        
print(read_config()['api_key'])