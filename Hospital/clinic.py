class Clinic:
    def __init__(self, name, director) -> None:
        self.name = name
        self.director = director
    
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def director(self):
        return self._director

    @director.setter
    def director(self, value):
        self._director = value

    def __str__(self) -> str:
        return "Clinic name: " + str(self.name) + ", director: " + str(self.director)