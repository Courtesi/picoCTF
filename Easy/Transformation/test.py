flag = "picoCTF{16_bits_inst34d_of_8_0ddcd97a}"

x = ''.join([chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)])

print("encoded:", x)

def decode(encrypted):
    flag = ""
    for i in range(len(encrypted)):
        char1 = chr(ord(encrypted[i]) >> 8)
        char2 = chr(encrypted[i].encode("utf-16be")[-1])
        flag += char1 + char2

    return flag

print("decoded: ", decode(x))
