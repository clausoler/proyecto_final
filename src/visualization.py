import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns
 
def pedidos_por_mes(df):
    """
    Calcula el número de pedidos por mes.

    Parametros
    ----------
    df : pd.DataFrame

    Devuelve
    --------
    pd.DataFrame
    """
    resultado = (
        df.groupby(
            pd.Grouper(
                key="order_purchase_date",
                freq="M"
            )
        )["order_id"]
        .count()
        .reset_index()
    )

    return resultado

def analizar_estado_pedidos(df):
    """
    Calcula la distribución porcentual de los estados de pedido.

    Parámetros
    ----------
    df : pd.DataFrame
        Dataset final del proyecto.

    Devuelve
    --------
    pd.DataFrame
        Tabla con el porcentaje de pedidos por estado.
    """

    resultado = (
        df["order_status"]
        .value_counts(normalize=True)
        .mul(100)
        .round(2)
        .reset_index()
    )

    resultado.columns = [
        "order_status",
        "porcentaje"
    ]

    return resultado
     
def obtener_top_categorias_ventas(df, top_n=10):
    """
    Calcula las categorías que generan mayor volumen de ventas.

    Parámetros
    ----------
    df : pd.DataFrame
        Dataset final del proyecto.

    top_n : int, default=10
        Número de categorías a mostrar.

    Devuelve
    --------
    pd.DataFrame
        Categorías ordenadas por ventas descendentes.
    """

    resultado = (
        df.groupby("main_product_category", dropna=True)
        ["order_total_value"]
        .sum()
        .sort_values(ascending=False)
        .head(top_n)
        .reset_index()
    )

    return resultado
     
def obtener_distribucion_metodos_pago(df):
    """
    Calcula la distribución porcentual de los métodos de pago.

    Parámetros
    ----------
    df : pd.DataFrame
        Dataset final del proyecto.

    Devuelve
    --------
    pd.DataFrame
        Tabla con el porcentaje de pedidos por método de pago.
    """

    resultado = (
        df["payment_type_main"]
        .value_counts(normalize=True)
        .mul(100)
        .round(2)
        .reset_index()
    )

    resultado.columns = [
        "payment_type",
        "percentage"
    ]

    return resultado
     
def obtener_distribucion_articulos(df):
    """
    Calcula la distribución del número de artículos
    incluidos en cada pedido.

    Parámetros
    ----------
    df : pd.DataFrame
        Dataset final del proyecto.

    Devuelve
    --------
    pd.Series
        Frecuencia de pedidos por número de artículos.
    """

    return (
        df["total_items"]
        .dropna()
        .astype(int)
        .value_counts()
        .sort_index()
    )
     
def obtener_top_estados(df, top_n=10):
    """
    Calcula los estados con mayor volumen de pedidos.

    Parámetros
    ----------
    df : pd.DataFrame
        Dataset final.

    top_n : int, default=10
        Número de estados a mostrar.

    Devuelve
    --------
    pd.DataFrame
        Top estados por número de pedidos.
    """

    resultado = (
        df["customer_state"]
        .value_counts()
        .head(top_n)
        .reset_index()
    )

    resultado.columns = [
        "estado",
        "pedidos"
    ]

    return resultado
     
