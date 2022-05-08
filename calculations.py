class calculation:

    def __init__(self, kwh_electricity, kwh_gas):
        self.kwh_electricity = kwh_electricity
        self.kwh_gas = kwh_gas

    def calculate_co2_emissions_electricity(self):
        constant = 0.553
        return float(self.kwh_electricity) * constant

    def calculate_co2_emissions_gas(self):
        constant = 0.553
        return float(self.kwh_gas) * constant

    def calculate_co2_overall(self):
        return self.calculate_co2_emissions_electricity() + self.calculate_co2_emissions_gas()

    def calculate_co2_tonne(self):
        return self.calculate_co2_overall() / 1000

    def set_kwh_electricity(self, kwh_electricity):
        self.kwh_electricity = kwh_electricity

    def set_kwh_gas(self, kwh_gas):
        self.kwh_gas = kwh_gas

    def get_kwh_electricity(self):
        return self.kwh_electricity

    def get_kwh_gas(self):
        return self.kwh_gas
