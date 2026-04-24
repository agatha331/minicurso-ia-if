import streamlit as st
import pandas as pd

# Configuração de Layout
st.set_page_config(page_title="Analista de Notas IF", page_icon="🎓", layout="wide")

def main():
    # Estilização CSS para melhorar o visual dos cards
    st.markdown("""
        <style>
        .stMetric { background-color: #ffffff; padding: 15px; border-radius: 10px; box-shadow: 0 2px 4px rgba(0,0,0,0.05); }
        footer {visibility: hidden;}
        </style>
    """, unsafe_allow_html=True)

    st.title("🎓 Analista de Desempenho Acadêmico")
    st.subheader("Cálculo de Média e Projeção de Resultados")
    st.divider()

    # Área de Entrada de Dados (Sidebar para deixar o centro livre para os gráficos)
    with st.sidebar:
        st.header("📝 Lançamento de Notas")
        n1 = st.number_input("Nota 1º Bimestre", min_value=0.0, max_value=10.0, value=5.0, step=0.1)
        n2 = st.number_input("Nota 2º Bimestre", min_value=0.0, max_value=10.0, value=5.0, step=0.1)
        
        st.write("")
        calcular = st.button("🚀 Calcular e Gerar Relatório", use_container_width=True)

    # Lógica Principal (Só aparece após o clique ou se os valores mudarem)
    media = (n1 + n2) / 2
    
    # Criamos três colunas para as métricas principais
    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(label="Média Final", value=f"{media:.2f}", delta=f"{media-6.0:.1f}")
    
    with col2:
        status = "APROVADO" if media >= 6.0 else "RECUPERAÇÃO" if media >= 4.0 else "REPROVADO"
        st.metric(label="Situação", value=status)
        
    with col3:
        progresso = (media / 10.0)
        st.write("**Aproveitamento Total**")
        st.progress(progresso)

    st.divider()

    # SEÇÃO DE GRÁFICOS (Aparece logo abaixo das métricas)
    col_graf1, col_graf2 = st.columns(2)

    with col_graf1:
        st.markdown("### 📊 Comparativo de Bimestres")
        # Criando um DataFrame para o gráfico de barras
        df_notas = pd.DataFrame({
            "Bimestre": ["1º Bim", "2º Bim"],
            "Nota": [n1, n2]
        }).set_index("Bimestre")
        
        st.bar_chart(df_notas, color="#2e7d32")

    with col_graf2:
        st.markdown("### 📈 Evolução vs Meta")
        # Gráfico de área mostrando a oscilação em relação à média 6.0
        df_evolucao = pd.DataFrame({
            "Notas": [n1, n2],
            "Meta (6.0)": [6.0, 6.0]
        })
        st.line_chart(df_evolucao)

    # Feedback Contextual (Mensagens de texto baseadas no resultado)
    if media >= 6.0:
        st.balloons()
        st.success(f"🎉 **Parabéns!** Você atingiu a meta com uma média de {media:.2f}.")
    elif media >= 4.0:
        st.warning(f"⚠️ **Quase lá!** Você está em recuperação. Precisa de {(10 - media):.1f} pontos no exame final.")
    else:
        st.error("🚨 **Atenção:** Seu rendimento está abaixo do mínimo para recuperação direta.")

if __name__ == "__main__":
    main()
