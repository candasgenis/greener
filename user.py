from calculations import calculation


class User:

    def __init__(self, user_id=None, carbon_emission=None, kwh_total=None, kwh_electricity=None, kwh_gas=None,
                 location=None, householdType=None, numberOfRooms=None, heatingType=None,
                 insulation=None):
        self.user_id = user_id
        self.carbon_emission = carbon_emission
        self.kwh_total = kwh_total
        self.kwh_electricity = kwh_electricity
        self.kwh_gas = kwh_gas
        self.location = location
        self.householdType = householdType
        self.numberOfRooms = numberOfRooms
        self.heatingType = heatingType
        self.insulation = insulation




    ''' Get all of the attributes belong to user object within an array format '''

    def dump_user_attributes(self):
        return tuple((self.get_user_id, self.get_kwh_total, self.get_kwh_electricity, self.get_kwh_gas,
                      self.get_carbon_emission, self.get_location,
                    self.get_householdType, self.get_numberOfRooms, self.get_heatingType,
                    self.get_insulation))

    ''' Create getter and setter functions'''

    def set_user_id(self, user_id):
        self.user_id = user_id

    def set_kwh_total(self, kwh_total):
        self.kwh_total = kwh_total

    def set_kwh_electricity(self, kwh_electricity):
        self.kwh_electricity = kwh_electricity

    def set_kwh_gas(self, kwh_gas):
        self.kwh_gas = kwh_gas

    def set_carbon_emission(self, carbon_emission):
        self.carbon_emission = carbon_emission

    def set_location(self, location):
        self.location = location

    def set_householdType(self, householdType):  # householdType
        self.householdType = householdType

    def set_numberOfRooms(self, numberOfRooms):
        self.numberOfRooms = numberOfRooms

    def set_heatingType(self, heatingType):
        self.heatingType = heatingType

    def set_insulation(self, insulation):
        self.insulation = insulation

    def get_user_id(self):
        return self.user_id

    def get_kwh_total(self):
        return self.kwh_total

    def get_kwh_electricity(self):
        return self.kwh_electricity

    def get_kwh_gas(self):
        return self.kwh_gas

    def get_carbon_emission(self):
        return self.carbon_emission

    def get_location(self):
        return self.location

    def get_householdType(self):
        return self.householdType

    def get_numberOfRooms(self):
        return self.numberOfRooms

    def get_heatingType(self):
        return self.heatingType

    def get_insulation(self):
        return self.insulation
