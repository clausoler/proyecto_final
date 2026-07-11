from pathlib import Path

import chardet

import pandas as pd
import numpy as np
 
def crear_variables_temporales(df, columna_fecha):
    """
    Crea variables temporales a partir de una columna de fecha.

    Parametros:
        df: DataFrame de entrada.
        columna_fecha: columna datetime base.

    Devuelve:
        DataFrame con nuevas variables temporales.
    """
    df = df.copy()

    df["order_purchase_date"] = df[columna_fecha].dt.normalize()
    df["purchase_year"] = df[columna_fecha].dt.year
    df["purchase_month"] = df[columna_fecha].dt.month
    df["purchase_day"] = df[columna_fecha].dt.day
    df["purchase_hour"] = df[columna_fecha].dt.hour
    df["purchase_dayofweek"] = df[columna_fecha].dt.dayofweek
    df["purchase_quarter"] = df[columna_fecha].dt.quarter

    return df
     
def crear_variables_logisticas(df):
    """
    Crea variables logísticas a partir de las fechas de pedidos.

    Parametros:
        df: DataFrame de pedidos.

    Devuelve:
        DataFrame con variables logísticas.
    """
    df = df.copy()

    df["approval_time_hours"] = (
        df["order_approved_at"] - df["order_purchase_timestamp"]
    ).dt.total_seconds() / 3600

    df["carrier_delivery_days"] = (
        df["order_delivered_carrier_date"] - df["order_approved_at"]
    ).dt.total_seconds() / 86400

    df["customer_delivery_days"] = (
        df["order_delivered_customer_date"] - df["order_purchase_timestamp"]
    ).dt.total_seconds() / 86400

    df["estimated_delivery_days"] = (
        df["order_estimated_delivery_date"] - df["order_purchase_timestamp"]
    ).dt.total_seconds() / 86400

    df["delay_days"] = (
        df["order_delivered_customer_date"] - df["order_estimated_delivery_date"]
    ).dt.total_seconds() / 86400

    return df
     
def crear_variables_estado_pedido(df):
    """
    Crea variables binarias a partir del estado del pedido.

    Parametros:
        df: DataFrame de pedidos.

    Devuelve:
        DataFrame con variables binarias.
    """
    df = df.copy()

    df["is_delivered"] = np.where(
        df["order_status"] == "delivered",
        1,
        0
    )

    df["is_canceled"] = np.where(
        df["order_status"] == "canceled",
        1,
        0
    )

    df["is_unavailable"] = np.where(
        df["order_status"] == "unavailable",
        1,
        0
    )

    df["is_late"] = np.where(
        df["delay_days"] > 0,
        1,
        0
    )

    return df

def agregar_items_por_pedido(items):
    """
    Agrega las líneas de pedido a nivel order_id.

    Parametros:
        items: DataFrame de líneas de pedido.

    Devuelve:
        DataFrame agregado por pedido.
    """
    items_agg = (
        items
        .groupby("order_id", as_index=False)
        .agg(
            total_items=("order_item_id", "count"),
            total_products=("product_id", "nunique"),
            order_products_value=("price", "sum"),
            order_freight_value=("freight_value", "sum"),
            avg_item_price=("price", "mean"),
            max_item_price=("price", "max")
        )
    )

    return items_agg
 
def agregar_pagos_por_pedido(payments):
    """
    Agrega los pagos a nivel order_id.

    Parametros:
        payments: DataFrame de pagos.

    Devuelve:
        DataFrame agregado por pedido.
    """
    payments_agg = (
        payments
        .groupby("order_id", as_index=False)
        .agg(
            total_payment_value=("payment_value", "sum"),
            payment_count=("payment_sequential", "count"),
            max_installments=("payment_installments", "max"),
            payment_type_main=("payment_type", lambda x: x.mode().iloc[0])
        )
    )

    return payments_agg
 
def categoria_principal_por_pedido(items_products):
    """
    Obtiene la categoría principal de cada pedido según el mayor importe de producto.

    Parametros:
        items_products: DataFrame de items enriquecido con productos y categorías.

    Devuelve:
        DataFrame con order_id y categoría principal.
    """
    categoria_agg = (
        items_products
        .groupby(
            [
                "order_id",
                "product_category_name_english"
            ],
            as_index=False
        )
        .agg(
            category_value=("price", "sum"),
            category_items=("order_item_id", "count")
        )
    )

    categoria_agg = categoria_agg.sort_values(
        by=["order_id", "category_value"],
        ascending=[True, False]
    )

    categoria_principal = (
        categoria_agg
        .drop_duplicates(subset=["order_id"], keep="first")
        .rename(columns={
            "product_category_name_english": "main_product_category"
        })
    )

    return categoria_principal[
        [
            "order_id",
            "main_product_category",
            "category_value",
            "category_items"
        ]
    ]

def crear_variables_economicas(df):
    """
    Crea variables economicas finales para el analisis.

    Parametros:
        df: DataFrame final.

    Devuelve:
        DataFrame con variables economicas derivadas.
    """
    df = df.copy()

    df["order_total_value"] = (
        df["order_products_value"]
        + df["order_freight_value"]
    )

    df["freight_ratio"] = np.where(
        df["order_total_value"] > 0,
        df["order_freight_value"] / df["order_total_value"],
        np.nan
    )

    df["avg_product_value_per_item"] = np.where(
        df["total_items"] > 0,
        df["order_products_value"] / df["total_items"],
        np.nan
    )

    return df

def crear_segmentacion_pedido(df):
    """
    Crea segmentos de pedido según valor y número de productos.

    Parametros:
        df: DataFrame final.

    Devuelve:
        DataFrame con variables de segmentación.
    """
    df = df.copy()

    df["order_value_segment"] = pd.cut(
        df["order_total_value"],
        bins=[-0.01, 50, 150, 500, np.inf],
        labels=[
            "bajo",
            "medio",
            "alto",
            "muy_alto"
        ]
    )

    df["items_segment"] = pd.cut(
        df["total_items"],
        bins=[-0.01, 1, 3, np.inf],
        labels=[
            "un_producto",
            "dos_tres_productos",
            "mas_de_tres_productos"
        ]
    )

    return df
     
def convertir_contadores_enteros(df):
    """
    Convierte variables de conteo a tipo entero nullable.
    """

    df = df.copy()

    columnas = [
        "total_items",
        "total_products",
        "payment_count",
        "max_installments"
    ]

    for columna in columnas:
        df[columna] = df[columna].astype("Int64")

    return df
 
def ajustar_tipos_finales(df):
    """
    Ajusta los tipos de datos finales del dataset
    antes de su exportación para análisis y Power BI.

    Parámetros:
        df (pd.DataFrame): Dataset final.

    Devuelve:
        pd.DataFrame: Dataset con tipos corregidos.
    """

    df = df.copy()

    columnas_enteras = [
        "total_items",
        "total_products",
        "payment_count",
        "max_installments",
        "category_items"
    ]

    for columna in columnas_enteras:
        df[columna] = df[columna].astype("Int64")

    df["payment_difference"] = (
        df["payment_difference"]
        .round(2)
    )

    return df
     
