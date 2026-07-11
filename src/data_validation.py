from pathlib import Path

import chardet

import pandas as pd

def mostrar_dimensiones(datasets):
    """
    Muestra el numero de filas y columnas de cada DataFrame.

    Parametros:
        datasets: diccionario de DataFrames.

    Devuelve:
        DataFrame resumen con filas y columnas.
    """
    resumen = []

    for nombre, df in datasets.items():
        resumen.append({
            "dataset": nombre,
            "filas": df.shape[0],
            "columnas": df.shape[1]
        })

    return pd.DataFrame(resumen).sort_values(by="filas", ascending=False)

def mostrar_columnas(datasets):
    """
    Muestra las columnas de cada dataset.

    Parametros:
        datasets: diccionario de DataFrames.
    """
    for nombre, df in datasets.items():
        print(f"\nColumnas de {nombre}:")
        print(df.columns.tolist())


def resumen_tipos_datos(datasets):
    """
    Genera un resumen de los tipos de datos por dataset.

    Parametros:
        datasets: diccionario de DataFrames.

    Devuelve:
        DataFrame con dataset, columna y tipo de dato.
    """
    resumen = []

    for nombre, df in datasets.items():
        for columna, tipo in df.dtypes.items():
            resumen.append({
                "dataset": nombre,
                "columna": columna,
                "tipo_dato": tipo
            })

    return pd.DataFrame(resumen)
     
def resumen_nulos(datasets):
    """
    Calcula el numero y porcentaje de nulos por columna.

    Parametros:
        datasets: diccionario de DataFrames.

    Devuelve:
        DataFrame con resumen de nulos.
    """
    resumen = []

    for nombre, df in datasets.items():
        total_filas = len(df)

        for columna in df.columns:
            nulos = df[columna].isna().sum()
            porcentaje = (nulos / total_filas) * 100

            resumen.append({
                "dataset": nombre,
                "columna": columna,
                "nulos": nulos,
                "porcentaje_nulos": round(porcentaje, 2)
            })

    return pd.DataFrame(resumen).sort_values(
        by="porcentaje_nulos",
        ascending=False
    )

def resumen_duplicados(datasets):
    """
    Calcula el numero de filas duplicadas por dataset.

    Parametros:
        datasets: diccionario de DataFrames.

    Devuelve:
        DataFrame con el numero de duplicados.
    """
    resumen = []

    for nombre, df in datasets.items():
        duplicados = df.duplicated().sum()

        resumen.append({
            "dataset": nombre,
            "filas": len(df),
            "duplicados": duplicados
        })

    return pd.DataFrame(resumen)

def analizar_claves(datasets, claves):
    """
    Analiza si las claves principales son unicas o repetidas.

    Parametros:
        datasets: diccionario de DataFrames.
        claves: diccionario con dataset y columna clave.

    Devuelve:
        DataFrame con total de filas, valores unicos y repetidos.
    """
    resumen = []

    for nombre, clave in claves.items():
        df = datasets[nombre]

        resumen.append({
            "dataset": nombre,
            "clave": clave,
            "filas": len(df),
            "valores_unicos": df[clave].nunique(),
            "valores_repetidos": len(df) - df[clave].nunique()
        })

    return pd.DataFrame(resumen)
     
def resumen_calidad_datos(datasets):
    """
    Crea un resumen general de calidad para cada dataset.

    Parametros:
        datasets: diccionario de DataFrames.

    Devuelve:
        DataFrame con filas, columnas, nulos y duplicados.
    """
    resumen = []

    for nombre, df in datasets.items():
        total_nulos = df.isna().sum().sum()
        total_duplicados = df.duplicated().sum()

        resumen.append({
            "dataset": nombre,
            "filas": df.shape[0],
            "columnas": df.shape[1],
            "total_nulos": total_nulos,
            "total_duplicados": total_duplicados
        })

    return pd.DataFrame(resumen)
 
