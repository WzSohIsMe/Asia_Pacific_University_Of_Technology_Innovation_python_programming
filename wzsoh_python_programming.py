#SOH WEI ZHENG
#TP063631

patientDetails = []
vaccinationDetails= []

def writingTo():
    #writing List to patient.txt
    def writingListToPatient():
        try:
            with open("patient.txt","w") as patient_FileHandler:
                for patient in patientDetails:
                    patient_FileHandler.write(patient[0])
                    for detail in patient[1:]:
                        patient_FileHandler.write(","+str(detail))
                    patient_FileHandler.write("\n")
            patient_FileHandler.close()
        except:
            print("File cannot be opened. \n")
            exit(writingTo())

    #writing List To vaccination.txt
    def writingListToVaccination():
        try:
            with open("vaccination.txt","w") as vaccination_FileHandler:
                for patient in vaccinationDetails:
                    vaccination_FileHandler.write(patient[0])
                    for detail in patient[1:]:
                        vaccination_FileHandler.write(","+str(detail))
                    vaccination_FileHandler.write("\n")
                vaccination_FileHandler.close()
        except:
            print("File cannot be opened. \n")
            exit(writingTo())

    writingListToPatient()
    writingListToVaccination()

def convert():
    #writing patient.txt to patientDetails = []
    def listPatientDetails():
        patientDetails.clear()
        try:
            patient_FileHandler = open("patient.txt","r")
            patient = patient_FileHandler.readlines()

            for line in patient:
                patientDetails.append(line.strip().split(","))
            patient_FileHandler.close()
        except:
            print("File cannot be opened. \n")
            exit(convert())

    #writing vaccination.txt to vaccinationDetails = []
    def listVaccinationDetails():#convert
        vaccinationDetails.clear()
        try:
            vaccination_FileHandler = open("vaccination.txt","r")
            vaccination = vaccination_FileHandler.readlines()

            for line in vaccination:
                vaccinationDetails.append(line.strip().split(","))
            vaccination_FileHandler.close()
        except:
            print("File cannot be opened. \n")
            exit(convert())

    listPatientDetails()
    listVaccinationDetails()

