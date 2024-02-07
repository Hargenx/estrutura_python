def soma_char_codigos_1(n: str) -> int:
    '''O(N)'''
    soma = 0
    for char in n:
        soma += ord(char)
    return soma


def soma_char_codigos_2(n: str) -> int:
    '''O(N^2)'''
    soma = 0
    for _ in range(len(n)):
        for j in range(len(n)):
            soma += ord(n[j])
    return soma

def soma_char_codigos_3(n: str) -> int:
    '''O(N^3)'''
    soma = 0
    for _ in range(len(n)):
        for _ in range(len(n)):
            for k in range(len(n)):
                soma += ord(n[k])
    return soma

if __name__ == '__main__':
    print(f"O(N): {soma_char_codigos_1('123456789')}")
    print(f"O(N^2): {soma_char_codigos_2('123456789')}")
    print(f"O(N^3): {soma_char_codigos_3('123456789')}")