from typing import Annotated

from fastapi import Depends
from snuvote.database.models import User
from snuvote.app.user.store import UserStore



class UserService:
    def __init__(self, user_store: Annotated[UserStore, Depends()]) -> None:
        self.user_store = user_store

    
    #ȸ������
    def add_user(self, userid: str, password: str, email: str):
        return self.user_store.add_user(userid=userid, password=password, email=email)
    
