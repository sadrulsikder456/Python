class UserAccount:
    def __init__(self,username,password):
        self.username=username
        self.__password=password
    def set_password(self,new_password):
        self.__password=new_password
        print("New password has been set.")
    def checker(self,input_password):
        if self.__password==input_password:
            print("Access Granted.")
            return True
        else:
            print("Access Denied.")
            return False

user1= UserAccount("Sadrul Amin", "&adrul")
user1.checker("sadrul")
user1.checker("&adrul")