def detectar_encodings_archivos(lista_archivos):
    """
    Detecta el encoding de varios archivos.

    Parametros:
        lista_archivos: lista de rutas de archivos.
    """

    for archivo in lista_archivos:

        with open(archivo, "rb") as f:
            resultado = chardet.detect(f.read())

        print("-" * 50)
        print(f"Archivo: {Path(archivo).name}")
        print(f"Encoding: {resultado['encoding']}")
        print(f"Confianza: {resultado['confidence']:.2%}")
         
def resumen_tipos(df, nombre_dataset):
    """
    Muestra los tipos de datos de un DataFrame.

    Parametros:
        df: DataFrame a analizar.
        nombre_dataset: nombre identificativo del dataset.

    Devuelve:
        DataFrame con columna y tipo de dato.
    """
    return pd.DataFrame({
        "dataset": nombre_dataset,
        "columna": df.columns,
        "tipo_dato": df.dtypes.astype(str).values
    })

def resumen_nulos(df, nombre_dataset):
    """
    Calcula el numero y porcentaje de valores nulos por columna.

    Parametros:
        df: DataFrame a analizar.
        nombre_dataset: nombre del dataset.

    Devuelve:
        DataFrame con el resumen de nulos.
    """
    resumen = pd.DataFrame({
        "dataset": nombre_dataset,
        "columna": df.columns,
        "nulos": df.isna().sum().values,
        "porcentaje_nulos": (df.isna().mean().values * 100).round(2)
    })

    return resumen.sort_values(by="porcentaje_nulos", ascending=False)
     
def resumen_duplicados(datasets):
    """
    Calcula el numero de filas duplicadas por dataset.

    Parametros:
        datasets: diccionario de DataFrames.

    Devuelve:
        DataFrame con filas totales y duplicados.
    """
    resumen = []

    for nombre, df in datasets.items():
        resumen.append({
            "dataset": nombre,
            "filas": len(df),
            "duplicados": df.duplicated().sum()
        })

    return pd.DataFrame(resumen)
     
def resumen_nulos_final(df):
    """
    Calcula valores nulos del dataset final.

    Parametros:
        df: DataFrame final.

    Devuelve:
        DataFrame con resumen de nulos.
    """
    resumen = pd.DataFrame({
        "columna": df.columns,
        "nulos": df.isna().sum().values,
        "porcentaje_nulos": (df.isna().mean().values * 100).round(2)
    })

    return resumen.sort_values(by="porcentaje_nulos", ascending=False)
     
def obtener_kpis_generales(df):
    """
    Calcula los principales KPIs del negocio.
    """

    return pd.Series({
        "Pedidos": df["order_id"].nunique(),
        "Clientes": df["customer_unique_id"].nunique(),
        "Ventas Totales": round(df["order_total_value"].sum(), 2),
        "Ticket Medio": round(df["order_total_value"].mean(), 2),
        "Pedidos Entregados (%)": round(df["is_delivered"].mean() * 100, 2),
        "Pedidos Retrasados (%)": round(df["is_late"].mean() * 100, 2),
        "Pedidos en Festivo (%)": round(df["is_holiday"].mean() * 100, 2),
        "Coste Medio Envío": round(df["order_freight_value"].mean(), 2)
    })
     
def revisar_nulos(df):
    """
    Calcula el número y porcentaje de valores nulos por columna.

    Parametros
    ----------
    df : pd.DataFrame
        DataFrame con las variables que se quieren revisar.

    Devuelve
    --------
    pd.DataFrame
        Tabla con columnas, número de nulos y porcentaje de nulos.
    """

    resultado = pd.DataFrame({
        "nulos": df.isna().sum(),
        "porcentaje_nulos": df.isna().mean() * 100
    })

    resultado = (
        resultado
        .sort_values("porcentaje_nulos", ascending=False)
        .round(2)
    )

    return resultado
     

     

