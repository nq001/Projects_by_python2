names = ["naif","ali","osama"]

name = input("enter your name: ")
if name in names:
    print(f"welcome {name} ")

    ask = input("new donor press(n) or search about blood press(r) or to read file press(re): ")
    print("="*20)
    if ask == "r":
        from Blood_search import system_search
        print(system_search())
    elif ask == "re":
        file_path = input("enter file path: ")
        mode = "r"
        file = open(f"{file_path}",f"{mode}")
        print(file.read())
    else:
        if ask == "n":
            from Blood_search import system_donors
            print(system_donors())
else:     
    print(f"sorry sir\s but your name not in menu!")
        