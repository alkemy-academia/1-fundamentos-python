# Determinar el acceso segun el usuario y nivel
usuario = 'luis'
nivel = 1

if usuario == 'admin' or nivel >= 4:
    print('Acceso total')
elif 2 < nivel < 4:
    print('Acceso parcial')
else:
    print('Acceso denegado')
