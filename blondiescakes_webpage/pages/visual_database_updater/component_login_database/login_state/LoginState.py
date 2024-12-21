import reflex as rx
from blondiescakes_webpage.pages.visual_database_updater.component_login_database.login_state.PyMongoAPI import mongo_client
from blondiescakes_webpage.pages.visual_database_updater.visual_database_updater import VerifyID
from blondiescakes_webpage.pages.visual_database_updater.component_login_database.login_state.cookies import CookieState
from blondiescakes_webpage.styles import constants as c

from datetime import datetime, timedelta, timezone
from uuid import uuid4
from jose import jwt
from passlib.hash import bcrypt
import time
from collections import defaultdict



class InMemoryRateLimiter:
    def __init__(self, max_attempts: int = 5, window_seconds: int = 300):
        self.max_attempts = max_attempts
        self.window_seconds = window_seconds
        self.attempts = defaultdict(list)

    def is_rate_limited(self, key: str) -> bool:
        current = time.time()
        self.attempts[key] = [t for t in self.attempts[key] if current - t < self.window_seconds]
        self.attempts[key].append(current)
        return len(self.attempts[key]) > self.max_attempts

memory = InMemoryRateLimiter()

class LoginState(rx.State):
    password:str
    username:str
    token:dict

    def auth_user(self):
        
        # Buscar usuario en la base de datos
        user = mongo_client.test.users.find_one({"username": self.username})
        match user:
            case None:
                out_of_rate_limit_username = memory.is_rate_limited(self.username)
                match out_of_rate_limit_username:
                    case True:
                        return rx.toast.error("Demasiados intentos. Por favor, intente más tarde.")
                return rx.toast.error("Usuario o contraseña incorrectos")

        # Verificar contraseña
        verifyed = bcrypt.verify(self.password, user["password"])
        match verifyed:
            case False:
                out_of_rate_limit_username = memory.is_rate_limited(self.username)
                match out_of_rate_limit_username:
                    case True:
                        return rx.toast.error("Demasiados intentos. Por favor, intente más tarde.")
                return rx.toast.error("Usuario o contraseña incorrectos")
        
        
        # Generar token
        page_id = str(uuid4())
        user_id = str(user["_id"])
        access_token_expiration = datetime.now(tz=timezone.utc) + timedelta(minutes=int(c.AC_DURATION))
        access_token = {"sub": self.username,"exp": access_token_expiration}
        token = {
            "access_token": jwt.encode(access_token, key=c.SEED, algorithm=c.AL),
            "token_type": "Bearer"
        }

        self.token = token

        # Retornar acciones
        return [
            VerifyID.get_data(token, page_id, user_id),
            CookieState.update_cookie(self.token)
        ]



    def get_username(self, username:str):
        self.username=username

    def get_password(self, password:str):
        self.password=password