from mic_mac import MICMACAnalysis
import streamlit as st
 
def main():
    st.title("Aplicación de Análisis MIC-MAC")
    
    st.write("Bienvenido al aplicativo de análisis MIC-MAC.")
 
    # Entrada de factores
    factors_input = st.text_input("Ingrese los factores separados por comas:", "")
    factors = [factor.strip() for factor in factors_input.split(",") if factor]
 
    # Verificar si hay factores ingresados
    if len(factors) > 0:
        # Entrada de la matriz de interacciones
        interactions = []
        st.write("Ingrese las interacciones para cada factor (0=ninguna, 1=directa, 2=indirecta):")
        for factor in factors:
            row = st.text_input(f"Ingrese las interacciones para {factor} (separadas por comas):", "0,0,0")
            row = [int(r.strip()) for r in row.split(",")]
            interactions.append(row)
 
        # Si hay una matriz de interacciones válida
        if len(interactions) == len(factors):
            # Realizar el análisis MIC-MAC
            analysis = MICMACAnalysis(factors, interactions)
 
            # Mostrar resultados
            analysis.display_results()
 
            # Mostrar gráfico
            analysis.plot_results()

if __name__ == "__main__":
    main()