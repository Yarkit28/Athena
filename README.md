# Athena — Sistema de Cálculos y Planificación Financiera

**Athena** es una plataforma modular y desacoplada para cálculos financieros, proyección de inversiones, análisis de préstamos y planificación de retiro. El proyecto está construido bajo una **Arquitectura en 3 Capas (Limpia)**, lo que garantiza la portabilidad de sus motores de cálculo y la independencia total de las interfaces de usuario.

---

## 🏛️ Arquitectura del Sistema

El proyecto sigue un diseño estrictamente desacoplado donde la presentación, la orquestación de negocio y las matemáticas financieras residen en capas aisladas:

```
+-------------------------------------------------------------+
|                   CAPA DE PRESENTACIÓN                      |
|      CLI (cli/input_helpers.py)  |  GUI (gui/main_gui.py)   |
+------------------------------+------------------------------+
                               |
                               v
+-------------------------------------------------------------+
|                    CAPA DE APLICACIÓN                       |
|               finanzas_app/ (casos_uso.py)                  |
|  - Validaciones de entrada y manejo de excepciones          |
|  - DTOs y formateo de respuestas                            |
+------------------------------+------------------------------+
                               |
                               v
+-------------------------------------------------------------+
|                    CAPA CORE / DOMINIO                      |
|                  finanzas_core/ (intereses, credito)        |
|  - Fórmulas puras, sin dependencias de I/O ni GUI           |
+-------------------------------------------------------------+
```

### Principios Clave:
* **Invariancia del Core:** El motor `finanzas_core` no tiene dependencias externas ni maneja interfaz de usuario.
* **Capa de Aplicación (`finanzas_app`):** Unifica la lógica de los casos de uso y emite excepciones personalizadas (`ErrorValidacionEntrada`, `ErrorCalculoInvalido`).
* **Soporte Multicliente:** La interfaz de línea de comandos (CLI) y la interfaz gráfica (GUI) consumen exactamente los mismos servicios de la capa de aplicación.

---

## 🚀 Funcionalidades Principales

### 1. Interés Simple y Compuesto
* Cálculo de valor futuro, valor presente, tiempo y tasa efectiva.
* Proyección de interés compuesto con capitalización en distintos periodos ($M = P(1 + r/n)^{nt}$).
* Descuentos comerciales e intereses devengados.

### 2. Crédito y Amortización
* Cálculo de cuota mensual amortizable para préstamos.
* Simulador de pagos extraordinarios y reducción de plazos/intereses.
* Tablas de amortización dinámicas con apoyo para pagos fijos, pagos porcentuales y cargos recurrentes.

### 3. Planificación de Retiro y Libertad Financiera
* Estimación del fondo necesario mediante la Regla del 4% y cálculo ajustado a rendimiento.
* Proyección de aportes recurrentes combinados con ajustes por inflación.
* Estimación de ingresos mensuales sostenibles durante la jubilación.

---

## 📁 Estructura del Proyecto

```
Athena/
├── finanzas_core/          # Capa Dominio / Motor Matemático Puro
│   ├── intereses.py        # Fórmulas de interés, préstamos y retiro
│   └── credito.py          # Tablas y lógica de amortización
├── finanzas_app/           # Capa de Aplicación / Servicios
│   ├── __init__.py         # Exportación pública del paquete
│   ├── errores.py          # Jerarquía de excepciones personalizadas
│   └── casos_uso.py        # Orquestación de casos de uso financieros
├── cli/                    # Interfaz en Línea de Comandos
│   └── input_helpers.py    # Manejo interactivo de entradas de usuario
├── gui/                    # Interfaz Gráfica de Usuario (Tkinter)
│   └── main_gui.py         # Aplicación Tkinter desacoplada de 3 capas
├── docs/                   # Documentación de Arquitectura y ADRs
│   └── decision_gui.md     # ADR-003: Selección de tecnología GUI
├── tests/                  # Pruebas Automatizadas e Integradas
│   ├── test_application.py
│   ├── test_cli_compatibilidad.py
│   └── test_mision3_2.py
└── README.md               # Documentación general del proyecto
```

---

## 🛠️ Requisitos e Instalación

El proyecto está diseñado para funcionar de manera nativa sin necesidad de librerías de terceros pesadas:

* **Python:** 3.10 o superior (Probado en Python 3.13).
* **GUI Framework:** Standard `tkinter` (incluido en la instalación oficial de Python).

### Ejecución de la Interfaz Gráfica (GUI)
```bash
python -m gui.main_gui
```

### Ejecución de la Suite de Pruebas Reproducibles
Para verificar la compatibilidad, integración de capas y no-regresión de la CLI:
```bash
python -m unittest discover -s tests
```

---

## 📄 Decisiones de Arquitectura (ADR)

* **ADR-003 (GUI):** Se seleccionó Tkinter Estándar para la GUI con el patrón *App Service Layer*, asegurando 100% de portabilidad en Windows, Linux y macOS sin requerir entornos virtuales con binarios compilados de C++.