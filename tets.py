import pandas as pd
       
def test():
    try:
        ruta_archivo = 'Vacacionespendientsagosto24.csv'
        df = pd.read_csv(ruta_archivo,delimiter=",")  
        for i,codigo in df["Codigo"].items():
            print(codigo)
    except Exception as e:
        print("Error",e)        

test()