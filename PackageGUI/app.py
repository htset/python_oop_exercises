from persistence import Persistence
from ui import UI

class App:   
    def __init__(self) -> None:
        self.packages = []
        self.persistence = Persistence(self.packages)
        self.ui = UI(self.packages, self.persistence)

if __name__ == "__main__":
    app = App()