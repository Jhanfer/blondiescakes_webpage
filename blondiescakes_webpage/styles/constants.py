import dotenv
import os



### Element updater constants ###


dotenv.load_dotenv()
AL = os.environ.get("AL")
AC_DURATION = os.environ.get("AC_DURATION")
SEED = os.environ.get("SEED")



### Head_component Scripts ###

ANALYTICS_SCRIPTS_1 = os.environ.get("ANALYTICS_SCRIPTS_1")
ANALYTICS_ID = os.environ.get("ANALYTICS_ID")

ANALYTICS_SCRIPTS_2 = f"""window.dataLayer = window.dataLayer || [];
                        function gtag(){{dataLayer.push(arguments);}}
                        gtag('js', new Date());
                        gtag('config', '{ANALYTICS_ID}');"""


##Number##
CONTACT_NUMBER = "+573225360402"


