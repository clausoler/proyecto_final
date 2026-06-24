# Diccionario de Variables del Dataset Final

## Variables originales

| Variable | Origen | Descripción |
|-----------|---------|-------------|
| order_id | Orders | Identificador único del pedido. |
| customer_id | Orders | Identificador del cliente asociado al pedido. |
| order_status | Orders | Estado actual del pedido (delivered, canceled, unavailable, etc.). |
| order_purchase_timestamp | Orders | Fecha y hora en que se realizó la compra. |
| order_approved_at | Orders | Fecha y hora en que se aprobó el pago del pedido. |
| order_delivered_carrier_date | Orders | Fecha y hora en que el pedido fue entregado al transportista. |
| order_delivered_customer_date | Orders | Fecha y hora en que el pedido fue entregado al cliente. |
| order_estimated_delivery_date | Orders | Fecha estimada de entrega proporcionada al cliente. |
| customer_unique_id | Customers | Identificador único del cliente real. Permite identificar clientes repetidos. |
| customer_zip_code_prefix | Customers | Prefijo del código postal del cliente. |
| customer_city | Customers | Ciudad de residencia del cliente. |
| customer_state | Customers | Estado de residencia del cliente. |
| holiday_name | Holidays | Nombre original del festivo asociado a la fecha del pedido. |
| holiday_name_normalized | Holidays | Nombre normalizado del festivo para facilitar análisis y comparaciones. |

---

## Variables agregadas

### Información agregada de Items

| Variable | Origen | Descripción |
|-----------|---------|-------------|
| total_items | Items | Número total de artículos incluidos en el pedido. |
| total_products | Items | Número de productos distintos incluidos en el pedido. |
| order_products_value | Items | Importe total de los productos comprados. |
| order_freight_value | Items | Coste total de envío asociado al pedido. |
| avg_item_price | Items | Precio medio de los artículos del pedido. |
| max_item_price | Items | Precio del artículo más caro del pedido. |

### Información agregada de Payments

| Variable | Origen | Descripción |
|-----------|---------|-------------|
| total_payment_value | Payments | Importe total pagado por el cliente. |
| payment_count | Payments | Número de registros de pago asociados al pedido. |
| max_installments | Payments | Número máximo de cuotas utilizadas en el pago. |
| payment_type_main | Payments | Método de pago principal utilizado en el pedido. |

### Información agregada de Products

| Variable | Origen | Descripción |
|-----------|---------|-------------|
| main_product_category | Products | Categoría principal de productos presente en el pedido. |
| category_value | Products | Valor económico total de la categoría principal dentro del pedido. |
| category_items | Products | Número de artículos pertenecientes a la categoría principal. |

---

## Variables derivadas

### Variables temporales

| Variable | Descripción |
|-----------|-------------|
| order_purchase_date | Fecha de compra sin componente horaria. |
| purchase_year | Año de realización del pedido. |
| purchase_month | Mes de realización del pedido. |
| purchase_day | Día del mes en que se realizó la compra. |
| purchase_hour | Hora del día en que se realizó la compra. |
| purchase_dayofweek | Día de la semana de la compra (0=Lunes, 6=Domingo). |
| purchase_quarter | Trimestre del año en que se realizó la compra. |

### Variables logísticas

| Variable | Descripción |
|-----------|-------------|
| approval_time_hours | Tiempo transcurrido entre la compra y la aprobación del pedido (horas). |
| carrier_delivery_days | Tiempo transcurrido entre la aprobación y la entrega al transportista (días). |
| customer_delivery_days | Tiempo transcurrido entre la compra y la entrega al cliente (días). |
| estimated_delivery_days | Tiempo estimado de entrega comunicado al cliente (días). |
| delay_days | Diferencia entre la fecha real y la fecha estimada de entrega. Valores negativos indican entregas adelantadas. |

### Variables económicas

| Variable | Descripción |
|-----------|-------------|
| order_total_value | Valor total del pedido (productos + envío). |
| freight_ratio | Proporción que representa el coste de envío sobre el valor total del pedido. |
| avg_product_value_per_item | Valor medio por artículo comprado. |
| payment_difference | Diferencia entre el valor calculado del pedido y el importe realmente pagado. |

### Variables indicadoras

| Variable | Descripción |
|-----------|-------------|
| is_delivered | Indicador binario de pedido entregado (1=Sí, 0=No). |
| is_canceled | Indicador binario de pedido cancelado (1=Sí, 0=No). |
| is_unavailable | Indicador binario de pedido no disponible (1=Sí, 0=No). |
| is_late | Indicador binario de pedido retrasado respecto a la fecha estimada (1=Sí, 0=No). |
| is_holiday | Indicador binario de compra realizada en festivo (1=Sí, 0=No). |
| carrier_before_approval | Indicador binario que identifica pedidos entregados al transportista antes de la aprobación registrada. Utilizado para control de calidad de datos. |

### Variables de segmentación

| Variable | Descripción |
|-----------|-------------|
| order_value_segment | Segmento económico del pedido (bajo, medio, alto o muy alto) según su importe total. |
| items_segment | Segmento basado en la cantidad de artículos incluidos en el pedido. |

---

## Resumen de la estructura

| Tipo de variable | Cantidad |
|------------------|---------:|
| Variables originales | 14 |
| Variables agregadas | 13 |
| Variables derivadas | 24 |
| **Total** | **51** |
