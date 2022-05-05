from calculations import calculation

class user:

    def __init__(self,user_id = None,kwh = None,location = None,householdType = None,numberOfRooms = None,heatingType = None,insulation = None):
        self.user_id = user_id
        self.kwh = kwh
        self.location = location
        self.householdType = householdType
        self.numberOfRooms = numberOfRooms
        self.heatingType = heatingType
        self.insulation = insulation


    def get_overall_kwh(kwh_electricity,kwh_gas): # Get overall KW/h for specified user object. 
        calculation_object = calculation(kwh_electricity,kwh_gas)
        return calculation_object.calculate_co2_overall()

    ''' Get all of the attributes belong to user object within an array format '''
    def dump_user_attributes(self):
        return list(self.get_user_id, self.get_overall_kwh, self.get_location,
                    self.get_householdType,self.get_numberOfRooms,self.get_heatingType,
                    self.get_insulation)
        
    ''' Create getter and setter functions'''

    def set_user_id(self,user_id):
        self.user_id = user_id

    def set_kwh(self,kwh):
        self.kwh = kwh

    def set_location(self,location):
        self.location = location

    def set_householdType(self,householdType):  #householdType
        self.householdType = householdType

    def set_numberOfRooms(self,numberOfRooms):
        self.numberOfRooms = numberOfRooms

    def set_heatingType(self,heatingType):
        self.heatingType = heatingType

    def set_insulation(self,insulation):
        self.insulation = insulation

    def get_user_id(self):
        return self.user_id

    def get_kwh(self):      #kwh
        return self.kwh 

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




    