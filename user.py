from calculations import calculation


class User:

    def __init__(self, user_id=None, name=None, carbon_emission=None, kwh_total=None,location=None, kwh_electricity_total=None, kwh_gas_total=None, homes=None):
        self.user_id = user_id
        self.name = name
        self.carbon_emission = carbon_emission
        self.kwh_total = kwh_total
        self.location = location
        self.kwh_electricity_total = kwh_electricity_total
        self.kwh_gas_total = kwh_gas_total
        self.homes = homes



    ''' Get all of the attributes belong to user object within an array format '''

    def dump_user_attributes(self):
        return tuple((self.get_user_id, self.get_kwh_total,self.get_carbon_emission, self.get_location))

    ''' Create getter and setter functions'''

  # Setters 

    def set_user_id(self, user_id):
        self.user_id = user_id

    def set_name(self, name):
        self.name = name

    def set_kwh_total(self, kwh_total):
        self.kwh_total = kwh_total

    def set_carbon_emission(self, carbon_emission):
        self.carbon_emission = carbon_emission

    def set_location(self, location):
        self.location = location

    def set_kwh_electricity_total(self, kwh_electricity_total):
        self.kwh_electricity_total = kwh_electricity_total

    def set_kwh_gas_total(self, kwh_gas_total):
        self.kwh_gas_total = kwh_gas_total

    def set_user_homes(self, homes):
        self.homes = homes
  # Getters 

    def get_user_id(self):
        return self.user_id

    def get_name(self):
        return self.name

    def get_kwh_total(self):
        return self.kwh_total

    def get_carbon_emission(self):
        return self.carbon_emission

    def get_location(self):
        return self.location

    def get_kwh_electricity_total(self):
        return self.kwh_electricity_total

    def get_kwh_gas_total(self):
        return self.kwh_gas_total

    def get_user_homes(self):
        return self.homes
