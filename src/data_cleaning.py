from pathlib import Path

import chardet

import pandas as pd
 
  
def eliminar_columnas(df, columnas):
    """
    Elimina columnas de un DataFrame si existen.

    Parametros:
        df: DataFrame de entrada.
        columnas: lista de columnas a eliminar.

    Devuelve:
        DataFrame sin las columnas indicadas.
    """
    columnas_existentes = [col for col in columnas if col in df.columns]

    return df.drop(columns=columnas_existentes)

def corregir_encoding(texto):
    """
    Corrige problemas de codificación en cadenas de texto que han sido
    interpretadas incorrectamente entre los formatos Latin-1 y UTF-8.

    Esta función es útil para recuperar caracteres especiales que aparecen
    corruptos tras la lectura de archivos CSV, por ejemplo:

    - "Pã¡scoa" -> "Páscoa"
    - "Independãªncia" -> "Independência"
    - "Proclamaã§ã£o" -> "Proclamação"

    Parámetros
    ----------
    texto : str
        Cadena de texto a corregir.

    Devuelve
    --------
    str
        Texto corregido. Si la conversión no es posible o el valor es nulo,
        devuelve el valor original.
    """

    if pd.isna(texto):
        return texto

    try:
        return texto.encode("latin1").decode("utf-8")
    except Exception:
        return texto

def limpiar_texto(df, columnas):
    """
    Limpia columnas de texto eliminando espacios al inicio y final
    y convirtiendo los valores a minusculas.

    Parametros:
        df: DataFrame de entrada.
        columnas: lista de columnas de texto.

    Devuelve:
        DataFrame con columnas de texto normalizadas.
    """
    df = df.copy()

    for columna in columnas:
        if columna in df.columns:
            df[columna] = (
                df[columna]
                .astype("string")
                .str.strip()
                .str.lower()
            )

    return df
     
def convertir_a_texto(df, columnas):
    """
    Convierte columnas a tipo object.

    Parametros:
        df: DataFrame de entrada.
        columnas: lista de columnas a convertir.

    Devuelve:
        DataFrame con las columnas convertidas a object.
    """
    df = df.copy()

    for columna in columnas:
        if columna in df.columns:
            df[columna] = df[columna].astype("object")

    return df

def convertir_fechas(df, columnas):
    """
    Convierte columnas a formato datetime.

    Parametros:
        df: DataFrame de entrada.
        columnas: lista de columnas de fecha.

    Devuelve:
        DataFrame con columnas convertidas a datetime.
    """
    df = df.copy()

    for columna in columnas:
        if columna in df.columns:
            df[columna] = pd.to_datetime(
                df[columna],
                errors="coerce"
            )

    return df
 
