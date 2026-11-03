# Creo la funcion que va a evaluar los parametros del correo.

def es_correo_valido (correo):

    # Cuenta si el correo tiene menos o mas de 1 arroba, en caso que lo tenga retorna Falso.
    if correo.count("@") != 1:
        return False

    # Ubica donde se encuentra el arroba
    pos_arroba = correo.find("@")

    # Juzga que el arroba no este en el inicio o en el final del correo, en caso que si retorna Falso.
    if pos_arroba == 0 or pos_arroba == len(correo) -1:
        return False

    # Guarda los valores que se encuentran despues del arroba
    parte_dominio = correo[pos_arroba +1:]

    # Juzga que despues del arroba exista un punto, en caso que no retorna Falso.
    if "." not in parte_dominio:
        return False

    # Juzga que el punto no este inmediatamente antes del simbolo arroba, en caso que si retorna Falso.
    if parte_dominio.startswith("."):
        return False
    
    # Juzga que el punto no este inmediatamente despues del simbolo arroba, en caso que si retorna Falso.
    if parte_dominio.endswith("."):
        return False

    return True

    
# Realizo las pruebas de los condicionales. 
print(f"\n¿'usuario@ejemplo.com' es válido?: {es_correo_valido('usuario@ejemplo.com')}")
print(f"¿'usuario.ejemplo.com'es valido?: {es_correo_valido('usuario.ejemplo.com')}")
print(f"¿'@ejemplo.com' es valido?: {es_correo_valido('@ejemplo.com')}")
print(f"¿'usuario@ejemplo' es valido?: {es_correo_valido('usuario@ejemplo')}")
print(f"¿'usuario@ejemplo.com.' es valido?: {es_correo_valido('usuario@ejemplo.com.')}")
print(f"¿'usuario@.com' es valido?: {es_correo_valido('usuario@.com')}\n")


