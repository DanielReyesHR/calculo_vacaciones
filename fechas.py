import pandas as pd
from datetime import datetime
def format_date():
    try:
        ruta_archivo = 'Vacacionespendientsagosto24.csv'
        df = pd.read_csv(ruta_archivo,delimiter=";")  
           
        for i, fecha in df["F.Ini.Cont"].items():  
            if pd.notna(fecha):  
                fecha_datetime = pd.to_datetime(fecha).to_pydatetime()
                df.at[i, "F.Ini.Cont"] = fecha_datetime.strftime('%d/%m/%Y')
                
        print("Datos después de modificar:")
        
        print(df.head())
        
        df.to_csv(ruta_archivo, index=False)
            
        print("Fechas convertidas y guardadas en la columna 'F.Ini.Cont'.")
        
        

        
    except Exception as e:
        print("Error al leer el archivo:", e) 
        
        
format_date()