import streamlit as st
from engine_calculo import Calculadora, OPERACOES

st.set_page_config(page_title="Calculadora Inteligente Gemini", page_icon="🧮")

st.sidebar.markdown(
    "Projeto estruturado por Gemini 1.5 Pro e executado por Flash"
)

st.title("Calculadora Inteligente Gemini")

a = st.number_input("Primeiro número", value=0.0, format="%f")
b = st.number_input("Segundo número", value=0.0, format="%f")

operador = st.selectbox("Operação", list(OPERACOES.keys()))

if st.button("Calcular"):
    calc = Calculadora()
    metodo = OPERACOES[operador]
    try:
        resultado = metodo(calc, a, b)
        st.success(f"Resultado: {resultado}")
    except ValueError as e:
        st.error(str(e))
