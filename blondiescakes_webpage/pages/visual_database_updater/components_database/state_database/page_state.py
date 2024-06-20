import reflex as rx
from blondiescakes_webpage.pages.visual_database_updater.components_database.state_database.api import get_data
from blondiescakes_webpage.pages.visual_database_updater.components_database.state_database.supabase_database import Featured
from typing import Union

class PageState(rx.State):

    database_data:list[Featured]
    title:str

    async def get_database_data(self):
        self.database_data = await get_data()






