from flask import Flask, jsonify, request, session
import yaml

import calculations
import sqlMessenger
from user import User
from household import household

#db = yaml.safe_load(open('../src/db.yaml'))
app = Flask(__name__)
#app.secret_key = db['secret_key']

@app.route('/set_user_info', methods=['POST'])
def set_user_info():
    user_id = request.form['user_id']
    kwh_electricity_total = request.form['kwh_electricity_total']
    kwh_gas_total = request.form['kwh_gas_total']
    location = request.form['location']

    user_object = User(user_id)
    user_object.set_kwh_electricity_total(kwh_electricity_total)
    user_object.set_kwh_gas_total(kwh_gas_total)
    user_object.set_location(location)
    user_object.set_kwh_total(int(user_object.get_kwh_electricity_total()) + int(user_object.get_kwh_gas_total()))

    calculation_object = calculations.calculation(kwh_electricity=user_object.get_kwh_electricity_total(),
                                                  kwh_gas=user_object.get_kwh_gas_total())

    user_object.set_carbon_emission(calculation_object.calculate_co2_overall())

    if sqlMessenger.insert_user_to_db(user_object):
        return jsonify({'status': 'success'})
    else:
        return jsonify({'status': 'failure'})

@app.route('/get_user_info', methods=['GET'])
def get_user_info():
    user_id = request.form['user_id']
    user_object = User(user_id)
    user_info = sqlMessenger.get_user_from_db(userObject=user_object)
    print(user_info)
    if user_info:
        return jsonify({'status': 'success', 'user_info': user_info})
    else:
        return jsonify({'status': 'failure'})

@app.route('/get_carbon_emission', methods=['GET'])
def get_carbon_emission_flask():
    user_id = request.form['user_id']
    user_object = User(user_id)
    user_object.set_carbon_emission(sqlMessenger.get_carbon_emission_from_db(userObject=user_object))
    if user_object.get_carbon_emission():
        return jsonify({'status': 'success', 'carbon_emission': user_object.get_carbon_emission()})
    else:
        return jsonify({'status': 'failure'})

@app.route('/set_carbon_emission', methods=['POST'])
def set_carbon_emission_flask():
    user_id = request.form['user_id']
    total_electricity = request.form['total_electricity']
    total_gas = request.form['total_gas']
    user_object = User(user_id)
    calculation_object = calculations.calculation(kwh_electricity=total_electricity, kwh_gas=total_gas)
    carbon_emission = calculation_object.calculate_co2_overall()
    user_object.set_carbon_emission(carbon_emission=carbon_emission)
    if sqlMessenger.update_carbon_emission(user_object):
        return jsonify({'status': 'success'})
    else:
        return jsonify({'status': 'failure'})

@app.route('/get_kwh_total', methods=['GET'])
def get_kwh_total_flask():
    user_id = request.form['user_id']
    user_object = User(user_id)
    user_object.set_kwh_total(sqlMessenger.get_kwh_total_from_db(user_id))
    if user_object.get_kwh_total():
        return jsonify({'status': 'success', 'kwh_total': user_object.get_kwh_total()})
    else:
        return jsonify({'status': 'failure'})

@app.route('/set_kwh_total', methods=['POST'])
def set_kwh_total_flask():
    user_id = request.form['user_id']
    kwh_electricity = request.form['kwh_electricity']
    kwh_gas = request.form['kwh_gas']
    user_object = User(user_id)
    user_object.set_kwh_total(int(kwh_electricity) + int(kwh_gas))
    if sqlMessenger.update_kwh_total(user_object):
        return jsonify({'status': 'success'})
    else:
        return jsonify({'status': 'failure'})

@app.route('/get_kwh_electricity_total', methods=['GET'])
def get_kwh_electricity_flask():
    user_id = request.form['user_id']
    user_object = User(user_id)
    user_object.set_kwh_electricity_total(sqlMessenger.get_user_kwh_electricity_from_db(userObject=user_object))
    if user_object.get_kwh_electricity_total():
        return jsonify({'status': 'success', 'kwh_electricity': user_object.get_kwh_electricity_total()})
    else:
        return jsonify({'status': 'failure'})

@app.route('/set_kwh_electricity_total', methods=['POST'])
def set_kwh_electricity_flask():
    user_id = request.form['user_id']
    kwh_electricity = request.form['kwh_electricity_total']
    user_object = User(user_id)
    user_object.set_kwh_electricity_total(kwh_electricity)
    if sqlMessenger.update_user_kwh_electricity(user_object):
        return jsonify({'status': 'success'})
    else:
        return jsonify({'status': 'failure'})

@app.route('/set_kwh_gas_total', methods=['POST'])
def set_kwh_gas_flask():
    user_id = request.form['user_id']
    kwh_gas = request.form['kwh_gas']
    user_object = User(user_id)
    user_object.set_kwh_gas(kwh_gas)
    if sqlMessenger.update_user_kwh_gas(user_object):
        return jsonify({'status': 'success'})
    else:
        return jsonify({'status': 'failure'})

@app.route('/get_kwh_gas_total', methods=['GET'])
def get_kwh_gas_flask():
    user_id = request.form['user_id']
    user_object = User(user_id)
    user_object.set_kwh_gas_total(sqlMessenger.get_user_kwh_gas_from_db(userObject=user_object))
    if user_object.get_kwh_gas_total():
        return jsonify({'status': 'success', 'kwh_gas': user_object.get_kwh_gas_total()})
    else:
        return jsonify({'status': 'failure'})

