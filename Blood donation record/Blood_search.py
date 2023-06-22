
def system_search():

    print("Blood donation record")

    All_lists = []
    lists_details_donor = []
    lisdonor_name, lisblood_type, lisdate, lisplace, lisphone= [],[],[],[],[]
    today_date = "20/12/2023"
    lisblood_type1 = ["A+","B","O+","A-","O-"]
    # today_date = input("enter date: ")
    type_blood1 = input("enter type of blood to search ( A+ or O- ...ect ): ")
    if type_blood1 in lisblood_type1:
        print("TRUE")
        item = input("new order press(y) or no press(c): ")
        if item == "y":
            num_person = int(input("enter how many request: "))
            for person in range(num_person):

                lisdonor_name.append(input("enter name: "))
                lisblood_type.append(input("enter type of blood ( A+ or O- ...ect ): "))
                date = today_date
                lisdate.append(date)
                lisplace.append(input("enter place of donation: "))
                lisphone.append(int(input("enter phone number: ")))
                
            lists_details_donor.append(lisphone)

            All_lists.append(lisdonor_name)
            All_lists.append(lisblood_type)
            All_lists.append(lisdate)
            All_lists.append(lisplace)
            All_lists.append(lists_details_donor)

            ph = input("do you want to print this in output here press (ok): ")
            if ph == "ok":
                print(f"name\ttype_blood\tdate\tplace\t  phone")
                print("="*80)
                    
                h = 0 
                for v in range(num_person):
                    print(f"{All_lists[0][h]}\t   {All_lists[1][h]}\t {All_lists[2][h]}\t{All_lists[3][h]}  {All_lists[4][0][h]}\n")
                    h += 1
                print("="*80)

            def report(path_file, mode_file):
        
                file = open(f"{path_file}",f"{mode_file}")
                # file = open(r"D:\Learn\univer\PAU\Assignment on monday\Blood donation record.txt","a")
                file.write(f"\t\t\treport for search about blood today\t\t\n")
                file.write(f"{'='*120}\n")
                file.write(f"name\t\ttype_blood\t\tdate\t\tplace\t\tphone\n")
                file.write(f"{'='*120}\n")

                n = 0
                for i in range(len(lisdonor_name)):
                    file.write(f"{All_lists[0][n]}\t\t{All_lists[1][n]}\t\t{All_lists[2][n]}\t\t{All_lists[3][n]}\t{All_lists[4][0][n]}\n")
                    n += 1
                file.write(f"{'='*120}\n")
                file.close()
            rep = input("print report in file press (p): ")
            if rep == "p":
                path_file = input("enter path file: ")
                mode_file = "a"                # input("enter mode for file a or w : ")
                report(path_file, mode_file)
            else:
                print("thank you")
            print("="*80)
        else:
            print("thank you")
    else:
        print("sorry sir\s this blood not available now")
    
# New Donors =>=>

def system_donors():

    print("Blood donation record")

    All_lists = []
    lists_details_donor = []
    lisdonor_name, lisblood_type, lisdate, lisplace, lisphone, lisemail, lisaddress= [],[],[],[],[],[],[]
    today_date = "20/12/2023"
    # today_date = input("enter date: ")

    num_donor = int(input("enter how many donors: "))
    for donor in range(num_donor):
        lisdonor_name.append(input("enter name: "))
        lisblood_type.append(input("enter type of blood ( A+ or O- ...ect ): "))
        date = today_date
        lisdate.append(date)
        lisplace.append(input("enter place of donation: "))
        lisphone.append(int(input("enter phone number: ")))
        lisemail.append(input("enter email: "))
        lisaddress.append(input("enter address: "))
        
    lists_details_donor.append(lisphone)
    lists_details_donor.append(lisemail)
    lists_details_donor.append(lisaddress)

    All_lists.append(lisdonor_name)
    All_lists.append(lisblood_type)
    All_lists.append(lisdate)
    All_lists.append(lisplace)
    All_lists.append(lists_details_donor)

    ph = input("do you want to print this in output here press (ok): ")
    if ph == "ok":
        print(f"name\ttype_blood\tdate\tplace\t  phone\t   address\t\temail")
        print("="*80)
            
        h = 0
        for k in range(num_donor):
            print(f"{All_lists[0][h]}\t   {All_lists[1][h]}\t {All_lists[2][h]}\t{All_lists[3][h]}  {All_lists[4][0][h]}  {All_lists[4][2][h]}  {All_lists[4][1][h]}\n")
            h += 1
        print("="*80)

    def report(path_file, mode_file):
        file = open(f"{path_file}",f"{mode_file}")
        # file = open(r"D:\Learn\univer\PAU\Assignment on monday\Blood donation record.txt","a")
        file.write(f"\t\t\treport new donors\t\t\n")
        file.write(f"{'='*120}\n")
        file.write(f"name\t\ttype_blood\t\tdate\t\tplace\t\tphone\t\taddress\t\temail\n")
        file.write(f"{'='*120}\n")
        n = 0
        for i in range(num_donor):
            file.write(f"{All_lists[0][n]}\t\t{All_lists[1][n]}\t\t{All_lists[2][n]}\t\t{All_lists[3][n]}\t{All_lists[4][0][n]}\t  {All_lists[4][2][n]}\t {All_lists[4][1][n]}\n")
            n += 1
        file.write(f"{'='*120}\n")
        file.close()
    rep = input("print report in file press (p): ")
    if rep == "p":
        path_file = input("enter path file: ")
        mode_file = "a"
        print(report(path_file, mode_file))
    else:
        print("thank you")
    print("="*80)