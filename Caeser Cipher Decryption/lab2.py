import enchant as e

alphabet = set()
char = 'A'
alphabet.add(char)
for a in range(51):
    if char == 'Z':
        char = chr(ord(char) + 6)
    char = chr(ord(char) + 1)
    alphabet.add(char)

def decrypt(str):
    new_string = str.split()
    D = e.Dict("en_US")
    for i in range(26):
        for j in range(len(new_string)):
            updated = ''
            for letter in new_string[j]:
                if chr(ord(letter)) in alphabet:
                    new_char = chr(ord(letter) + 1)
                    if new_char == '[' or new_char == '{':
                        new_char = chr(ord(letter) - 25)
                    updated += new_char
                else:
                    updated += chr(ord(letter))

            new_string[j] = updated

        total = 0
        for k in new_string:
            if D.check(k):
                total += 1

        percentage = total / len(new_string)

        if percentage >= .75:
            new_string.append(i+1)
            return new_string


def encrypt(key, str):
    subtractor = 26-key
    new_string = str.split()

    for j in range(len(new_string)):
        updated = ''
        for letter in new_string[j]:
            if chr(ord(letter)) in alphabet:
                new_char = chr(ord(letter) + key)
                if ('[' <= new_char < 'a') or new_char >= '{':
                    new_char = chr(ord(letter) - subtractor)
                updated += new_char
            else:
                updated += chr(ord(letter))

        new_string[j] = updated

    final_string = ''
    for s in new_string:
        final_string += s
        final_string += ' '

    return final_string







if __name__ == '__main__':
    string = "Axeeh xoxkrhgx tgw Wxevhfx mh Likbgz 2021, VEVL 378!. B ahix rhn wbwg'm mktgletmx mabl ur atgw, matm'l " \
             "patm vhfinmxkl tkx yhk. By rhn wbw bm ur atgw, rhn lahnew kxwh bm uxvntlx whbgz bm ur atgw bl " \
             "bgxyybvbxgm tgw matm'l par mabl mxqm bl lh ehgz. Telh, mabl tllbzfxgm vteel yhk t lftee irmahg " \
             "ikhzktf.Hgx ptr hy lheobgz mabl, bl nlbgz lmkbgz.ftdxmktgl() tgw bm bl kxvhffxgwxw. Ahix rhn atw " \
             "yng phkdbgz mabl hnm. Ehhdbgz yhkptkw mh phkdbgz pbma tee hy rhn mabl lxfxlmxk! :)"

    print('Given string:', string)
    decryption = decrypt(string)


    final_string = ''
    for i in range(len(decryption)-1):
        final_string += decryption[i]
        final_string += ' '

    print('The decrypted message is:', final_string)
    print('The encryption key used is:', decryption[-1])

    encryption = encrypt(4, string)
    print('Given string:', string)
    print("The encrypted message with key = 4 is:", encryption)
