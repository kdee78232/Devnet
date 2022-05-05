x=0
while True:
    try:
        filename= input('Which file do you want to open?' ':' '\n')
        with open(filename, "r")as data:
            file_data=data.read()
    except FileNotFoundError:
        print(f"Sorry, {filename} doesn't exist! Please try again")

    else:
        print(file_data)
        x=0
        break
    finally:
        x+=1
        if x==3:
            print("you are at limit")
            break


