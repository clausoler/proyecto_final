from pathlib import Path

import pandas as pd
 
def cargar_datasets(diccionario_archivos):
    """
    Carga varios archivos CSV y los devuelve en un diccionario de DataFrames.

    Parametros:
        diccionario_archivos: diccionario con el nombre del dataset y su ruta.

    Devuelve:
        diccionario con los datasets cargados como DataFrames.
    """
    datasets = {}

    for nombre, ruta in diccionario_archivos.items():
        try:
            datasets[nombre] = pd.read_csv(ruta)
            print(f"Dataset cargado correctamente: {nombre}")
        except FileNotFoundError:
            print(f"No se encontro el archivo: {ruta}")

    return datasets
 
def cargar_csv(ruta, **kwargs):
    """
    Carga un archivo CSV.

    Parametros:
        ruta: ruta del archivo.
        **kwargs: parametros adicionales para pd.read_csv().

    Devuelve:
        DataFrame.
    """

    return pd.read_csv(ruta, **kwargs)

def cargar_pkl(ruta):
    """
    Carga un archivo pickle.

    Parametros:
        ruta: ruta del archivo pickle.

    Devuelve:
        DataFrame con los datos cargados.
    """
    return pd.read_pickle(ruta)
     
def cargar_dataset(ruta):
    """
    Carga el dataset final generado durante el proceso
    de Feature Engineering.

    Parametros
    ----------
    ruta : str o Path
        Ruta del archivo pickle.

    Devuelve
    --------
    pd.DataFrame
        Dataset final listo para análisis.
    """
    return pd.read_pickle(ruta)
     
def cargar_dataset(ruta):
    """
    Carga el dataset final en formato pickle.

    Parametros
    ----------
    ruta : str
        Ruta donde se encuentra guardado el archivo pickle.

    Devuelve
    --------
    pd.DataFrame
        Dataset final cargado en memoria.
    """

    df = pd.read_pickle(ruta)

    return df
     
