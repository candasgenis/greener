import mysql.connector
from mysql.connector import Error



def connect_mysql_server():
    try:
        connection = mysql.connector.connect(host='localhost',
                                            database='greenerapp',
                                            user='root',
                                            password='##yourpassword##')
        if connection.is_connected():
            db_Info = connection.get_server_info()
            print("Connected to MySQL Server version ", db_Info)
            cursor = connection.cursor()
            cursor.execute("select database();")
            record = cursor.fetchone()
            print("You're connected to database: ", record)

    except Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")


def insert_user_to_db(userObject): # Function for inserting user's information to database.
    try:
        connection = mysql.connector.connect(host='localhost',database='greenerapp',user='root',password='##yourpassword##')
        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("INSERT INTO user_info"
                            "(user_id,kwh,location,house_type,number_of_rooms,heating_type,insulation)"  
                            "VALUES(%s, %s, %s, %s ,%s, %s,%s)", userObject.dump_user_attributes())
            cursor.commit()

            if(cursor.rowcount() > 0):
                return True
            else:
                return False
    except Error as e:
        print("Error while inserting user to database",e)
    finally:
        cursor.close()
        connection.close()

def update_user_kwh(userObject):   # Function for updating user's kwh.
    try:
         connection = mysql.connector.connect(host='localhost',database='greenerapp',user='root',password='##yourpassword##')
         if connection.is_connected():
             cursor = connection.cursor()
             cursor.execute("UPDATE user_info SET kwh = %s WHERE user_id = %s", (userObject.get_kwh(), userObject.get_user_id(),))
             cursor.commit()

             if(cursor.rowcount() > 0):
                 return True
             else:
                 return False
    except Error as e:
        print("Error while updating user kwh",e)
    finally:
        cursor.close()
        connection.close()

def update_user_heating_type(userObject): # Function for updating user's heating type.
    try:
        connection = mysql.connector.connect(host='localhost',database='greenerapp',user='root',password='##yourpassword##')
        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("UPDATE user_info SET heating_type = %s WHERE user_id = %s", (userObject.get_heatingType(), userObject.get_user_id(),))
            cursor.commit()

            if(cursor.rowcount() > 0):
                return True
            else:
                return False
    except Error as e:
        print("Error while updating user heating type",e)
    finally:
        cursor.close()
        connection.close()

def update_user_room_number(userObject): # Function for updating user's number of rooms.
    try:
        connection = mysql.connector.connect(host='localhost',database='greenerapp',user='root',password='##yourpassword##')
        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("UPDATE user_info SET number_of_rooms = %s WHERE user_id = %s", (userObject.get_numberOfRooms(), userObject.get_user_id(),))
            cursor.commit()

            if(cursor.rowcount() > 0):
                return True
            else:
                return False
    except Error as e:
        print("Error while updating user room number",e)
    finally:
        cursor.close()
        connection.close()

def update_user_location(userObject): # Function for updating user's location.
    try:
        connection = mysql.connector.connect(host='localhost',database='greenerapp',user='root',password='##yourpassword##')
        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("UPDATE user_info SET location = %s WHERE user_id = %s", (userObject.get_location(), userObject.get_user_id(),))
            cursor.commit()

            if(cursor.rowcount() > 0):
                return True
            else:
                return False
    except Error as e:
        print("Error while updating user location",e)
    finally:
        cursor.close()
        connection.close()


def update_insulation(userObject): # Function for updating user's insulation.
    try:
        connection = mysql.connector.connect(host='localhost',database='greenerapp',user='root',password='##yourpassword##')
        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("UPDATE user_info SET insulation = %s WHERE user_id = %s", (userObject.get_insulation(), userObject.get_user_id(),))
            cursor.commit()

            if(cursor.rowcount() > 0):
                return True
            else:
                return False
    except Error as e:
        print("Error while updating user insulation",e)
    finally:
        cursor.close()
        connection.close()

def update_house_type(userObject): # Function for updating user's house type.
    try:
        connection = mysql.connector.connect(host='localhost',database='greenerapp',user='root',password='##yourpassword##')
        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("UPDATE user_info SET house_type = %s WHERE user_id = %s", (userObject.get_houseType(), userObject.get_user_id(),))
            cursor.commit()

            if(cursor.rowcount() > 0):
                return True
            else:
                return False
    except Error as e:
        print("Error while updating user house type",e)
    finally:
        cursor.close()
        connection.close()