def newPatientRegistration():
    convert()
    dose1 = False
    dose2 = False

    #New Patient Registration
    print("-"*80,"\n1. New Patient Registration","\n"+"-"*80)
    print("You have entered to the new patient registration.\n")
    print("-"*30+'Patient Details'+"-"*30)
    vaccinationCentre = input("Choose a vacination centre [VC1/VC2]: ")
    if vaccinationCentre == 'vc1' or 'Vc1' or 'vC1' or '1':
        vaccinationCentre = 'VC1'
    elif vaccinationCentre == 'vc2' or 'Vc2' or 'vC2' or '2':
        vaccinationCentre = 'VC2'
    else:
        print("Invalid Input. Please choose the vaccination centre properly. \n")
        exit(newPatientRegistration())
    patientName = input("Enter name: ")
    patientContact = input("Enter contact numbers: ")

    #try except for patientAge, prevent the program crashing when users input letters in their age
    try:
        patientAge = int(input("Enter your age: "))
    except ValueError:
        print("Invalid Input. Please enter your age properly. \n")
        exit(newPatientRegistration())

    def vaccineCode(patientAge):
        #a bunch of available vaccine code
        list_vaccineCode = ["AF","BV","CZ","DM","EC"] #allvaccine
        list_availableVaccinefor12Above = ["AF","CZ","DM"] #12above
        list_availableVaccinefor18Above = ["BV","CZ","EC"] #18above
        list_availableVaccinefor45Above = ["AF","BV","DM","EC"] #45above
        list_availableVaccinefor12Below = 'No avaibale vaccine below 12 years old.' #12below
        count = 0
        print("-"*20+"Vaccine Codes"+"-"*20)
        if (patientAge >= 45):
            print("Your available vaccine codes are: ")
            for vccode in list_availableVaccinefor45Above:
                print(count+1,'.',vccode)
                count+=1
            vcCodeOption = input("Choose your vaccine code: ")
            if(vcCodeOption=='1')or(vcCodeOption==list_availableVaccinefor45Above[0]):
                vcCodeOption = list_availableVaccinefor45Above[0]

            elif(vcCodeOption=='2')or(vcCodeOption==list_availableVaccinefor45Above[1]):
                vcCodeOption = list_availableVaccinefor45Above[1]

            elif(vcCodeOption=='3')or(vcCodeOption==list_availableVaccinefor45Above[2]):
                vcCodeOption = list_availableVaccinefor45Above[2]

            elif(vcCodeOption=='4')or(vcCodeOption==list_availableVaccinefor45Above[3]):
                    vcCodeOption = list_availableVaccinefor45Above[3]

            print("You have chosen",vcCodeOption+'.\n')
            return vcCodeOption
        elif(patientAge >=18):
            print("Your available vaccine codes are: ")
            for vccode in list_availableVaccinefor18Above:
                print(count+1,'.',vccode)
                count+=1
            vcCodeOption = input("Choose your vaccine code: ")
            if(vcCodeOption=='1')or(list_availableVaccinefor18Above[0]):
                vcCodeOption = list_availableVaccinefor18Above[0]

            elif(vcCodeOption=='2')or(vcCodeOption==list_availableVaccinefor18Above[1]):
                vcCodeOption = list_availableVaccinefor18Above[1]

            elif(vcCodeOption=='3')or(vcCodeOption==list_availableVaccinefor18Above[2]):
                vcCodeOption = list_availableVaccinefor18Above[2]

            print("You have chosen",vcCodeOption+'.\n')
            return vcCodeOption

        elif(patientAge >= 12):
            print("Your available vaccine codes are: ")
            for vccode in list_availableVaccinefor12Above:
                print(count+1,'.',vccode)
                count+=1
            vcCodeOption = input("Choose your vaccine code: ")
            if(vcCodeOption=='1')or(list_availableVaccinefor12Above[0]):
                vcCodeOption = list_availableVaccinefor12Above[0]

            elif(vcCodeOption=='2')or(vcCodeOption==list_availableVaccinefor12Above[1]):
                vcCodeOption = list_availableVaccinefor12Above[1]

            elif(vcCodeOption=='3')or(vcCodeOption==list_availableVaccinefor12Above[2]):
                vcCodeOption = list_availableVaccinefor12Above[2]

            print("You have chosen",vcCodeOption+'.\n')
            return vcCodeOption

        elif(patientAge <= 12) and (patientAge>=0):
            print(list_availableVaccinefor12Below)
            return None
        else:
            print("Error at choosing vaccine code. Please insert details properly. \n")
            exit(newPatientRegistration())

    #patientID Generator
    def patientID():
        patientNum = 0
        start=0
        for i in range(start,(len(patientDetails)+1)):
            patientNum += 1
        patientIDgen = 'VC' + '_' + str(patientNum)
        return patientIDgen


    #PROGRAM STARTS HERE
    if patientAge>=12:
        patientID = patientID()
        vaccineCode = vaccineCode(patientAge)
        print("Your ID is",patientID,"\n")

        patientDetails.append([patientID,patientName,patientAge,vaccinationCentre,patientContact,vaccineCode,dose1,dose2])
        vaccinationDetails.append([patientID,vaccineCode,dose1,dose2])

        try:
            with open("patient.txt","a") as patient_FileHandler:
                patient_FileHandler.write(f"{patientID},{patientName},{patientAge},{vaccinationCentre},{patientContact},{vaccineCode},{dose1},{dose2}\n")
                patient_FileHandler.close()
        except:
            print("File cannot be opened. \n")
            exit()

        try:
            with open("vaccination.txt","a") as vaccination_FileHandler:
                vaccination_FileHandler.write(f"{patientID},{vaccineCode},{dose1},{dose2}\n")
                vaccination_FileHandler.close()
        except:
            print("File cannot be opened. \n")
            exit()

        print("Your data has been recorded. \n")
    elif patientAge<=12:
        print("No vaccination below 12 years old. \n")
    else:
        print("Error at registering age. \n")

