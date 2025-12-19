# 🌊 Calculadora de Caudal – Molino Hidráulico

Aplicación web desarrollada en **Python con Streamlit** para calcular el **caudal de agua** en un molino hidráulico, usando datos experimentales y analíticos de Mecánica de Fluidos.

---

## 📐 Métodos de cálculo

### 🔹 Método volumétrico
Calcula el caudal a partir del volumen recolectado en un intervalo de tiempo:

Q = V / t

Donde:
- V: volumen de agua recolectado (m³)
- t: tiempo de recolección (s)

---

### 🔹 Método analítico
Calcula el caudal a partir del área de la sección transversal y la velocidad del flujo:

Q = A · v

Donde:
- A: área de la sección transversal de la manguera (m²)
- v: velocidad promedio del agua (m/s)

---

## 🛠️ Funcionalidades de la aplicación

- Ingreso interactivo de datos experimentales
- Cálculo automático del caudal
- Comparación entre método volumétrico y analítico
- Tabla resumen de resultados
- Export
