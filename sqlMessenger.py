import mysql.connector
from mysql.connector import Error


def connect_mysql_server():
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='greenerapp',
                                             user='root',
                                             password='1234')
        if connection.is_connected():
            db_Info = connection.get_server_info()
            print("Connected to MySQL Server version ", db_Info)
            cursor = connection.cursor()
            cursor.execute("select database();")
            record = cursor.fetchone()
            print("You're connected to database: ", record)
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

    except Error as e:
        print("Error while connecting to MySQL", e)


def insert_user_to_db(userObject):  # Function for inserting user's information to database.
    try:
        connection = mysql.connector.connect(host='localhost', database='greenerapp', user='root',
                                             password='1234')
        if connection.is_connected():
            dump_tuple = (userObject.get_user_id(), userObject.get_carbon_emission(),
                          userObject.get_kwh_total(), userObject.get_kwh_electricity_total(),
                          userObject.get_kwh_gas_total(), userObject.get_location())
            print(dump_tuple)
            cursor = connection.cursor()
            try:
                cursor.execute("INSERT INTO user_info"
                               "(user_id, carbon_emission, kwh_total, electricity_kwh_total, gas_kwh_total, location) "
                               "VALUES(%s, %s, %s, %s, %s, %s, %s ,%s, %s, %s)", dump_tuple)

                connection.commit()
                cursor.close()
                connection.close()
                return True
            except Error as e:
                print("Error while inserting data into MySQL", e)
                cursor.close()
                connection.close()
                return False
    except Error as e:
        print("Error while inserting user to database", e)


def get_user_from_db(userObject):  # Function for getting user's information from database.
    try:
        connection = mysql.connector.connect(host='localhost', database='greenerapp', user='root',
                                             password='1234')
        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM user_info WHERE user_id = %s", (userObject.get_user_id(),))
            record = cursor.fetchone()
            print(record)
            if record is not None:
                cursor.close()
                connection.close()
                return record
            else:
                cursor.close()
                connection.close()
                return False
    except Error as e:
        print("Error while getting user from database", e)


def get_carbon_emission_from_db(userObject):  # Function for getting user's carbon emission from database.
    try:
        connection = mysql.connector.connect(host='localhost', database='greenerapp', user='root',
                                             password='1234')
        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("SELECT carbon_emission FROM user_info WHERE user_id = %s", (userObject.get_user_id(),))
            record = cursor.fetchone()
            print(record)
            if record is not None:
                cursor.close()
                connection.close()
                return record
            else:
                cursor.close()
                connection.close()
                return False
    except Error as e:
        print("Error while getting carbon emission from database", e)
        return False


def update_carbon_emission(userObject):  # Function for setting user's carbon emission in database.
    try:
        connection = mysql.connector.connect(host='localhost', database='greenerapp', user='root',
                                             password='1234')
        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("UPDATE user_info SET carbon_emission = %s WHERE user_id = %s", (
                userObject.get_carbon_emission(), userObject.get_user_id()))
            connection.commit()
            cursor.close()
            connection.close()
            return True
    except Error as e:
        print("Error while setting carbon emission in database", e)
        return False


def get_house_belong_to_user(user_id):
    try:
        connection = mysql.connector.connect(host='localhost', database='greenerapp', user='root',
                                             password='1234')
        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("SELECT home_id FROM user_home WHERE user_id = %s", (user_id,))
            record = cursor.fetchAll()
            if(len(record) > 0):
                return record
            else:
                return False

    except Error as e:
        print("Error while getting house belong to user", e)
        return False



def get_kwh_total_from_db(user_id):  # Function for getting user's total kwh from database.
    try:
        connection = mysql.connector.connect(host='localhost', database='greenerapp', user='root',
                                             password='1234')
        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("SELECT kwh_total FROM user_info WHERE user_id = %s", (user_id,))
            record = cursor.fetchone()
            if record is not None:
                cursor.close()
                connection.close()
                return record[0]
            else:
                cursor.close()
                connection.close()
                return False
    except Error as e:
        print("Error while getting user from database", e)
        return False


def update_kwh_total(userObject):  # Function for setting user's total kwh in database.
    try:
        connection = mysql.connector.connect(host='localhost', database='greenerapp', user='root',
                                             password='1234')
        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("UPDATE user_info SET kwh_total = %s WHERE user_id = %s", (
                userObject.get_kwh_total(), userObject.get_user_id()))
            connection.commit()
            cursor.close()
            connection.close()
            return True
    except Error as e:
        print("Error while setting kwh total in database", e)
        return False

