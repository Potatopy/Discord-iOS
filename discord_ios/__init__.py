from .identify import identify
from nextcord.gateway import DiscordWebSocket

DiscordWebSocket.identify = identify
