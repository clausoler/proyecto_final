import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns
 
def resumen_estadistico(df):
    """
    Genera un resumen estadístico de las variables numéricas.

    Incluye conteo, media, desviación estándar, mínimo,
    percentiles principales y máximo.

    Parametros
    ----------
    df : pd.DataFrame
        DataFrame con variables numéricas.

    Devuelve
    --------
    pd.DataFrame
        Resumen estadístico transpuesto.
    """

    resumen = df.describe().T

    return resumen
     
def comparar_media_mediana(df):
    """
    Compara la media y la mediana de cada variable numérica.

    Esta comparación ayuda a detectar distribuciones asimétricas.
    Cuando la media es muy superior a la mediana, suele indicar
    presencia de valores extremos altos.

    Parametros
    ----------
    df : pd.DataFrame
        DataFrame con variables numéricas.

    Devuelve
    --------
    pd.DataFrame
        Tabla con media, mediana y diferencia entre ambas.
    """

    resultado = pd.DataFrame({
        "media": df.mean(),
        "mediana": df.median()
    })

    resultado["diferencia_media_mediana"] = (
        resultado["media"] - resultado["mediana"]
    )

    return resultado.round(2)
     
def analizar_forma_distribucion(df):
    """
    Calcula asimetría y curtosis de las variables numéricas.

    La asimetría permite identificar si la distribución está sesgada
    hacia valores altos o bajos.

    La curtosis permite evaluar si existen colas pesadas o valores
    extremos más frecuentes de lo esperado.

    Parametros
    ----------
    df : pd.DataFrame
        DataFrame con variables numéricas.

    Devuelve
    --------
    pd.DataFrame
        Tabla con asimetría y curtosis por variable.
    """

    resultado = pd.DataFrame({
        "asimetria": df.skew(),
        "curtosis": df.kurtosis()
    })

    return resultado.round(2)
     
def obtener_correlaciones_fuertes(matriz, umbral=0.7):
    """
    Extrae las correlaciones fuertes de una matriz de correlación.

    Parametros
    ----------
    matriz : pd.DataFrame
        Matriz de correlación.

    umbral : float, default=0.7
        Valor mínimo absoluto para considerar una correlación fuerte.

    Devuelve
    --------
    pd.DataFrame
        Pares de variables con correlación superior al umbral indicado.
    """

    matriz_abs = matriz.abs()

    mascara = np.triu(
        np.ones_like(matriz_abs),
        k=1
    ).astype(bool)

    correlaciones_filtradas = (
        matriz_abs
        .where(mascara)
        .stack()
        .reset_index()
    )

    correlaciones_filtradas.columns = [
        "variable_1",
        "variable_2",
        "correlacion"
    ]

    correlaciones_filtradas = (
        correlaciones_filtradas[
            correlaciones_filtradas["correlacion"] >= umbral
        ]
        .sort_values("correlacion", ascending=False)
    )

    return correlaciones_filtradas

def detectar_outliers_iqr(serie):
    """
    Detecta valores atípicos utilizando el método del rango intercuartílico.

    Un valor se considera outlier si se encuentra por debajo de:
    Q1 - 1.5 * IQR

    o por encima de:
    Q3 + 1.5 * IQR

    Parametros
    ----------
    serie : pd.Series
        Variable numérica sobre la que detectar outliers.

    Devuelve
    --------
    dict
        Diccionario con límites inferior y superior, número de outliers
        y porcentaje de outliers.
    """

    serie = serie.dropna()

    q1 = serie.quantile(0.25)
    q3 = serie.quantile(0.75)

    iqr = q3 - q1

    limite_inferior = q1 - 1.5 * iqr
    limite_superior = q3 + 1.5 * iqr

    outliers = (
        (serie < limite_inferior)
        |
        (serie > limite_superior)
    )

    resultado = {
        "limite_inferior": limite_inferior,
        "limite_superior": limite_superior,
        "numero_outliers": outliers.sum(),
        "porcentaje_outliers": outliers.mean() * 100
    }

    return resultado
     
def resumir_outliers(df, columnas):
    """
    Aplica la detección de outliers por IQR a varias columnas.

    Parametros
    ----------
    df : pd.DataFrame
        Dataset que contiene las columnas numéricas.

    columnas : list
        Lista de columnas sobre las que se quiere detectar outliers.

    Devuelve
    --------
    pd.DataFrame
        Resumen de outliers por variable.
    """

    resultados = []

    for columna in columnas:
        resultado = detectar_outliers_iqr(df[columna])
        resultado["variable"] = columna
        resultados.append(resultado)

    resumen = pd.DataFrame(resultados)

    columnas_orden = [
        "variable",
        "limite_inferior",
        "limite_superior",
        "numero_outliers",
        "porcentaje_outliers"
    ]

    resumen = resumen[columnas_orden]

    return resumen.round(2)
     