@app.route('/get_location', methods=['GET'])
def get_location_flask():
    user_id = request.form['user_id']
    user_object = User(user_id)
    user_object.set_location(sqlMessenger.get_user_location_from_db(userObject=user_object))
    if user_object.get_location():
        return jsonify({'status': 'success', 'location': user_object.get_location()})
    else:
        return jsonify({'status': 'failure'})

@app.route('/set_location', methods=['POST'])
def set_location_flask():
    user_id = request.form['user_id']
    location = request.form['location']
    user_object = User(user_id)
    user_object.set_location(location)
    if sqlMessenger.update_user_location(user_object):
        return jsonify({'status': 'success'})
    else:
        return jsonify({'status': 'failure'})

 #########################################################################

@app.route('/set_kwh_electricity', methods=['POST'])
def set_kwh_electricity_flask():
    user_id = request.form['user_id']
    home_id = request.form['home_id']
    kwh_electricity = request.form['kwh_electricity']
    user_object = User(user_id=user_id)
    home_object = household(home_id=home_id)
    home_object.set_kwh_electricity(kwh_electricity)
    if sqlMessenger.update_home_kwh_electricity(user_object):
        return jsonify({'status': 'success'})
    else:
        return jsonify({'status': 'failure'})


@app.route('/set_kwh_gas', methods=['POST'])
def set_kwh_gas_flask():
    user_id = request.form['user_id']
    kwh_gas = request.form['kwh_gas']
    user_object = User(user_id)
    user_object.set_kwh_gas(kwh_gas)
    if sqlMessenger.update_user_kwh_gas(user_object):
        return jsonify({'status': 'success'})
    else:
        return jsonify({'status': 'failure'})

@app.route('/get_house_type', methods=['GET'])
def get_house_type_flask():
    user_id = request.form['user_id']
    user_object = User(user_id)
    user_object.set_householdType(sqlMessenger.get_user_house_type_from_db(userObject=user_object))
    if user_object.get_householdType():
        return jsonify({'status': 'success', 'house_type': user_object.get_householdType()})
    else:
        return jsonify({'status': 'failure'})

@app.route('/set_house_type', methods=['POST'])
def set_house_type_flask():
    house_id = request.form['house_id']
    house_type = request.form['house_type']
    if sqlMessenger.update_house_type(house_id=house_id, house_type=house_type):
        return jsonify({'status': 'success'})
    else:
        return jsonify({'status': 'failure'})

@app.route('/get_number_of_rooms', methods=['GET'])
def get_number_of_rooms_flask():
    user_id = request.form['user_id']
    household_object = User(user_id)
    household_object.set_number_of_rooms(sqlMessenger.get_user_room_number_from_db(houseObject=household_object))
    if household_object.get_numberOfRooms():
        return jsonify({'status': 'success', 'number_of_rooms': household_object.get_numberOfRooms()})
    else:
        return jsonify({'status': 'failure'})

@app.route('/set_number_of_rooms', methods=['POST'])
def set_number_of_rooms_flask():
    house_id = request.form['house_id']
    number_of_rooms = request.form['number_of_rooms']
    household_object = household(house_id)
    household_object.set_numberOfRooms(number_of_rooms)
    if sqlMessenger.update_house_room_number(household_object):
        return jsonify({'status': 'success'})
    else:
        return jsonify({'status': 'failure'})

@app.route('/get_heating_type', methods=['GET'])
def get_heating_type_flask():
    house_id = request.form['house_id']
    household_object = household(house_id)
    household_object.set_heating_type(sqlMessenger.get_user_heating_type_from_db(houseObject=household_object))
    if household_object.set_heating_type():
        return jsonify({'status': 'success', 'heating_type': household_object.get_heating_type()})
    else:
        return jsonify({'status': 'failure'})

@app.route('/set_heating_type', methods=['POST'])
def set_heating_type_flask():
    home_id = request.form['home_id']
    heating_type = request.form['heating_type']
    house_object = household(home_id)
    house_object.set_heatingType(heating_type)
    if sqlMessenger.update_user_heating_type(house_object.get_user_id(), house_object.get_heatingType()):
        return jsonify({'status': 'success'})
    else:
        return jsonify({'status': 'failure'})

@app.route('/get_insulation', methods=['GET'])
def get_insulation_flask():
    house_id = request.form['user_id']
    house_object = household(house_id)
    house_object.set_insulation(sqlMessenger.get_user_insulation_from_db(userObject=house_object))
    if house_object.get_insulation():
        return jsonify({'status': 'success', 'insulation': house_object.get_insulation()})
    else:
        return jsonify({'status': 'failure'})

@app.route('/set_insulation', methods=['POST'])
def set_insulation_flask():
    house_id = request.form['user_id']
    insulation = request.form['insulation']
    house_object = household(house_id)
    house_object.set_insulation(insulation)
    if sqlMessenger.update_insulation(house_object):
        return jsonify({'status': 'success'})
    else:
        return jsonify({'status': 'failure'})














if __name__ == '__main__':
    app.run(debug=True)

