from datetime import datetime
from extralegal import extra_legal

def saldo_periodo_actual():
    try:
        # Datos de ejemplo
        array_data = [[12,"2010-01-02", 40.96], [13,"2024-01-04", 9.88], [14,"2022-08-17", 18.58], [15,"2022-03-04", 12.38],[17,"2020-11-05",25.33]]
        fecha_corte_str = "2024-08-31"
        array_anios = []
        fecha_corte = datetime.strptime(fecha_corte_str, "%Y-%m-%d")
        
        for fila in array_data:
            fecha_str = fila[1]
            id = fila[0] 
            saldo = fila[2]
            fecha_contratacion = datetime.strptime(fecha_str, "%Y-%m-%d")
            
            # Calcular el año de corte
            if fecha_contratacion.month > fecha_corte.month or \
               (fecha_contratacion.month == fecha_corte.month and fecha_contratacion.day > fecha_corte.day):
                nueva_fecha = fecha_contratacion.replace(year=fecha_corte.year - 1)
                meses = (12 - nueva_fecha.month)
                dias = (30 - nueva_fecha.day+1)
                diferencia_meses = meses + fecha_corte.month
                periodo = 2023
            else:
                nueva_fecha = fecha_contratacion.replace(year=fecha_corte.year)
                dias = (30 - nueva_fecha.day+1)
                diferencia_meses = (fecha_corte.month - nueva_fecha.month)
                periodo = 2024
                
            dias_vac_acum = float((((diferencia_meses*30)+dias)*15)/360)
            registro_anios = [saldo,{"id":id,"dias": dias_vac_acum, "año": periodo}]
            
            anio_actual = nueva_fecha.year
            anio_final = fecha_contratacion.year
            
            while anio_actual > anio_final:
                periodo_bucle = f"{anio_actual - 1}"
                registro_anios.append({"id":id,"dias": 15, "año": periodo_bucle})
                anio_actual -= 1  

            array_anios.append(registro_anios)
        print(array_anios)
        return array_anios
    
    except Exception as e:
        print("Exception:", e)

def calcular_saldo():
    try:
        # Obtener los datos
        periodo_actual = saldo_periodo_actual() 
        extralegal = extra_legal() 

        for periodo in periodo_actual:
            saldo = periodo[0]
            print(saldo)
            años_periodo = periodo[1:] 
            print(años_periodo)
            id_usuario = años_periodo[0]['id']
            
            print(f"\nProcesando ID: {id_usuario}, Saldo Inicial: {saldo:.2f}")

            extralegales_usuario = [extra for extra in extralegal if extra[0]['id'] == id_usuario][0]

            for año_periodo in sorted(años_periodo, key=lambda x: int(x['año']), reverse=True):
                if saldo <= 0:
                    break 

                dias_periodo = año_periodo['dias']
                año_actual = int(año_periodo['año'])

                if saldo >= dias_periodo:
                    saldo -= dias_periodo
                    print(f"Año {año_actual} (Legal) : Restados {dias_periodo:.2f} días, Saldo Restante: {saldo:.2f}")
                else:
                    print(f"Año {año_actual} (Legal): Saldo restante de este periodo {saldo:.2f} días ")
                    break

                dias_extralegal = next((extra['dias'] for extra in extralegales_usuario if int(extra['año']) == año_actual), 0)
                if saldo > 0 and dias_extralegal > 0:
                    if saldo >= dias_extralegal:
                        saldo -= dias_extralegal
                        print(f"Año {año_actual} (Extralegal): Restados {dias_extralegal:.2f} días, Saldo Restante: {saldo:.2f}")
                    else:
                        print(f"Año {año_actual} (Extralegal): Saldo restante de este periodo {saldo:.2f} días ")
                        break

#            if saldo > 0:
#                print(f"Saldo final restante para ID {id_usuario}: {saldo:.2f}")
#            else:
#                print(f"Saldo agotado para ID {id_usuario}.")

    except Exception as e:
        print("Exception:", e)

calcular_saldo()

#saldo_periodo_actual()
