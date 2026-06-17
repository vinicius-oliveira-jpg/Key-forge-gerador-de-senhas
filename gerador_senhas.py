import secrets
import string

def gerar_senha(tamanho: int, usar_numeros: bool, usar_especiais: bool) -> str:
    caracteres = string.ascii_letters

    if usar_numeros:
        caracteres += string.digits

    if usar_especiais:
        caracteres += string.punctuation

    senha = ''.join(secrets.choice(caracteres) for _ in range(tamanho))
    return senha