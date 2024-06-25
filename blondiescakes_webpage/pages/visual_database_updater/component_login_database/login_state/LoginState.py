import reflex as rx
from blondiescakes_webpage.pages.visual_database_updater.component_login_database.login_state.PyMongoAPI import mongo_client
from blondiescakes_webpage.pages.visual_database_updater.component_login_database.login_state.login_state_initializations import crypto
from blondiescakes_webpage.pages.visual_database_updater.visual_database_updater import VerifyID
from blondiescakes_webpage.pages.visual_database_updater.component_login_database.login_state.cookies import CookieState
from blondiescakes_webpage.styles import constants as c

from datetime import datetime, timedelta, timezone
from uuid import uuid4
from jose import jwt


class LoginState(rx.State):
    password:str
    username:str

    token:dict
    def auth_user(self):
        recovered=mongo_client.test.users.find_one({"username":self.username})
        page_id=str(uuid4())

        if not recovered == None:
            user_id=str(recovered["_id"])

            if crypto.verify(self.password,recovered["password"]) and self.username == recovered["username"]:
                acces_token_expiration = datetime.now(tz=timezone.utc) + timedelta(minutes=c.AC_DURATION)
                access_token = {"sub":self.username, "exp":acces_token_expiration}
                token={"access_token":jwt.encode(access_token, algorithm=c.AL, key=c.SEED), "token_type":"Bearer"}
                
                self.token = token

                return [VerifyID.get_data(token,page_id,user_id),CookieState.update_cookie(self.token)]

            else:
                return rx.toast.error("Usuario o contraseña incorrectos")
        else:
            return rx.toast.error("Usuario o contraseña incorrecto")


    def get_username(self, username:str):
        self.username=username

    def get_password(self, password:str):
        self.password=password