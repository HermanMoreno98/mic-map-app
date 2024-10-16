import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd

class MICMACAnalysis:
    def __init__(self, factors, interactions):
        self.factors = factors
        self.interactions = interactions
        self.interaction_matrix = pd.DataFrame(interactions, index=factors, columns=factors)
        self.influence = self.interaction_matrix.sum(axis=0)
        self.depended_on = self.interaction_matrix.sum(axis=1)
 
    def display_results(self):
        st.write("\nMatriz de Interacciones:")
        st.dataframe(self.interaction_matrix)
 
        st.write("\nInfluencia (Interacciones Entrantes):")
        for factor, total in self.influence.items():
            st.write(f"{factor}: {total}")
 
        st.write("\nDependencia (Interacciones Salientes):")
        for factor, total in self.depended_on.items():
            st.write(f"{factor}: {total}")
 
    def plot_results(self):
        plt.figure(figsize=(10, 6))
        plt.scatter(self.depended_on, self.influence, color='blue')
 
        # Etiquetar los puntos
        for i, factor in enumerate(self.factors):
            plt.annotate(factor, (self.depended_on[i], self.influence[i]), fontsize=12)
 
        plt.title("Análisis MIC-MAC")
        plt.xlabel("Dependencia (Interacciones Salientes)")
        plt.ylabel("Influencia (Interacciones Entrantes)")
        plt.grid(True)
        plt.axhline(0, color='grey', lw=0.5)
        plt.axvline(0, color='grey', lw=0.5)
        plt.xlim(0, max(self.depended_on) + 1)
        plt.ylim(0, max(self.influence) + 1)
        st.pyplot(plt)
        
class MICMACAnalysis:
    def __init__(self, factors, interactions):
        self.factors = factors
        self.interactions = interactions
        self.interaction_matrix = pd.DataFrame(interactions, index=factors, columns=factors)
        self.influence = self.interaction_matrix.sum(axis=0)
        self.depended_on = self.interaction_matrix.sum(axis=1)
 
    def display_results(self):
        st.write("\nMatriz de Interacciones:")
        st.dataframe(self.interaction_matrix)
 
        st.write("\nInfluencia (Interacciones Entrantes):")
        for factor, total in self.influence.items():
            st.write(f"{factor}: {total}")
 
        st.write("\nDependencia (Interacciones Salientes):")
        for factor, total in self.depended_on.items():
            st.write(f"{factor}: {total}")
 
    def plot_results(self):
        plt.figure(figsize=(10, 6))
        plt.scatter(self.depended_on, self.influence, color='blue')
 
        # Etiquetar los puntos
        for i, factor in enumerate(self.factors):
            plt.annotate(factor, (self.depended_on[i], self.influence[i]), fontsize=12)
 
        plt.title("Análisis MIC-MAC")
        plt.xlabel("Dependencia (Interacciones Salientes)")
        plt.ylabel("Influencia (Interacciones Entrantes)")
        plt.grid(True)
        plt.axhline(0, color='grey', lw=0.5)
        plt.axvline(0, color='grey', lw=0.5)
        plt.xlim(0, max(self.depended_on) + 1)
        plt.ylim(0, max(self.influence) + 1)
        st.pyplot(plt)