def update_user_kwh_electricity(userObject):  # Function for updating user's electricity kwh.
    try:
        connection = mysql.connector.connect(host='localhost', database='greenerapp', user='root',
                                             password='1234')
        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("UPDATE user_info SET kwh_electricity_total = %s WHERE user_id = %s",
                           (userObject.get_kwh_electricity_total(), userObject.get_user_id()))
            connection.commit()
            cursor.close()
            connection.close()
            return True
    except Error as e:
        print("Error while updating user's electricity kwh", e)
        return False

def update_home_kwh_electricity(homeObject):  # Function for updating user's electricity kwh.
    try:
        connection = mysql.connector.connect(host='localhost', database='greenerapp', user='root',
                                             password='1234')
        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("UPDATE home SET kwh_electricity = %s WHERE home_id = %s",
                           (homeObject.get_kwh_electricity(), homeObject.get_home_id()))
            connection.commit()
            cursor.close()
            connection.close()
            return True
    except Error as e:
        print("Error while updating user's electricity kwh", e)
        return False

def update_home_kwh_gas(homeObject):  # Function for updating home's gas kwh.
    try:
        connection = mysql.connector.connect(host='localhost', database='greenerapp', user='root',
                                             password='1234')
        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("UPDATE home SET kwh_gas = %s WHERE home_id = %s",
                           (homeObject.get_kwh_gas(), homeObject.get_home_id()))
            connection.commit()
            cursor.close()
            connection.close()
            return True
    except Error as e:
        print("Error while updating home's gas kwh", e)
        return False


def get_user_kwh_electricity_from_db(userObject):  # Function for getting user's electricity kwh.
    try:
        connection = mysql.connector.connect(host='localhost', database='greenerapp', user='root',
                                             password='1234')
        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("SELECT kwh_electricity FROM user_info WHERE user_id = %s", (userObject.get_user_id(),))
            record = cursor.fetchone()
            if record is not None:
                cursor.close()
                connection.close()
                return record[0]
            else:
                cursor.close()
                connection.close()
                return False
    except Error as e:
        print("Error while getting user's electricity kwh", e)
        return False


def update_user_kwh_gas(userObject):  # Function for updating user's gas kwh.
    try:
        connection = mysql.connector.connect(host='localhost', database='greenerapp', user='root',
                                             password='1234')
        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("UPDATE user_info SET kwh_gas_total = %s WHERE user_id = %s",
                           (userObject.get_kwh_gas_total(), userObject.get_user_id()))
            connection.commit()
            cursor.close()
            connection.close()
            return True
    except Error as e:
        print("Error while updating user's gas kwh", e)
        return False




def get_user_kwh_gas_from_db(userObject):  # Function for getting user's gas kwh.
    try:
        connection = mysql.connector.connect(host='localhost', database='greenerapp', user='root',
                                             password='1234')
        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("SELECT kwh_gas FROM user_info WHERE user_id = %s", (userObject.get_user_id(),))
            record = cursor.fetchone()
            if record is not None:
                cursor.close()
                connection.close()
                return record[0]
            else:
                cursor.close()
                connection.close()
                return False
    except Error as e:
        print("Error while getting user's gas kwh", e)
        return False

def get_user_homes_from_db(userObject):
    try:
        connection = mysql.connector.connect(host='localhost', database='greenerapp', user='root',
                                             password='1234')
        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("SELECT home_id FROM user_home WHERE user_id = %s", (userObject.get_user_id(),))
            record = cursor.fetchall()
            if record is not None:
                cursor.close()
                connection.close()
                return record
            else:
                cursor.close()
                connection.close()
                return False
    except Error as e:
        print("Error while getting user's gas kwh", e)
        return False

def update_house_heating_type(home_id, heating_type):  # Function for updating user's heating type.
    try:
        connection = mysql.connector.connect(host='localhost', database='greenerapp', user='root',
                                             password='##yourpassword##')
        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("UPDATE house SET heating_type = %s WHERE home_id = %s",
                           (heating_type, home_id,))
            connection.commit()

            if len(cursor.fetchall()) > 0:
                cursor.close()
                connection.close()
                return True
            else:
                cursor.close()
                connection.close()
                return False
    except Error as e:
        print("Error while updating user heating type", e)


def get_user_heating_type_from_db(houseObject):  # Function for getting user's heating type.
    try:
        connection = mysql.connector.connect(host='localhost', database='greenerapp', user='root',
                                             password='##yourpassword##')
        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("SELECT heating_type FROM home WHERE home_id = %s", (houseObject.get_house_id(),))
            record = cursor.fetchone()
            if len(cursor.fetchall()) > 0:
                cursor.close()
                connection.close()
                return record[0]
            else:
                cursor.close()
                connection.close()
                return False
    except Error as e:
        print("Error while getting user heating type", e)


