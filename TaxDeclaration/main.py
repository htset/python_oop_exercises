from file_service import FileService
from db_service import DbService
from statistics_service import StatisticsService
from ui_service import UIService

def main():
    ps = FileService()
    #ps = DbService()
    ss = StatisticsService(ps)
    ui = UIService(ps, ss)

    ui.menu()

if __name__ == "__main__":
    main()  