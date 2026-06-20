"""
Custom storage that fixes pyrofork 2.3.9's missing update_usernames implementation.
Wraps MemoryStorage and adds all missing abstract methods as no-ops safe for bots.
"""
from pyrogram.storage import MemoryStorage


class BotStorage(MemoryStorage):
    """
    MemoryStorage extended with stubs for methods pyrofork added to the
    Storage interface but did not implement in the concrete classes.
    For bots these methods are not needed — bots don't do username lookups.
    """

    async def update_usernames(self, usernames):
        pass

    async def get_peer_by_username(self, username: str):
        raise KeyError(f"Username not found: {username}")
