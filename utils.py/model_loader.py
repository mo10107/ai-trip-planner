from typing import Literal, Optional
from pydantic import BaseModel, Field
import os
from langchain_together import ChatTogether
from dotenv import load_dotenv
load_dotenv()
from utils.config_loader import load_config

class ConfigLoader:
    def __init__(self):
        print(f"Loaded config.....")
        self.config = load_config()
    
    def __getitem__(self, key):
        return self.config[key]

class ModelLoader(BaseModel):
    model_provider = Literal["together_ai"]
    config: Optional[ConfigLoader] = Field(default=None, exclude=True)

    def model_post_init(self):
        self.config = ConfigLoader()
    
    model_config = {
        "arbitrary_types_allowed": True
    }
    
    def load_llm(self):
        print("LLM loading...")
        print(f"Loading model from provider: {self.model_provider}")
        if self.model_provider == "together_ai":
            print("Loading LLM from Together AI..............")
            together_api_key = os.getenv("TOGETHER_API_KEY")
            model_name = self.config["llm"]["together_ai"]["model_name"]
            llm=ChatTogether(model=model_name, api_key=together_api_key)

        return llm