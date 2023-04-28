MorseCode = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..',
             'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--._',
             'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
             'Z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....',
             '7': '--...', '8': '---..', '9': '----.', '0': '-----', '.': '......', ',': '.−.−.−', '?': '..--..',
             '!': '−−..−−'}


def main():
    print('Вас приветствует программа Азбуки Морзе. Пожалуйста, выберите действие.')
    while True:
        print('Команды:')
        print('    exit                               -- выход')
        print('    encode <text>                      -- ход из клетки (row, col)')
        print('    decode <code>                      -- ход из клетки (row, col)')
        command = input()
        func, text = command[:command.find(' ')], command[command.find(' ') + 1:]
        if func == 'encode':
            print(decode_from_morse(text))
        elif func == 'decode':
            print(decode_from_morse(text))
        elif func == 'exit':
            break
        else:
            print('Неверная команда!')


def encode_to_morse(text):
    result = ''
    for i in text.split():
        result += ' '.join(MorseCode.get(j.upper()) for j in i)
        result += '   '
    return result
    # Внутри функции проходимся по переданному слову, делая каждый символ заглавным.
    # Методом get() возвращаем значение по указанному ключу в параметрах.
    # Возвращаем уже кодированный текст


def decode_from_morse(code):
    result = ''
    text = code.split('   ')
    for i in text:
        word = ''
        for j in i.split(' '):
            for val, item in MorseCode.items():
                if item == j:
                    word += val.lower()
        if len(result) >= 2 and (result[-2] == '.' or result[-2] == '?' or result[-2] == '!'):
            word = word.capitalize()
        result += word + ' '
    return result


if __name__ == '__main__':
    main()
    
