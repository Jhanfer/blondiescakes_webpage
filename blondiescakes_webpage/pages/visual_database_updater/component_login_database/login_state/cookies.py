import reflex as rx
#from blondiescakes_webpage.pages.visual_database_updater.component_login_database.login_state.LoginState import CookieBase

class CookieState(rx.State):
    sesion_token:str=rx.Cookie("")
    show:str=rx.Cookie("False")

    def update_cookie(self,coso:dict):
        self.sesion_token=coso

    def show_page(self,show:bool):
        self.show=show

    def logout(self):
        self.show=False
        return rx.remove_cookie("sesion_token")