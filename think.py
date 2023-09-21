
# Dentist Appointment Scheduler
# An empty dictionary to store appointments
appointments = {}

# Function to schedule an appointment
def schedule_appointment(appointments):
    name = input("Enter the name for appointment: ")
    day = input("Enter the day ex) Tuesday: ")
    time = input("Enter the time ex) 11:00 AM): ")
    appointments[name] =[day,time]
       


    
    
    print("Appointment scheduled for " + name + " is " + day + " at " + time)
choice = "1"
while choice != "3":

    print("Dentist Appointment Scheduler")
    print("1. Schedule Appointment")
    print("2. list Appointments")
    print("3. Quit")
    

    choice = input("Enter your choice (1/2/3): ")

    if choice == '1':
        schedule_appointment(appointments) #my function is being called here for a dictionary appointments
    elif choice == '2':
        for key in appointments:
            print("Appointment for", key, "is on", appointments[key][0], "at", appointments[key][1])
    elif choice == '3':
        print("Thank you for using the appointment scheduler. Have a good day!")
    else:
        print("Invalid choice. Please try again.")