def vaccineAdministration():
    convert()
    patientID = input("Enter your ID: ")
    print()
    def vacWeekDisplay():
        #vaccine week
        week_AF = 'Please register for dose 2 after 2 weeks (or 14 days).\n'
        week_BV = 'Please register for dose 2 after 3 weeks (or 21 days).\n'
        week_CZ = 'Please register for dose 2 after 3 weeks (or 21 days).\n'
        week_DM = 'Please register for dose 2 after 4 weeks (or 28 days).\n'
        week_EC = 'You have completed your vaccination. '
        for patient in vaccinationDetails:
            if(patient[0]==patientID):
                if(patient[1]=='AF'):
                    return week_AF
                elif(patient[1] =='BV'):
                    return week_BV
                elif(patient[1] == 'CZ'):
                    return week_CZ
                elif(patient[1] == 'DM'):
                    return week_DM
                else:
                    return week_EC
        else:
            print("Error at showing weeks")

    #replace False to True
    for patient in vaccinationDetails:
        if patient[0]==patientID:
            if patient[-2]=='False':
                if patient[1] == 'EC':
                    option = input("Do you want to register for EC [yes/no]?")
                    print()
                    if(option=='yes'):
                        patient[-2]=True
                        patient[-1]=True
                        for patient in patientDetails:
                            if patient[0]==patientID:
                                patient[-2]=True
                                patient[-1]=True
                        print(vacWeekDisplay())
                        writingTo()
                        print("Your data has been updated. \n")

                else:
                    option = input("Do you want to register for dose 1 [yes/no]: ")
                    print()
                    if(option=='yes'):
                        patient[-2]=True
                        for patient in patientDetails:
                            if patient[0]==patientID:
                                patient[-2]=True
                        print("You have registered for dose 1. \n")
                        print(vacWeekDisplay())
                        writingTo()
                        print("Your data has been updated. \n")

            elif patient[-1]=='False':
                option = input("Do you want to register for dose 2 [yes/no]: ")
                print()
                if(option=='yes'):
                    patient[-1]=True
                    for person in patientDetails:
                        if person[0]==patientID:
                            person[-1]=True

                    print("You have registered for dose 2. \n")
                    writingTo()
                    print("Your data has been updated. \n")
            else:
                print("You have registered for dose 1 and dose 2. \n")
            break
    else:
        print("ID not found. ")


def searchPatientRecordAndVaccinationStatus():
    before_dose1 = 'NEW'
    after_dose1 = 'COMPLETED-D1'
    after_dose1_EC = 'COMPLETED'
    after_dose2 = after_dose1_EC
    patientID = input("Search ID: ")
    print(f"Searching {patientID}......\n")
    for patient in patientDetails:
        #search patientID
        if patient[0]== patientID:
            print(f"\tName        : {patient[1]}\n")
            print(f"\tAge         : {patient[2]}\n")
            print(f"\tVaccine Code: {patient[-3]}\n")
            if patient[-2] == 'False' and patient[-1] == 'False':
                print(f"\tStatus      : {before_dose1}\n")
            elif patient[-2] == 'True' and patient[-1] == 'False':
                if patient[-3] == 'EC':
                    print(f"\tStatus      : {after_dose1_EC}\n")
                else:
                    print(f"\tStatus      : {after_dose1}\n")
            elif patient[-1] == 'True':
                print(f"\tStatus      : {after_dose2}\n")
            else:
                print("Error at showing status. ")
            break
    else:
        print("ID not found. ")

def statisticalInformationOnPatientsVaccinated():
    patientNum_VC1_dose2 = 0
    patientNum_VC1_complete = 0

    patientNum_VC2_dose2 = 0
    patientNum_VC2_complete = 0

    for patient in patientDetails:
        if patient[3] == 'VC1':
            if patient[-1] == 'False' and patient[-2] =='True':
                patientNum_VC1_dose2 += 1
            elif patient[-1] == 'True':
                patientNum_VC1_complete += 1
        if patient[3] =='VC2':
            if patient[-1]=="False" and patient[-2] == 'True':
                patientNum_VC2_dose2 += 1
            elif patient[-1] == 'True':
                patientNum_VC2_complete += 1

    print("-"*20,"Vaccination Centre 1","-"*20,"\n")
    print(f"People who are waiting for dose 2: {str(patientNum_VC1_dose2)}")
    print(f"People who have completed vaccination: {str(patientNum_VC1_complete)}\n")

    print("-"*20,"Vaccination Centre 2","-"*20,"\n")
    print(f"People who are waiting for dose 2: {str(patientNum_VC2_dose2)}")
    print(f"People who have completed vaccination: {str(patientNum_VC2_complete)}\n")

def menu():
    switch = True
    while(switch==True):
            convert()
            #MainMenu
            showMainMenu = input("[Enter] to show main menu......")
            print("-"*20+"Main Menu"+"-"*20)
            print("\t1. New Patient Registration\n")
            print("\t2. Vaccine Administration\n")
            print("\t3. Search Patient Record and Vaccination Status\n")
            print("\t4. Statistical Information on Patients Vaccinated\n")
            option = (input("\tInsert 1/2/3/4 to choose the option[x to exit]: "))

            if(option=='1'):
                newPatientRegistration()
            elif(option=='2'):
                vaccineAdministration()
            elif(option=='3'):
                searchPatientRecordAndVaccinationStatus()
            elif(option=='4'):
                statisticalInformationOnPatientsVaccinated()
            elif(option=='x'):
                switch = False
                break
            else:
                pass

menu()
