class Tesla:
    def __init__(self, model: str, color: str, autopilot: bool = False) -> None:
      self.__unlock_count = 0
      self.__model = model
      self.__color = color
      self.__battery_charge = 99.9
      self.__is_locked = True
      self.__seats_count = 5
      self.__autopilot = autopilot
      self.__open_doors = "Car is locked!"
      self.__efficiency = 0.3

    def welcome(self) -> str:
        raise NotImplementedError

    @property
    def getColor(self) -> str:
        return self.__color
    @property
    def getModel(self) -> str:
        return self.__model
    @property
    def seats_count(self) -> str:
        return self.__seats_count

    @seats_count.setter
    def seats_count(self, new_count: str) -> str:
        self.__seats_count = new_count

    def autopilot(self, obsticle: str) -> str:
        # COMPLETE THE FUNCION
        if self.__autopilot:
          return f"Tesla model {self.__model} avoids {obsticle}"
        return "Autopilot is not available"

    def unlock(self) -> str:
      self.__unlock_count = 1

    def lock(self) -> str:
      self.__unlock_count = 0

    def open_doors(self):
      if self.__unlock_count == 0:
        return "Car is locked!"
      else:
        return "Doors opens sideways"

    def check_battery_level(self) -> str:
        return f"Battery charge level is {self.__battery_charge}%"

    def charge_battery(self) -> str:
        self.__battery_charge = 100
        return f"Battery charge level is {self.__battery_charge}%"

    def drive(self, travel_range: float):
        battery_discharge_percent = travel_range * self.__efficiency
        if self.__battery_charge - battery_discharge_percent >= 0:
          self.__battery_charge -= battery_discharge_percent
          return f"Battery charge level is {self.__battery_charge}%"
        else:
          return "Battery charge level is not sufficient"
