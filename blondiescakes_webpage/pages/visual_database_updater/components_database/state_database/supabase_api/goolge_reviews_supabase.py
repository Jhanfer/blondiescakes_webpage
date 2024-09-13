import os
from supabase import create_client, Client
import dotenv
from blondiescakes_webpage.pages.visual_database_updater.components_database.state_database.supabase_api.classes_base import ReviewsBase



class GoogleReviewsSupabase():
    """Supabase API for Google Reviews"""
    url: str = os.environ.get("SUPABASE_URL")
    key: str = os.environ.get("SUPABASE_KEY")
    supabase:Client

    @property
    def act_data(self):
        """Update data and load envs"""
        dotenv.load_dotenv()
        if self.url and self.key:
            self.supabase: Client = create_client(self.url, self.key)
            
    # Google Maps Reviews #
    def get_reviews_data(self):
        self.act_data
        response = self.supabase.table("google_review_data").select("*").execute()
        if len(response.data) > 0:
            dictionary = response.data
            reviews = dictionary[0]["data"]
            reviews_list = []
            for review in reviews:
                if "description" in review:
                    if len(review["description"]) > 190:
                        short = review["description"][:190] + "..."
                        reviews_list.append(
                            ReviewsBase(
                                username=review["username"],
                                rating=review["rating"],
                                description=short,
                                date=review["date"]
                            )
                        )
                    else:
                        reviews_list.append(
                            ReviewsBase(
                                username=review["username"],
                                rating=review["rating"],
                                description=review["description"],
                                date=review["date"]
                            )
                        )
                else:
                    pass
        return reviews_list

    def update_reviews_data(self,google_json):
        self.act_data
        response = self.supabase.table("google_review_data").update({"data":google_json}).eq("id", 1).execute()
