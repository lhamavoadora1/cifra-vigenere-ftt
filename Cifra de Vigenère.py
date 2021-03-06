import math

tabula_recta = []
alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', ' ', 'Ç', 'Ã', 'Á', 'À', 'Â', 'É', 'Ê', 'Í', 'Õ', 'Ô', 'Ó', 'Ú', '?', ',', '!', '.']
def build_tabula():
    module = len(alphabet)
    for i in range(module):
        line = []
        for j in range(i, i + module):
            index = j % module
            line.append(alphabet[index])
        tabula_recta.append(line)

def check_input(text):
    for letter in text:
        if letter not in alphabet:
            return False
    return True

def input_phrase():
    phrase = input('Digite uma frase: ').upper()
    while not phrase or not check_input(phrase):
        message = ''
        if not phrase:
            message = 'DIGITE uma frase: '
        elif not check_input(phrase):
            message = 'Existem caracteres desconhecidos na frase, digite uma frase: '
        phrase = input(message).upper()
    phrase_len = len(phrase)
    return phrase, phrase_len

def input_key(phrase_len):
    key = input('Digite a chave: ').upper()
    key_len = len(key)
    while phrase_len < key_len or not key or not check_input(key):
        message = ''
        if phrase_len < key_len:
            message = 'A chave é maior do que a palavra!\nPor favor, digite uma chave menor: '
        elif not key:
            message = 'DIGITE a chave: '
        elif not check_input(key):
            message = 'Existem caracteres desconhecidos na chave, digite outra chave: '
        key = input(message).upper()
        key_len = len(key)
    key_repetition = math.ceil(phrase_len / key_len)
    for i in range(1, key_repetition):
        key += key
    return key

build_tabula()

while True:
    print('Cifra de Vigenère\n')
    choice = input('1 - Criptografar\n2 - Descriptografar\nOutro - Sair\n')
    if choice == '1':
        print('Criptografar')
        phrase, phrase_len = input_phrase()
        key = input_key(phrase_len)
        crypto_phrase = ''
        for index in range(phrase_len):
            index_x = alphabet.index(phrase[index])
            index_y = alphabet.index(key[index])
            crypto_phrase += tabula_recta[index_x][index_y]
        print('Frase criptografada => "%s"\n' %crypto_phrase)

    elif choice == '2':
        print('Descriptografar')
        phrase, phrase_len = input_phrase()
        key = input_key(phrase_len)
        decrypto_phrase = ''
        for index in range(phrase_len):
            index_y = alphabet.index(key[index])
            index_x = tabula_recta[index_y].index(phrase[index])
            decrypto_phrase += alphabet[index_x]
        print('Frase descriptografada => "%s"' %decrypto_phrase)

    else:
        print('Sair')
        break