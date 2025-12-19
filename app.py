import streamlit as st
import math
import pandas as pd
import io


# =============================
# CONFIGURACIÓN DE PÁGINA
# =============================
st.set_page_config(
    page_title="Molino Hidráulico",
    layout="centered"
)

# =============================
# TÍTULO
# =============================
st.title("🌊 Calculadora de Caudal – Molino Hidráulico")
st.markdown("**Mecánica de Fluidos – Método Volumétrico y Analítico**")
st.divider()

# =============================
# SELECCIÓN DE MÉTODO
# =============================
st.header("🔢 Ingreso de datos")

metodo = st.selectbox(
    "Seleccione el método de cálculo",
    ["Método volumétrico", "Método analítico", "Comparar ambos"]
)

# =============================
# DATOS COMUNES
# =============================
st.subheader("📥 Datos comunes")

volumen_L = st.number_input(
    "Volumen recolectado (litros)",
    min_value=0.0,
    value=3.0
)

tiempo_recoleccion = st.number_input(
    "Tiempo de recolección (s)",
    min_value=0.0,
    value=12.0
)

# Conversión a m³
volumen_m3 = volumen_L / 1000

# =============================
# MÉTODO VOLUMÉTRICO
# =============================
if metodo in ["Método volumétrico", "Comparar ambos"]:
    Q1 = volumen_m3 / tiempo_recoleccion

# =============================
# MÉTODO ANALÍTICO
# =============================
if metodo in ["Método analítico", "Comparar ambos"]:
    st.subheader("📐 Datos del método analítico")

    diametro = st.number_input(
        "Diámetro interno de la manguera (m)",
        min_value=0.0,
        value=0.012
    )

    longitud = st.number_input(
        "Longitud del tramo observado (m)",
        min_value=0.0,
        value=0.30
    )

    tiempo_flujo = st.number_input(
        "Tiempo de recorrido del flujo (s)",
        min_value=0.0,
        value=0.9
    )

    area = math.pi * (diametro / 2) ** 2
    velocidad = longitud / tiempo_flujo
    Q2 = area * velocidad

# =============================
# RESULTADOS
# =============================
st.divider()
st.header("📊 Resultados")

if st.button("Calcular caudal"):
    datos = []

    if metodo in ["Método volumétrico", "Comparar ambos"]:
        st.subheader("🔹 Método volumétrico")
        st.write(f"Caudal Q₁ = **{Q1:.5e} m³/s**")
        datos.append(["Volumétrico", Q1])

    if metodo in ["Método analítico", "Comparar ambos"]:
        st.subheader("🔹 Método analítico")
        st.write(f"Área = {area:.5e} m²")
        st.write(f"Velocidad = {velocidad:.2f} m/s")
        st.write(f"Caudal Q₂ = **{Q2:.5e} m³/s**")
        datos.append(["Analítico", Q2])

    # =============================
    # TABLA Y EXPORTACIÓN
    # =============================
    df = pd.DataFrame(datos, columns=["Método", "Caudal (m³/s)"])
    st.subheader("📋 Resumen de resultados")
    st.dataframe(df)

    buffer = BytesIO()
buffer = io.BytesIO()
df.to_excel(buffer, index=False)
buffer.seek(0)

st.download_button(
    label="📥 Descargar resultados en Excel",
    data=buffer,
    file_name="resultados_molino_hidraulico.xlsx",
    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
)

buffer.seek(0)

st.download_button(
    label="📥 Descargar resultados en Excel",
    data=buffer,
    file_name="resultados_molino_hidraulico.xlsx",
    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
)

