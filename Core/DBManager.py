from Core.ConnectionConfig import ConnectionConfig
from Core.MySqlEngine import MySqlEngine
class DBManager:
    def __init__(self):
        self.config = ConnectionConfig("localhost","3306", "admin", "admin", "DataBaseA")
        self.engine = MySqlEngine(self.config)

    def login(self, name, password, userType):
      
        query = """
        SELECT fk_var_user_name, txt_password FROM User
            WHERE fk_var_user_name = '%s' AND txt_password = '%s' AND enu_type = '%s'
        """%(name, password,userType )
  
        if(len(self.engine.select(query))>0):
            return True
        return False
    
    def registry(self, name, lastName, email, password, userName, gender, userType, birthDate):
        try:
            insertFullName = """INSERT INTO FullName (var_user_name, txt_name, txt_last_name) 
                                VALUES 
                                ('%s', '%s', '%s') """%(userName, name, lastName)
            self.engine.insert(insertFullName)  
            insertUser = """
                    INSERT INTO User(fk_var_user_name, txt_password, var_email, enu_gender, enu_type, dat_birthdate) VALUES
                    ('%s','%s', '%s', '%s', '%s', '%s');
                """%(userName,password,email,gender, userType, birthDate)
            self.engine.insert(insertUser)
            print("Si se agrego")
        except:
            print("No se agrego")
            
    def delete(self,userName):
        try:
            deleteUser = " DELETE FROM user WHERE fk_var_user_name = '%s' "%(userName)
            self.engine.delete(deleteUser)
            deleteFullName = "DELETE FROM fullname WHERE var_user_name = '%s'"%(userName)
            self.engine.delete(deleteFullName)
            print("Si elimino")
        except:
            print("No elimno")
    
    def getUsers(self):
        query =  "SELECT * FROM User;"
        return self.engine.select(query)

        




        


        
