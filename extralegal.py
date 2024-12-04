from pandas import pandas as pd
from datetime import datetime

def extra_legal():
    try:
        #ruta_archivo = 'Vacacionespendientsagosto24.csv'
        #df = pd.read_csv(ruta_archivo, delimiter=",") df["F.Ini.Cont"].items()
        array_data =[[12,"2010-01-02"], [13,"2024-01-04"], [14,"2022-08-17"], [15,"2022-03-04"],[17,"2020-11-05"]]
        resultado = []
        fecha_tentativa_inicial = 2024

        for fecha_ in array_data:
            fecha = fecha_[1]
            id = fecha_[0]
            sub_resultado = []
            if pd.notna(fecha):
                if isinstance(fecha, str):
                    fecha_objeto = datetime.strptime(fecha, "%Y-%m-%d")
                else:
                    fecha_objeto = fecha

                anio_actual = fecha_objeto.year
                fecha_tentativa = fecha_tentativa_inicial

                while anio_actual <= fecha_tentativa:
                    diferencia_anios = fecha_tentativa - anio_actual + 1

                    if diferencia_anios >= 6 and diferencia_anios <= 10:
                        dias_totales = 2
                    elif diferencia_anios > 10:
                        dias_totales = 4
                    else: 
                        dias_totales = 0

                    sub_resultado.append({"id":id,"dias":dias_totales,"año":fecha_tentativa})
                    fecha_tentativa -= 1
                    
            resultado.append(sub_resultado)
        print(resultado)
        return resultado


    except Exception as e:
        print("Error al procesar el archivo:", e)

