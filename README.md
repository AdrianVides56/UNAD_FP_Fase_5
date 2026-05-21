## Programa de clasificación de compromiso de clientes

Este programa evalúa el nivel de compromiso de sesiones de clientes con base en su duración y cantidad de clics.

### Requisitos del ejercicio

- Datos iniciales: al menos 5 sesiones de cliente en una lista.
- Módulos:
  - función de cálculo de clasificación de compromiso.
- Lógica de negocio:
  - `Alto` si `duración > 180` y `clics > 8`
  - `Bajo` si `duración < 60` o `clics < 3`
  - `Medio` en los demás casos
- Salida:
  - informe en tabla con `ID del cliente` y la `clasificación final`

---

## Descripción

El programa define:

- una clase `Cliente` con `ID`, `duracion`, `clics` y `clasificacion`
- un `Enum` `ClasificacionCompromiso` con valores `ALTO`, `MEDIO` y `BAJO`
- funciones para:
  - crear clientes mediante entrada de usuario
  - validar duración y clics
  - calcular la clasificación de compromiso
  - clasificar clientes
  - imprimir resultados en una tabla ajustada al ancho

---

## Cómo usar

1. Ejecuta el archivo principal:

```bash
python problema1.py
```

2. En el menú, elige una opción:
- `1` para ver resultados
- `2` para agregar un nuevo cliente
- `3` para salir

3. Si eliges agregar un cliente, ingresa:
- duración en segundos
- número de clics

---

## Estructura de funciones

- `crear_cliente()`
- `ingresar_duracion()`
- `ingresar_clics()`
- `calcular_compromiso(cliente)`
- `clasificar_cliente(cliente)`
- `clasificar_clientes(clientes)`
- `imprimir_resultados(clientes)`
- `mostrar_menu()`

---

## Ejemplo de reglas de clasificación

- Cliente con `200s` y `10 clics` → `Alto`
- Cliente con `20s` o `2 clics` → `Bajo`
- Cliente con `100s` y `5 clics` → `Medio`
