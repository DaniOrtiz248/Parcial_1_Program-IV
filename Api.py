import pandas as pd
from sodapy import Socrata


def obtener_informacion():
    
    client = Socrata("www.datos.gov.co", None)
    results = client.get("ch4u-f3i5", limit=1000)
    results_df = pd.DataFrame.from_records(results)

    return results_df
    
    
    



