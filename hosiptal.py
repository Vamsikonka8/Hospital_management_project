from tkinter import *
from tkinter import ttk
import random
import time
import datetime
from tkinter import messagebox
import mysql.connector

class hospital():
    def __init__(self , root):
        self.root = root
        self.root.title("Hospital Management System")
        self.root.geometry("1500x800+0+0")

        self.NameofTablets = StringVar()
        self.ref = StringVar()
        self.Dose = StringVar()
        self.NumberofTablets = StringVar()
        self.Lot = StringVar()
        self.Issuedate= StringVar()
        self.ExpDate = StringVar()
        self.DailyDose = StringVar()
        self.SideEffect = StringVar()
        self.FurtherInformation = StringVar()
        self.Storageadvice = StringVar()
        self.DrivingUsingMachine= StringVar()
        self.HowToUseMedication = StringVar()
        self.PatientId = StringVar()
        self.nhsNumber = StringVar()
        self.PatientName = StringVar()
        self.DateofBirth = StringVar()
        self.PatientAddress = StringVar()



        lbltitle = Label(self.root,bd=15,relief=RIDGE,text="+ Hospital Management System",fg="red",bg="white",font=("time new roman",30,"bold"))
        lbltitle.pack(side=TOP,fill=X)

        #===============================DataFrame++++++++++++++++++++++++

        dataframe = Frame(self.root,bd=15,padx=5, pady=5,relief=RIDGE)
        dataframe.place(x=0,y=85,width=1275,height=330)

        dataframeleft = LabelFrame(dataframe,bd=15, relief=RIDGE,
                                                            font=("time new roman",12,"bold"),text='Patient information')
        dataframeleft.place(x=0,y=0,width=880,height=290)


        dataframeright = LabelFrame(dataframe,bd=15,relief=RIDGE,
                                                            font=("time new roman",12,"bold"),text='prescription',padx=3 , pady= 4)
        dataframeright.place(x=890,y=0,width=340,height=290)

        # #================= button frame==============================================

        Buttonframe = Frame(self.root,bd=15,relief=RIDGE,padx=10 ,pady=2)
        Buttonframe.place(x=0,y=415,width=1275,height=60 )

        # # ========================= details frame =============================================
        
        detailframe = Frame(self.root,bd=20,relief=RIDGE)
        detailframe.place(x=0,y=475,width=1275,height=168)

        # ================== dataframele ft ========================================================

        lblNameTablet= Label(dataframeleft, font = ("arial",10,"bold"),text="Name of Tablets",padx=2, pady=4)
        lblNameTablet.grid(row=0,column=0,sticky=W)
       
        comNameTablet = ttk.Combobox(dataframeleft,textvariable=self.NameofTablets, state= "readonly",
                                     font=("arial",10,"bold") ,width=32)
        comNameTablet["value"] = ("Nice", "Corona Vaccine", "Acetimopheno", "Addrall", "Amodipine", "Ativan")
        comNameTablet.current(0)
        comNameTablet.grid(row=0,column=1)


        lblref = Label(dataframeleft, font=("arial", 10, "bold"),text="Reference No:",padx=2,pady= 4)
        lblref.grid(row=1,column=0,sticky=W)
        txtref = Entry(dataframeleft,font=("arial",12,"bold"),textvariable=self.ref,width=27)
        txtref.grid(row=1,column=1)


        lblDose = Label(dataframeleft, font=("arial", 10, "bold"),text="Dose:", padx=2,pady=4)
        lblDose.grid(row=2,column=0,sticky=W)
        txtDose = Entry(dataframeleft,font=("arial",12,"bold"), textvariable=self.Dose,width=27)
        txtDose.grid(row=2,column=1)


        lblNoOftablets = Label(dataframeleft, font=("arial", 10, "bold"),text="No of Tablets:", padx=2,pady=4)
        lblNoOftablets.grid(row=3,column=0,sticky=W)
        txtNoOftablets = Entry(dataframeleft,font=("arial",12,"bold"),textvariable=self.NumberofTablets, width=27)
        txtNoOftablets.grid(row=3,column=1)


        lblLot = Label(dataframeleft, font=("arial", 10, "bold"),text="Lot:", padx=2,pady=4)
        lblLot.grid(row=4,column=0,sticky=W)
        txtLot = Entry(dataframeleft,font=("arial",12,"bold"),textvariable=self.Lot,width=27)
        txtLot.grid(row=4,column=1)

        lblissueDate= Label(dataframeleft, font=("arial", 10, "bold"),text="Issue Date:", padx=2 ,pady=4)
        lblissueDate.grid(row=5,column=0,sticky=W)
        txtissueDate = Entry(dataframeleft,font=("arial",12,"bold"),textvariable=self.Issuedate, width=27)
        txtissueDate.grid(row=5,column=1)


        lblExpDate= Label(dataframeleft, font=("arial", 10, "bold"),text="Exp Date:", padx=2 ,pady=4)
        lblExpDate.grid(row=6,column=0,sticky=W)
        txtExpDate= Entry(dataframeleft,font=("arial",12,"bold"),textvariable=self.ExpDate, width=27)
        txtExpDate.grid(row=6,column=1)

        
        lblDailyDose = Label(dataframeleft, font=("arial", 10, "bold"),text="Daily Dose:", padx=2 ,pady=4)
        lblDailyDose.grid(row=7,column=0,sticky=W)
        txtDailyDose = Entry(dataframeleft,font=("arial",12,"bold"),textvariable=self.DailyDose,width=27)
        txtDailyDose.grid(row=7,column=1)

        lblSideEffect=Label(dataframeleft, font=("arial", 10, "bold"),text="Side Effect:", padx=2 ,pady=4)
        lblSideEffect.grid(row=8,column=0,sticky=W)
        txtSideEffect=Entry(dataframeleft,font=("arial",12,"bold"),textvariable=self.SideEffect,width=27)
        txtSideEffect.grid(row=8,column=1)


        lblFurtherinfo=Label(dataframeleft, font=("arial", 10, "bold"),padx=20,text= "Further Information:",pady=4)
        lblFurtherinfo.grid(row=0,column=2,sticky=W)
        txtFurtherinfo=Entry(dataframeleft,font=("arial",12,"bold"),textvariable=self.FurtherInformation,width=27)
        txtFurtherinfo.grid(row=0,column=3)


        lblBloodPressure=Label(dataframeleft, font=("arial", 10, "bold"),padx=20,text= "Blood Pressure:", pady=4)
        lblBloodPressure.grid(row=1,column=2,sticky=W)
        txtBloodPressure= Entry(dataframeleft,font=("arial",12,"bold"), textvariable=self.DrivingUsingMachine,width=27)
        txtBloodPressure.grid(row=1,column=3)


        lblStorage=Label(dataframeleft, font=("arial", 10, "bold"),padx=20,text="Storage Advise:", pady=4)
        lblStorage.grid(row=2,column=2,sticky=W)
        txtStorage=Entry(dataframeleft,font=("arial",12,"bold"),textvariable=self.Storageadvice, width=27)
        txtStorage.grid(row=2,column=3)

        lblMedicine = Label(dataframeleft, font=("arial", 10, "bold"),padx=20,text="Mediation:",pady=4)
        lblMedicine.grid(row=3,column=2,sticky=W)
        txtMedicine = Entry(dataframeleft,font=("arial",12,"bold"),textvariable=self.HowToUseMedication,width=27)
        txtMedicine.grid(row=3,column=3)


        lblPatientId= Label(dataframeleft, font=("arial", 10, "bold"),padx=20,text="Patient Id:", pady=4)
        lblPatientId.grid(row=4,column=2,sticky=W)
        txtPatientId= Entry(dataframeleft,font=("arial",12,"bold"), textvariable=self.PatientId,width=27)
        txtPatientId.grid(row=4,column=3)

        
        lblNhsNumber= Label(dataframeleft, font=("arial", 10, "bold"),padx=20,text="NHS Number:",pady=4)
        lblNhsNumber.grid(row=5,column=2,sticky=W)
        txtNhsNumber= Entry(dataframeleft,font=("arial",12,"bold"), textvariable=self.nhsNumber,width=27)
        txtNhsNumber.grid(row=5,column=3)


        lblPatientname= Label(dataframeleft, font=("arial", 10, "bold"),padx=20,text="Patient Name:",pady=4)
        lblPatientname.grid(row=6,column=2,sticky=W)
        txtPatientname= Entry(dataframeleft,font=("arial",12,"bold"),textvariable=self.PatientName, width=27)
        txtPatientname.grid(row=6,column=3)


        lblDateofBirth= Label(dataframeleft, font=("arial", 10, "bold"),padx=20,text="Date of Birth:",pady=4)
        lblDateofBirth.grid(row=7,column=2,sticky=W)
        txtDateofBirth= Entry(dataframeleft,font=("arial",12,"bold"), textvariable=self.DateofBirth, width=27)
        txtDateofBirth.grid(row=7,column=3)

        lblPatientAddress= Label(dataframeleft, font=("arial", 10, "bold"),padx=20,text="Patient Address:",pady=4)
        lblPatientAddress.grid(row=8,column=2,sticky=W)
        txtPatientAddress= Entry(dataframeleft,font=("arial",12,"bold"),textvariable=self.PatientAddress, width=27)
        txtPatientAddress.grid(row=8,column=3)


        # # =======================data frame right ===================================================

        self.txtprescription = Text(dataframeright,font=("arial",12,"bold"),width=30, height=12)
        self.txtprescription.grid(row=0, column=0)

        # # ============== button =========================================================

        btnprescription = Button(Buttonframe,text="Prescription",bg="green",font=("arial",12,"bold") ,fg="white",width=19, height=1,padx=2)
        btnprescription.grid(row=0, column=0)


        btnprescription_data= Button(Buttonframe,text="Prescription data",bg="green",font=("arial",12,"bold") ,fg="white",width=19,height=1)
        btnprescription_data.grid(row=0, column=1)

 
        btnupdate = Button(Buttonframe,text="Update",bg="green",font=("arial",12,"bold") ,fg="white",width=19, height=1)
        btnupdate.grid(row=0, column=2)


        btnDelete = Button(Buttonframe,text="Delete",bg="green",font=("arial",12,"bold") ,fg="white",width=19, height=1)
        btnDelete.grid(row=0, column=3)


        btnClear = Button(Buttonframe,text="Clear",bg="green",font=("arial",12,"bold") ,fg="white",width=19, height=1)
        btnClear.grid(row=0, column=4)


        btnExit = Button(Buttonframe,text="Exit",bg="green",font=("arial",12,"bold") ,fg="white",width=19, height=1)
        btnExit.grid(row=0, column=5)


        # #  =======================================scroll bar=================================================================================

        scroll_x = ttk.Scrollbar(detailframe, orient = HORIZONTAL)
        scroll_y = ttk.Scrollbar(detailframe, orient= VERTICAL)
        self.hospital_table = ttk.Treeview(detailframe,column= ("nameoftable", "ref", "dose", "nooftablets", "lot", "issuedate",
                                                                   "expdate", "dailydose", "storage", "nhsnumber", "pname", "dob", 'address'),xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM, fill = X)
        scroll_y.pack(side=RIGHT , fill = Y)

        scroll_x = ttk.Scrollbar(command=self.hospital_table.xview)
        scroll_y = ttk.Scrollbar(command=self.hospital_table.yview)

        self.hospital_table.heading("nameoftable",text="Name of Tablet")
        self.hospital_table.heading("ref",text="Reference No")
        self.hospital_table.heading("dose",text="Dose")
        self.hospital_table.heading("nooftablets",text="No of Tablets")
        self.hospital_table.heading("lot",text="Lot")
        self.hospital_table.heading("issuedate",text="Issue Date")
        self.hospital_table.heading("expdate",text="Exp Date")
        self.hospital_table.heading("dailydose", text="Daily Dose")
        self.hospital_table.heading("storage",text="Storage")
        self.hospital_table.heading("nhsnumber",text="NHS Number")
        self.hospital_table.heading("pname",text="Patient Name")
        self.hospital_table.heading("dob",text="DOB")
        self.hospital_table.heading("address",text="Address")

        self.hospital_table["show"] = "headings"


    
        self.hospital_table.column("nameoftable",width = 60)
        self.hospital_table.column("ref", width = 60)
        self.hospital_table.column("dose", width = 60)
        self.hospital_table.column("nooftablets", width = 60)
        self.hospital_table.column("lot", width = 60)
        self.hospital_table.column("issuedate", width = 60)
        self.hospital_table.column("expdate", width = 60)
        self.hospital_table.column("dailydose", width = 60)
        self.hospital_table.column("storage", width = 60)
        self.hospital_table.column("nhsnumber", width = 60)
        self.hospital_table.column("pname", width = 60)
        self.hospital_table.column("dob", width = 60)
        self.hospital_table.column("address", width = 60)

        self.hospital_table.pack(fill= BOTH, expand=1)


        def IperscriptionData(self):
            if self.NameofTablets.get()==""or self.ref.get()=="":
                messagebox.showerror("Error", "All Fields are  Required")
            else:
                conn = mysql.connector.connect(host="localhost", username="root", password="1234", database="db1" )
                my_cursor = conn.cursor()
                my_cursor.execute("insert into hospital values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.Nameoftablets.get(),
                                                                                                                    self.ref.get(),
                                                                                                                    self.Dose.get(),
                                                                                                                    self.Numberoftablets.get(),
                                                                                                                    self.Lot.get(),
                                                                                                                    self.Issuedate.get(),
                                                                                                                    self.ExpDate.get(),
                                                                                                                    self.DailyDose.get(),
                                                                                                            
                                                                                                                
                                                                                                                    self.Storageadvice.get(),
                                                                                                    
                                                                                                     
                                                                                                                    self.nhsNumber.get(),
                                                                                                                    self.PatientName.get(),
                                                                                                                    self.DateOfBirth.get(),
                                                                                                                    self.PatientAddress.get()

                                                                                                                ))
                
                conn.commit(IperscriptionData)
                conn.close()
                messagebox.showinfo(("Sucess , Record has been inserted"))
    

                

       

if __name__ == "__main__":
    root = Tk()
    obj = hospital(root)
    root.mainloop()


