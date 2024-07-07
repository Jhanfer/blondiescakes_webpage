import reflex as rx
from instagrapi import Client



class InstaAPI(rx.State):

    id:list[str]
    taken:list[str]
    username:list[str]
    like_count:list[str]
    image_urls:list[str]
    urls:list[str]

    def api_init(self):
        cl = Client()
        ACCOUNT_USERNAME="test"
        ACCOUNT_PASSWORD="test"
        cl.login(ACCOUNT_USERNAME, ACCOUNT_PASSWORD)

        user_id = cl.user_id_from_username(ACCOUNT_USERNAME)
        data_string = cl.user_medias(user_id, 1)


        # Iteramos sobre cada objeto Media en la lista
        for media_object in data_string:
            # Extraer el ID
            self.id = media_object.id

            # Extraer la fecha
            self.taken = media_object.taken_at

            # Extraer el nombre de usuario
            self.username = media_object.user.username

            # Extraer el conteo de likes
            self.like_count = media_object.like_count

            # Extraer las URLs de las imágenes
            self.image_urls = [resource.thumbnail_url for resource in media_object.resources if resource.thumbnail_url]
            
            for url in self.image_urls:
                self.urls=url







