def update_user_room_number(houseObject):  # Function for updating user's number of rooms.
    try:
        connection = mysql.connector.connect(host='localhost', database='greenerapp', user='root',
                                             password='##yourpassword##')
        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("UPDATE home SET number_of_rooms = %s WHERE home_id = %s",
                           (houseObject.get_number_of_rooms(), houseObject.get_home_id(),))
            connection.commit()

            if len(cursor.fetchall()) > 0:
                cursor.close()
                connection.close()
                return True
            else:
                cursor.close()
                connection.close()
                return False
    except Error as e:
        print("Error while updating user room number", e)


def get_house_room_number_from_db(houseObject):  # Function for getting user's number of rooms.
    try:
        connection = mysql.connector.connect(host='localhost', database='greenerapp', user='root',
                                             password='##yourpassword##')
        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("SELECT number_of_rooms FROM home WHERE home_id = %s", (houseObject.get_home_id(),))
            record = cursor.fetchone()
            if len(cursor.fetchall()) > 0:
                cursor.close()
                connection.close()
                return record[0]
            else:
                cursor.close()
                connection.close()
                return False
    except Error as e:
        print("Error while getting user room number", e)


def update_user_location(userObject):  # Function for updating user's location.
    try:
        connection = mysql.connector.connect(host='localhost', database='greenerapp', user='root',
                                             password='##yourpassword##')
        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("UPDATE user_info SET location = %s WHERE user_id = %s",
                           (userObject.get_location(), userObject.get_user_id(),))
            connection.commit()

            if len(cursor.fetchall()) > 0:
                cursor.close()
                connection.close()
                return True
            else:
                cursor.close()
                connection.close()
                return False
    except Error as e:
        print("Error while updating user location", e)


def get_user_location_from_db(userObject):  # Function for getting user's location.
    try:
        connection = mysql.connector.connect(host='localhost', database='greenerapp', user='root',
                                             password='##yourpassword##')
        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("SELECT location FROM user_info WHERE user_id = %s", (userObject.get_user_id(),))
            record = cursor.fetchone()
            if len(cursor.fetchall()) > 0:
                cursor.close()
                connection.close()
                return record[0]
            else:
                cursor.close()
                connection.close()
                return False
    except Error as e:
        print("Error while getting user location", e)


def update_insulation(houseObject):  # Function for updating user's insulation.
    try:
        connection = mysql.connector.connect(host='localhost', database='greenerapp', user='root',
                                             password='##yourpassword##')
        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("UPDATE house SET insulation = %s WHERE house_id= %s",
                           (houseObject.get_insulation(), houseObject.get_home_id(),))
            connection.commit()

            if len(cursor.fetchall()) > 0:
                cursor.close()
                connection.close()
                return True
            else:
                cursor.close()
                connection.close()
                return False
    except Error as e:
        print("Error while updating user insulation", e)


def get_home_insulation_from_db(homeObject):  # Function for getting user's insulation.
    try:
        connection = mysql.connector.connect(host='localhost', database='greenerapp', user='root',
                                             password='##yourpassword##')
        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("SELECT insulation FROM home WHERE house_id = %s", (homeObject.get_home_id(),))
            record = cursor.fetchone()
            if len(cursor.fetchall()) > 0:
                cursor.close()
                connection.close()
                return record[0]
            else:
                cursor.close()
                connection.close()
                return False
    except Error as e:
        print("Error while getting user insulation", e)


def update_house_type(house_id, house_type):  # Function for updating user's house type.
    try:
        connection = mysql.connector.connect(host='localhost', database='greenerapp', user='root',
                                             password='##yourpassword##')
        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("UPDATE house SET house_type = %s WHERE house_id = %s",
                           (house_type, house_id,))
            connection.commit()

            if len(cursor.fetchall()) > 0:
                cursor.close()
                connection.close()
                return True
            else:
                cursor.close()
                connection.close()
                return False
    except Error as e:
        print("Error while updating house type", e)


def get_user_house_type_from_db(userObject):  # Function for getting user's house type.
    try:
        connection = mysql.connector.connect(host='localhost', database='greenerapp', user='root',
                                             password='##yourpassword##')
        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("SELECT house_type FROM user_info WHERE user_id = %s", (userObject.get_user_id(),))
            record = cursor.fetchone()
            if len(cursor.fetchall()) > 0:
                cursor.close()
                connection.close()
                return record[0]
            else:
                cursor.close()
                connection.close()
                return False
    except Error as e:
        print("Error while getting user house type", e)
