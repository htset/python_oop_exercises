import tkinter as tk
from tkinter import messagebox, ttk
from datetime import date, datetime
from derived import AdvancedPackage, BasePackage, OvernightPackage

class UI:   
    def __init__(self, packages, persistence) -> None:
        self.packages = packages
        self.persistence = persistence
        self.persistence.load_from_file()

        self.window = tk.Tk()
        self.window.title("Packages")

        self.notebook = ttk.Notebook(self.window)
        self.notebook.pack(pady=10, expand=True)

        self.frame1 = ttk.Frame(self.notebook, width=400, height=280)
        self.frame1.pack(fill='both', expand=True)

        self.frame2 = ttk.Frame(self.notebook, width=400, height=280)
        self.frame2.pack(fill='both', expand=True)
        
        self.populate_frame1()
        self.populate_frame2()

        #add frames to two tabs of the notebook
        self.notebook.add(self.frame1, text='Package List')
        self.notebook.add(self.frame2, text='Add new Package')

        self.window.mainloop()

    def populate_frame1(self):
        #empty package list first
        for widget in self.frame1.winfo_children():
            widget.destroy()

        #table headers
        tk.Label(self.frame1, text="Package Type").grid(row=0, column=0)
        tk.Label(self.frame1, text="Recipient").grid(row=0, column=1)
        tk.Label(self.frame1, text="Address").grid(row=0, column=2)
        tk.Label(self.frame1, text="Weight").grid(row=0, column=3)
        tk.Label(self.frame1, text="Shipment Date").grid(row=0, column=4)

        #table rows
        current_row = 1
        for pk in self.packages:
            if isinstance(pk, BasePackage): 
                tk.Label(self.frame1, text="Base").grid(row=current_row, column=0)
            elif isinstance(pk, AdvancedPackage): 
                tk.Label(self.frame1, text="Advanced").grid(row=current_row, column=0)
            elif isinstance(pk, OvernightPackage): 
                tk.Label(self.frame1, text="Overnight").grid(row=current_row, column=0)

            tk.Label(self.frame1, text=pk.recipient).grid(row=current_row, column=1)
            tk.Label(self.frame1, text=pk.address).grid(row=current_row, column=2)
            tk.Label(self.frame1, text=pk.weight).grid(row=current_row, column=3)
            tk.Label(self.frame1, text=pk.shipment_date).grid(row=current_row, column=4)
            current_row += 1

    def populate_frame2(self):
        #options of the drop-down list
        options = [
            "Base",
            "Advanced",
            "Overnight"
        ] 

        #labels and input boxes
        selectedPackage = tk.StringVar()
        selectedPackage.set( "Base" )
        lblPackageType = tk.Label(self.frame2, text="Package Type")
        lblPackageType.grid(row=0, column=0)
        optPackageType = tk.OptionMenu(self.frame2, selectedPackage , *options )
        optPackageType.grid(row=0, column=1)

        valRecipient = tk.StringVar()
        lblRecipient = tk.Label(self.frame2, text="Recipient")
        lblRecipient.grid(row=1, column=0)
        entRecipient = tk.Entry(self.frame2, textvariable=valRecipient)
        entRecipient.grid(row=1, column=1)

        valAddress = tk.StringVar()
        lblAddress = tk.Label(self.frame2, text="Address")
        lblAddress.grid(row=2, column=0)
        entAddress = tk.Entry(self.frame2, textvariable=valAddress)
        entAddress.grid(row=2, column=1)

        valWeight = tk.IntVar()
        lblWeight = tk.Label(self.frame2, text="Weight")
        lblWeight.grid(row=3, column=0)
        entWeight = tk.Entry(self.frame2, textvariable=valWeight)
        entWeight.grid(row=3, column=1)

        valShipmentDate = tk.StringVar()
        lblShipmentDate = tk.Label(self.frame2,text="Shipment Date (YYYY-MM-DD)")
        lblShipmentDate.grid(row=4, column=0)
        entShipmentDate = tk.Entry(self.frame2, textvariable=valShipmentDate)
        entShipmentDate.grid(row=4, column=1)

        def add_package():
            #this function is called when the button is clicked
            try:
                #get input values from Stringvar and Intvar objects
                package_type = selectedPackage.get()
                recipient = valRecipient.get()
                address = valAddress.get()
                weight = int(valWeight.get())
                shipment_date = datetime.strptime(valShipmentDate.get(), \
                    '%Y-%m-%d').date()

                if(package_type == "Base"):
                    self.packages.append(BasePackage(recipient, address, \
                        weight, shipment_date))
                    self.persistence.save_to_file()
                elif(package_type == "Advanced"):
                    self.packages.append(AdvancedPackage(recipient, address, \
                        weight, shipment_date))
                    self.persistence.save_to_file()
                elif(package_type == "Overnight"):
                    self.packages.append(OvernightPackage(recipient, address, \
                        weight, shipment_date))
                    self.persistence.save_to_file()
            except ValueError as ex:
                messagebox.showinfo(message='Error: ' + str(ex))
                return

            messagebox.showinfo("Message", "Package added successfully")

            #empty input boxes
            valRecipient.set("")
            valAddress.set("")
            valWeight.set("")
            valShipmentDate.set("")

            #re-populate package list and switch to first tab
            self.populate_frame1()
            self.notebook.select(self.frame1)

        btnAddP = tk.Button(self.frame2, text="Add package", command=add_package)
        btnAddP.grid(row=5, column=0)
