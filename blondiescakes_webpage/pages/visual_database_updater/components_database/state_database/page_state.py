import reflex as rx
from blondiescakes_webpage.pages.visual_database_updater.components_database.state_database.api import get_data_alter_api,get_all_data_database #get_data
from blondiescakes_webpage.pages.visual_database_updater.components_database.state_database.supabase_database import Featured
from typing import Union

class PageState(rx.State):

    general_database_data:list[Featured]
    class_buttercream:list[Featured]
    class_frias:list[Featured]
    class_tradicionales:list[Featured]
    class_saludables:list[Featured]
    
    title:str

    async def get_database_data(self):
        self.general_database_data = await get_all_data_database()

    async def get_database_data_alter(self,categorie:str):
        
        categorias = {
            "buttercream": "class_buttercream",
            "frias": "class_frias",
            "saludables": "class_saludables",
            "tradicionales": "class_tradicionales",
            "database": "general_database_data"
        }

        if categorie in categorias:
            data = await get_data_alter_api(categorie)
            attr_name = categorias[categorie]
            self.title = categorie
            setattr(self, attr_name, data)
        else:
            print(f"Categoría no reconocida: {categorie}")