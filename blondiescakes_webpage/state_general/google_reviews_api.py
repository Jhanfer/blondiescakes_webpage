import os
import dotenv
import serpapi
import reflex as rx
from blondiescakes_webpage.pages.visual_database_updater.components_database.state_database.api import update_reviews
import json

class GoogleMapsReviewsUpdater(rx.State):
    def update_google_reviews_database(self):
        dotenv.load_dotenv()
        KEY = os.environ.get("KEY")
        client = serpapi.Client(api_key=KEY)
        results = client.search(
            {
                "engine":"google_maps",
                "type":"search",
                "place_id":"ChIJ8xBiSIWjMI4R02Vq0YhupFI"
            },
        )
        try:
            results = results["place_results"]["user_reviews"]["most_relevant"]
            update_reviews(results)
            return [rx.toast.success("Datos actualizados"), rx.call_script("window.location.reload()")]
        
        except:
            return rx.toast.error("un error ha ocurrido")