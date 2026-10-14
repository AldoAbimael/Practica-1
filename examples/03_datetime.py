"""
Ejemplo 03: Librería Estándar 'datetime'
========================================
Manejo integral de fechas, horas, marcas temporales (timestamps),
zonas horarias (UTC), formateo/parseo con strftime/strptime y aritmética con timedelta.
"""

import sys
from datetime import date, datetime, time, timedelta, timezone

# Asegurar codificación UTF-8 en consolas Windows
if sys.platform == "win32" and hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


def demostrar_instancias_basicas():
    print("\n" + "=" * 50)
    print(" 1. CREACIÓN E INSPECCIÓN DE FECHAS Y HORAS")
    print("=" * 50)
    ahora_local = datetime.now()
    ahora_utc = datetime.now(timezone.utc)
    solo_fecha = date(2026, 10, 13)
    solo_hora = time(14, 30, 45, 500000)

    print(f"Fecha y hora actual (Local) : {ahora_local}")
    print(f"Fecha y hora actual (UTC)   : {ahora_utc}")
    print(f"Objeto date específico      : {solo_fecha} (Año: {solo_fecha.year}, Mes: {solo_fecha.month}, Día: {solo_fecha.day})")
    print(f"Objeto time específico      : {solo_hora} (Hora: {solo_hora.hour}, Min: {solo_hora.minute}, Seg: {solo_hora.second})")
    print(f"Timestamp Unix equivalente  : {ahora_local.timestamp():.0f} segundos desde la época")


def demostrar_formateo_y_parseo():
    print("\n" + "=" * 50)
    print(" 2. FORMATEO (strftime) Y PARSEO (strptime)")
    print("=" * 50)
    momento = datetime(2026, 12, 25, 20, 15, 30)

    # strftime: Objeto datetime -> Cadena de texto formateada
    formato_humano = momento.strftime("%d/%m/%Y %I:%M:%S %p")
    formato_iso = momento.isoformat()
    formato_extenso = momento.strftime("%A, %d de %B de %Y - Semana %W")

    print(f"Original datetime           : {momento}")
    print(f"Formato DD/MM/AAAA 12h      : {formato_humano}")
    print(f"Estándar ISO 8601           : {formato_iso}")
    print(f"Formato extendido           : {formato_extenso}")

    # strptime: Cadena de texto -> Objeto datetime estructurado
    cadena_fecha = "2026-08-15 09:45:00"
    patron = "%Y-%m-%d %H:%M:%S"
    fecha_parseada = datetime.strptime(cadena_fecha, patron)
    print(f"\nParseo desde string '{cadena_fecha}':")
    print(f"Objeto recuperado           : {repr(fecha_parseada)}")
    print(f"Día de la semana (0=Lunes)  : {fecha_parseada.weekday()}")


def demostrar_aritmetica_timedelta():
    print("\n" + "=" * 50)
    print(" 3. ARITMÉTICA TEMPORAL CON timedelta")
    print("=" * 50)
    hoy = datetime.now()
    plazo_entrega = timedelta(days=15, hours=4, minutes=30)
    fecha_limite = hoy + plazo_entrega
    hace_una_semana = hoy - timedelta(weeks=1)

    print(f"Fecha base de referencia    : {hoy.strftime('%Y-%m-%d %H:%M')}")
    print(f"Delta a aplicar             : +15 días, 4 horas y 30 min")
    print(f"Fecha resultante futura     : {fecha_limite.strftime('%Y-%m-%d %H:%M')}")
    print(f"Fecha pasada (-7 días)      : {hace_una_semana.strftime('%Y-%m-%d %H:%M')}")

    # Diferencia entre dos fechas
    fin_de_ano = datetime(hoy.year, 12, 31, 23, 59, 59)
    tiempo_restante = fin_de_ano - hoy
    print(f"\nTiempo restante para Fin de Año:")
    print(f"  - Días restantes          : {tiempo_restante.days} días")
    print(f"  - Segundos totales        : {tiempo_restante.total_seconds():,.0f} s")


def caso_practico_vencimiento_facturas():
    print("\n" + "=" * 50)
    print(" 4. CASO PRÁCTICO: GESTIÓN DE VENCIMIENTO DE FACTURAS")
    print("=" * 50)
    facturas = [
        {"id": "FAC-1001", "emision": "2026-09-01", "plazo_dias": 30},
        {"id": "FAC-1002", "emision": "2026-10-01", "plazo_dias": 15},
        {"id": "FAC-1003", "emision": "2026-10-10", "plazo_dias": 30},
    ]

    fecha_corte = datetime(2026, 10, 13)
    print(f"Fecha de auditoría: {fecha_corte.strftime('%Y-%m-%d')}\n")

    for fac in facturas:
        f_emision = datetime.strptime(fac["emision"], "%Y-%m-%d")
        f_vencimiento = f_emision + timedelta(days=fac["plazo_dias"])
        dias_diferencia = (fecha_corte - f_vencimiento).days

        if dias_diferencia > 0:
            estado = f"VENCIDA (Retraso de {dias_diferencia} días)"
        elif dias_diferencia == 0:
            estado = "VENCE HOY"
        else:
            estado = f"VIGENTE ({abs(dias_diferencia)} días restantes)"

        print(f"Factura: {fac['id']} | Emisión: {fac['emision']} | Vence: {f_vencimiento.strftime('%Y-%m-%d')} | Estado: {estado}")


def main():
    print("DEMOSTRACIÓN COMPLETA DE LA LIBRERÍA 'datetime'")
    demostrar_instancias_basicas()
    demostrar_formateo_y_parseo()
    demostrar_aritmetica_timedelta()
    caso_practico_vencimiento_facturas()
    print("\n" + "=" * 50)
    print("✓ Fin de la demostración de 'datetime'")
    print("=" * 50)


if __name__ == "__main__":
    main()
