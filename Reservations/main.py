from persistence import PersistenceService
from ui import UIService

def main():
    ps = PersistenceService()
    ui = UIService(ps)
    ui.menu()

if __name__ == "__main__":
    main()
