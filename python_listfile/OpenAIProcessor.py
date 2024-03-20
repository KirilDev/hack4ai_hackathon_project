from openai import OpenAI
class OpenAIProcessor:
    def __init__(self, api_key, org):
        self.client = OpenAI(api_key=api_key, organization=org)