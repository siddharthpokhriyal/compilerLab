def py():
    l = []
    str = "ab*c(a+b)"
    pstr = ["aca", "acb"]
    print ("Siddharth Pokhriyal")
    print ("1816110205")
    n = input("Enter the string: ")
    if n[len(n) - 2] != "c":
        print("String not accepted")
    elif n in pstr:
        print("String Accepted")
    elif n[1] == "b":
        for i in range(len(n)):
            if n[i] == "b" and i != len(n) - 1:
                pass
            else:
                l.append(n[i])
        p = "".join(l)
        if p in pstr:
            print("String accepted")
        else:
            print("String not accepted")
    else:
        print("String not accepted")
py()
