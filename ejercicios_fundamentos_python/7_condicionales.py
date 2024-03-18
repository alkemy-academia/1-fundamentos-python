"""
Argentina tiene, entre otros, los siguientes feriados siempre en las mismas fechas (inamovibles):
- Año Nuevo
- Dia del Trabajo
- Día de la Revolución de Mayo

Escriba un programa que lea el dia y mes que ingresa el Usuario.
Si el mes y dia coinciden con alguno de los feriados listados previamente, entonces el programa debe mostrar el nombre del feriado.
En otro caso, tu programa deberia indicar que para el dia y mes ingresado, no corresponde un feriado.
"""

print("Consulta de dia y mes para saber si es Feriado")
dia = input("Ingrese el dia: ").strip()
mes = input("Ingrese el mes: ").strip()

if dia and mes:
    dia = int(dia)
    mes = mes.lower()

    # Pregunto por el mes y dia
    if mes == 'enero' and dia == 1:
        print("La fecha ingresada corresponde al Feriado de Año Nuevo")
    elif mes == 'mayo' and dia == 1:
        print("La fecha ingresada corresponde al Feriado del Dia del Trabajador")
    elif mes == 'mayo' and dia == 25:
        print("La fecha ingresada corresponde al Feriado del Dia de la Revolución de Mayo")
    else:
        print("La fecha ingresada no corresponde a ningun Feriado")
else:
    print("Debe ingresar dia y mes a consultar")
