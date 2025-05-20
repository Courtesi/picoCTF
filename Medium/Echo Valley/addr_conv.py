def converter():
    addr = input("Give me an address to convert: ")
    if addr.startswith("0x"):
        addr = addr[2:]

    if not addr.isdigit():
        print("Not a valid address")
        return
    
    exit_val = 0
    for i in range(len(addr)):
        if addr[i] != "0":
            exit_val = i
            break

    addr = addr[exit_val:]
        
    print(addr)



if __name__ == "__main__":
    converter()
