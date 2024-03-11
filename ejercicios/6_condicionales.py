"""
Una popular red social está implementando un filtro de edad obligatorio para sus
nuevos usuarios, que verifica su edad, de acuerdo a la misma establece o no un
control parental.
Si el usuario tiene menos de 12 años, no le permite crearse una cuenta.
Si el usuario tiene entre 13 y 17 años, le permite crearse una cuenta con control parental activado.
Si el usuario tiene 18 años o más, le permite crearse una cuenta sin restricciones.
Bonus:
Al mismo tiempo, en todos los casos, deberá haber facilitado su DNI para comprobar
realmente la información, si no lo hizo, no puede hacerse ningún tipo de cuenta,
sin importar su edad.
"""

dni = input('Ingrese su DNI: ').strip()
edad = input('Ingrese su edad: ').strip()

if not (dni and edad):
    print('Ud no ha ingresado su DNI ni edad por lo tanto no se puede generar ninguna cuenta')
else:
    edad = int(edad)
    if edad <= 12:
        print('No se puede crear una cuenta por su edad')
    elif 13 <= edad <= 17:
        print('Puedes tener una cuenta con control parental')
    else:
        print('Puedes tener una cuenta con acceso total')
