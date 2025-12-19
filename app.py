import streamlit as st
import math
import pandas as pd

st.set_page_config(page_title="Molino Hidráulico", layout="centered")

st.title("🌊 Calculadora de Caudal – Molino Hidráulico")
st.markdown("**Mecánica de Fluidos – Método Volumétrico y Analítico**")

st.divider()

# =============================
# ENTRADA DE DATOS
# =============================
st.header("🔢 Ingreso de datos")

metodo = st.selectbox(
    "Seleccione el método de cálculo",
    ["Método volumétrico", "Método analítico", "Comparar ambos"]
)

st.subheader("Datos comunes")

