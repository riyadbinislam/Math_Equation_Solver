from . import l2reval
morse_code = {'A': '.-', 'B': '-...',
                   'C': '-.-.', 'D': '-..', 'E': '.',
                   'F': '..-.', 'G': '--.', 'H': '....',
                   'I': '..', 'J': '.---', 'K': '-.-',
                   'L': '.-..', 'M': '--', 'N': '-.',
                   'O': '---', 'P': '.--.', 'Q': '--.-',
                   'R': '.-.', 'S': '...', 'T': '-',
                   'U': '..-', 'V': '...-', 'W': '.--',
                   'X': '-..-', 'Y': '-.--', 'Z': '--..',
                   '1': '.----', '2': '..---', '3': '...--',
                   '4': '....-', '5': '.....', '6': '-....',
                   '7': '--...', '8': '---..', '9': '----.',
                   '0': '-----', ', ': '--..--', '.': '.-.-.-',
                   '?': '..--..', '/': '-..-.', '-': '-....-',
                   '(': '-.--.', ')': '-.--.-'}


def morse_decrypt(message):
    message += ' '

    decipher = ''
    cipher_txt = ''
    for letter in message:

        if (letter != ' '):

            i = 0

            cipher_txt += letter

        else:
            i += 1

            if i == 2:

                decipher += ' '
            else:

                decipher += list(morse_code.keys())[list(morse_code
                                                              .values()).index(cipher_txt)]
                cipher_txt = ''

    return decipher


def morse2eq(m):
    m = m.replace("(", "").replace(")", "")
    m = m.split()
    print(m)
    a = ""
    for i in m:
        try:
            if i[0] == "-" and i[1] == " ":
                a += "-"
            else:
                a += morse_decrypt(i)
        except:
            a += i
    print(a)
    return l2reval(a)