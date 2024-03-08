from Api import obtener_informacion
from UI import seleccion_usuario, mostrar_propiedades_cultivo

def main():
    print("Bievenido al programa Análisis de Laboratorio Suelos en Colombia ")
    informacion_df = obtener_informacion()

    departamento, municipio, cultivo = seleccion_usuario()

   
    filtro = (informacion_df['departamento'] == departamento) & \
             (informacion_df['municipio'] == municipio) & \
             (informacion_df['cultivo'] == cultivo)

    propiedades_cultivo = informacion_df[filtro]

    mostrar_propiedades_cultivo(propiedades_cultivo)

if __name__ == "__main__":
    main()
