import streamlit as st
import pandas as pd

# Configuração da Página
st.set_page_config(page_title="Dashboard Acadêmico", layout="wide")

def main():
    st.title("📊 Análise Gráfica de Desempenho")
    st.markdown("---")

    # Sidebar para entrada de dados
    with st.sidebar:
        st.header("Entrada de Notas")
        n1 = st.number_input("Nota 1º Bimestre", 0.0, 10.0, 5.0, 0.1)
        n2 = st.number_input("Nota 2º Bimestre", 0.0, 10.0, 5.0, 0.1)
        
        media = (n1 + n2) / 2
        st.metric("Média Calculada", f"{media:.2f}", delta=f"{media-6.0:.1f}")

    # Layout Principal
    col_texto, col_grafico = st.columns([1, 2])

    with col_texto:
        st.subheader("📋 Resumo")
        if media >= 6.0:
            st.success("**Status: Aprovado**")
        elif media >= 4.0:
            st.warning("**Status: Recuperação**")
        else:
            st.error("**Status: Reprovado**")
        
        st.write(f"Sua primeira nota foi **{n1}** e a segunda foi **{n2}**.")
        st.info("O gráfico ao lado mostra a comparação entre suas notas e a linha de corte (6.0).")

    with col_grafico:
        st.subheader("📈 Visualização de Notas")
        
        # Criando os dados para o gráfico
        dados_grafico = pd.DataFrame({
            "Avaliação": ["1º Bimestre", "2º Bimestre", "Média Final"],
            "Sua Nota": [n1, n2, media],
            "Média IF": [6.0, 6.0, 6.0] # Linha de referência
        }).set_index("Avaliação")

        # Exibindo o gráfico de barras nativo
        st.bar_chart(dados_grafico)

    # Gráfico de Área para "Evolução"
    st.markdown("---")
    st.subheader("🌊 Tendência de Desempenho")
    # Mostra se a nota subiu ou desceu entre os bimestres
    st.area_chart([n1, n2])

if __name__ == "__main__":
    main()
