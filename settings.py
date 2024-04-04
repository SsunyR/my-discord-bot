#[T] = Token
from dotenv import load_dotenv
import os
load_dotenv()
TOKEN = os.getenv('TOKEN')

#[L] = Logger
import logging