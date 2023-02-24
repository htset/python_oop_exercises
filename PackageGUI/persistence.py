import os
from derived import AdvancedPackage, BasePackage, OvernightPackage

class Persistence:
    def __init__(self, packages) -> None:
        self.packages = packages
        
    def save_to_file(self):
        file = open('packages.txt', 'w')
        for p in self.packages:
            file.write(p.serialize())
        file.close()
            
    def load_from_file(self):
        try:
            if not os.path.isfile('packages.txt'):
                return

            file = open('packages.txt', 'r')
            package_str = ""
            lines = file.readlines()
            for line in lines:
                if line == "---\n":
                    if package_str.find("BasePackage") >= 0:
                        p = BasePackage()
                        p.deserialize(package_str)
                        self.packages.append(p)
                    elif package_str.find("AdvancedPackage") >= 0:
                        p = AdvancedPackage()
                        p.deserialize(package_str)
                        self.packages.append(p)
                    elif package_str.find("OvernightPackage") >= 0:
                        p = OvernightPackage()
                        p.deserialize(package_str)
                        self.packages.append(p)
                    package_str = ""
                else:
                    package_str = package_str + line

        except Exception as ex:
            print("error loading file")
                