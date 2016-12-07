def get_alphabet():
    '''
    this function returns the alphabet in a list
    :return: list
    '''
    alphabet = [chr(i) for i in range(97,123)]
    return alphabet


def cipher_alphabet(key='alext'):
    '''
    create cipher alphabets with the key provided
    :param key: string
    :return cipher_d: dictionary
    '''
    #convert string (key) to list (cipher)
    alphabet = get_alphabet()
    cipher = list(key)+[a for a in alphabet if a not in key]

    cipher_d = dict()
    for a, c in zip(alphabet, cipher):
        cipher_d[a] = c
    #cipher_d = {a: c for a, c in zip(alphabet, cipher)}
    return cipher_d


def encrypt(msg, key='alext'):
    '''
    encrypts the input messae using the key provided
    :param msg: string
    :param key: stirng
    :return encrypted_msg: string
    '''
    #cipher alphabet
    cipher = cipher_alphabet(key)
    encrypted_msg = ''
    for s in msg:
        encrypted_msg += cipher.get(s, s)
    return encrypted_msg


def decrypt(encrypted_msg, key='alext'):
    '''
    decrypts the input message with the key provided
    :param encrypted_msg: string
    :param key: string
    :return msg: string
    '''
    #cipher alphabet
    cipher = cipher_alphabet(key)
    reversed_cipher = dict()
    for k ,v in cipher.items():
        reversed_cipher[v] = k
    msg = ''
    for s in encrypted_msg:
        msg += reversed_cipher.get(s,s)
    return msg


#message = input('Enter your message to encrypt: ')


