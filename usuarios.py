def OLD_validar_email(email:str):
    """Validação inicial simplificada (intencionalmente incompleta)."""
    return isinstance(email, str) and "@" in email

def validar_email(email:str):
    """Validação inicial simplificada (intencionalmente incompleta)."""
    if email.strip(' ') != email : return False
    elif email.startswith('.') : return False # a@empresa.com
    elif email.startswith('@') : return False
    elif email.count('@') != 1 : return False
    elif not (email.endswith('.com') or email.endswith('.com.br')): return False #MAIS TRABALHO 
    elif 
        inicio_marcador = "@"
        fim_marcador = ".com"

        # Encontra a posição do início do primeiro marcador
        inicio_idx = email.find(inicio_marcador) + len(inicio_marcador)

        # Encontra a posição do segundo marcador a partir do início
        fim_idx = email.find(fim_marcador, inicio_idx)

        # Extrai a substring entre eles
        resultado = email[inicio_idx:fim_idx]
        if resultado == '' : return False
    return isinstance(email, str) and "@" in email

# TODO: Implementar validação de email mais robusta, incluindo verificação de domínio e formato adequado.