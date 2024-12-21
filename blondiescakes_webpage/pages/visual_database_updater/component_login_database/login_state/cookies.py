import reflex as rx
#from blondiescakes_webpage.pages.visual_database_updater.component_login_database.login_state.LoginState import CookieBase

class CookieState(rx.State):
    sesion_token:str=rx.Cookie("")
    show:str=rx.Cookie("False")
    current_url:str=rx.Cookie("")

    def update_cookie(self,token:dict):
        self.sesion_token=token

    def update_current_url(self,url:str):
        self.current_url=url

    def show_page(self,show:bool):
        self.show=show

    def logout(self):
        self.show=False
        return [rx.remove_cookie("sesion_token")]
    

