def xor_cipher(text, key):
    return ''.join(chr(ord(c) ^ key) for c in text)


text_dict = {}

while True:
    key = int(input('Введите ключ:  '))
    original_text = input('Введите текст:  ')
    encrypted_text = xor_cipher(original_text, key)
    print(f"Зашифрованный текст: {encrypted_text}")
    text_dict[original_text] = encrypted_text
    act = input('1.расшифровать текст или 2.Зашифровать текст  ')
    if act == '1':
        for original, encrypted in text_dict.items():
            print(f"Оригинальный текст: {original},    Зашифрованный текст: {encrypted}")
            print()
