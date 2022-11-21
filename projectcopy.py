'''This is a simple programme to store some information anout students.
we can add,delete,update and print the individual data of student as well as
all the data stored in it.'''
try:
    d = {
         
        "Rahul kumar yadav": 9693520671,
        "Anushka kumari" : 1000000000,
        "Kanhaiya jee": 9771050894,
        "Bishal moktan": 9711459161,
        "N.vamshidhar": 9347724211,
        "T.jagadeesh": 9701051449,
        "Nitin": 7731889978,
        "Krishna teja": 9701496281,
        "E.rahul": 7888676946,
        "Moosa": 7006657708,
        "Divyansh pandey": 8887990911,
        "Ansh Thakur": 8091360981,
        "Abigyan raj": 6299808685,
        "Aman": 9588531691,
        "Ishita singh": 6374701746,
        "S.lavakiran": 9398522578,
        "Vansh gupta": 7451917413,
        "Amit yadav": 9118901463,
        "Shyam Gupta": 8445985911,
        "Sahit.a": 8247591432,
        "Divyam katiyan": 9118680874,
        "Garv soga": 7009488176,
        "G.tharun": 9346984383,
        "Gungun": 7973661741,
        "Samreen": 9515184912,
        "L.ramasubrahmanyam": 9347848219,
        "S.srisai": 6397053522,
        "Yash": 7717469600,
        "Nikesh sahoo": 8658311234,
        "Manikanta sai": 6305100501,
        "Aman pandey": 8081525720
    }
     
    os = "True"
    while True:
        
        print ("\t\t\t Welcome to student's data page" )
        print("\t\t\t Enter 1 to print data.")
        print("\t\t\t Enter 2 to extract phone of given student.")
        print("\t\t\t Enter 3 to search student by number: ")
        print("\t\t\t Enter 4 to to add data.")
        print("\t\t\t Enter 5 to update any number.")
        print("\t\t\t Enter 6 delete any data.")
        print("\t\t\t Enter 7 to exit.")
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        choice = int(input("\t\t\t Enter choice: "))
        if choice == 1:
            
            print("{:25} {:<25}".format("NAME OF STUDENT", "PHONE"))
            for i in d:
                print("{:25} {:<25}".format(i,d[i]))
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')    
        elif choice == 2:
             x = input("Enter name of student: ").capitalize()
             print(f"Contact number of {x} is",d[x])
             print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~') 
             
        elif choice == 5:
            x = input("Enter name of student Whose phone is to be updated: ").capitalize()
            y = int(input("Enter new phone: "))
            d[x] = y
            for i in d:
                print("{:25} {:<25}".format(i,d[i]))
            print("\t\t\t Phone number updated")
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~') 
             
        elif choice == 4:
            x = input("Enter name of student: ").capitalize()
            y = int(input("Enter phone number: "))
            d[x]= y
            for i in d:
                print("{:25} {:<25}".format(i,d[i]))
            print("\t\t\t Information added on data!!")
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~') 
           
            
        elif choice == 3:
            x = int(input("Enter nuumber: "))
            for i in d:
                if d[i] == x:
                    print("Student with this number is:", i)
            
            
        elif choice == 6:
            x = input("Name of student to be deleted: ").capitalize() 
            del(d[x])
            for i in d:
                print("{:25} {:<25}".format(i,d[i]))
            print("\t\t\t Contact deleted")
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
           
        elif choice == 7:
            print("Thank you!!! Have a great day 💝💝💝💝💝")
            break

except Exception as e:
    print('\t\tError Occured')
    print('\t\t Try Again')
    print(e)
        
        
