class household:

    def __init__(self,home_id,house_type = "Undefined",number_of_rooms = 0.0,heating_type = "Undefined",insulation = "Undefined",kwh_electricity = 0.0,kwh_gas = 0.0,kwh_total = 0.0, carbon_emission=0.0):
        self.house_type = house_type
        self.number_of_rooms = number_of_rooms
        self.heating_type = heating_type
        self.insulation = insulation
        self.kwh_electricity = kwh_electricity
        self.kwh_gas = kwh_gas
        self.kwh_total = kwh_total
        self.home_id = home_id
        self.carbon_emission = carbon_emission

    """ Generate getters and setters belongs to household class """ 

    def set_carbon_emission(self, carbon_emission):
        self.carbon_emission = carbon_emission
    
    def set_house_type(self, house_type):
        self.house_type = house_type

    def set_number_of_rooms(self, number_of_rooms):
        self.number_of_rooms = number_of_rooms

    def set_heating_type(self, heating_type):
        self.heating_type = heating_type

    def set_insulation(self, insulation):
        self.insulation = insulation

    def set_kwh_electricity(self, kwh_electricity):
        self.kwh_electricity = kwh_electricity

    def set_kwh_gas(self, kwh_gas):
        self.kwh_gas = kwh_gas

    def set_kwh_total(self, kwh_total):
        self.kwh_total = kwh_total

    def set_home_id(self, home_id):
        self.home_id = home_id

    # Getters 

    def get_carbon_emission(self):
        return self.carbon_emission

    def get_house_type(self):
        return self.house_type

    def get_number_of_rooms(self):
        return self.number_of_rooms

    def get_heating_type(self):
        return self.heating_type

    def get_insulation(self):
        return self.insulation

    def get_kwh_electricity(self):
        return self.kwh_electricity

    def get_kwh_gas(self):
        return self.kwh_gas

    def get_kwh_total(self):
        return self.kwh_total

    def get_home_id(self):
        return self.home_id