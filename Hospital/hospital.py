from clinic import Clinic
from patient import Patient
from measurement import Measurement
from datetime import datetime

def main():
    c1 = Clinic("Surgery", "A. Dobbs")
    c2 = Clinic("Cardiology", "B. Smith")
    c3 = Clinic("Orthopedics", "C. Stubbs")

    p1 = Patient("John", "Doe", 1970, c1, "303")
    p2 = Patient("Jane", "Doe", 1985, c2, "306")
    p3 = Patient("Jimmy", "Doe", 1956, c2, "306")

    p1.insert_measurement(Measurement(37.5, datetime(2023, 1, 1, 3, 0)))
    p1.insert_measurement(Measurement(38.1, datetime(2023, 1, 1, 6, 0)))
    p1.insert_measurement(Measurement(37.9, datetime(2023, 1, 1, 9, 0)))

    p2.insert_measurement(Measurement(36.5, datetime(2023, 1, 1, 3, 0)))
    p2.insert_measurement(Measurement(38.0, datetime(2023, 1, 1, 6, 0)))

    p3.insert_measurement(39.5, datetime(2023, 1, 1, 3, 0))
    p3.insert_measurement(39.1, datetime(2023, 1, 1, 6, 0))

    p3.clinic = c3
    c1.director = "D. Jones"

    print(str(p1))
    print(str(p2))
    print(str(p3))


if __name__ == "__main__":
    main()