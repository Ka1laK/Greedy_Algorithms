def cambio_monedas(monto, monedas):
    resultado = []
    registro_pasos = []
    
    for moneda in monedas:
        while monto >= moneda:
            registro_pasos.append((monto, moneda, monto >= moneda, monto - moneda))  # Registrar el paso antes de modificar el monto
            monto -= moneda
            resultado.append(moneda)
    
    if monto != 0:
        print("No se puede devolver el monto exacto con las monedas disponibles")
    else:
        print("monto_Total    monedas[i]    montoTotal > monedas[i]    cambio")
        for paso in registro_pasos:
            print(f"{paso[0]:>10} {paso[1]:>11} {str(paso[2]):>21} {paso[3]:>8}")
    
    return resultado

test = cambio_monedas(15, [11, 5, 1])
print("Monedas utilizadas para el cambio:", test)
