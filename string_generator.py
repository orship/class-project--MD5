def to_ascii_list(str):
    lst = []
    for c in str:
        lst.append(ord(c))
    return lst

def to_str(ascii_list):
    str = ''
    for c in ascii_list:
        str += chr(c)
    return str

def main():
    password = 'aaaaaa'
    pass_ascii = []

    while password != '':
        print(password)
        
        pass_ascii = to_ascii_list(password)

        for n in reversed(range(len(pass_ascii))):
            pass_ascii[n] += 1

            if pass_ascii[n] > ord('z'):
                if n == 0:
                    pass_ascii = ''
                    break
                
                pass_ascii[n] = ord('a')
            else:
                break

        password = to_str(pass_ascii)


if __name__ == '__main__':
    main()
