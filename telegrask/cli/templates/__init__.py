from telegrask import Telegrask
from .config import TOKEN

bot = Telegrask(TOKEN)

from . import commands
