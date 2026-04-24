import streamlit as st
import time

# 1. Configuração de Estilo e Página
st.set_page_config(
    page_title="Analytics Acadêmico IF",
    page_icon="🎓",
    layout="wide"
)

# CSS Customizado para um visual "Clean & Modern"
st.markdown("""
    <style>
    .main { background-color: #f0f2f6; }
    div[data-testid="stMetricValue"] { font-size: 40px; color: #1E3A8A; }
    .stProgress > div > div > div > div { background-image: linear-gradient(to right, #4ade80, #22c55e); }
    .status-card {
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #2e7d32;
        background-color: white;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.05);
    }
    </style>
    """, unsafe_allow_html=True)

# 2. Lógica de Negócio
def calcular_status(media):
    if media >= 6.0:
        return "APROVADO", "✅", "success"
    elif media >= 4.0:
        return "RECUPERAÇÃO", "⚠️", "warning"
    else:
        return "REPROVADO", "🚨", "error"

def main():
    # Header Principal
    st.title("🎓 Portal de Performance Acadêmica")
    st.markdown(f"**Data do Sistema:** {time.strftime('%d/%m/%Y')}")
    st.divider()

    # 3. Layout de Colunas
    col_input, col_display = st.columns([1, 2], gap="large")

    with col_input:
        st.markdown("### 📥 Entrada de Dados")
        # Inputs modernos com sliders e números
        n1 = st.slider("Nota do 1º Bimestre", 0.0, 10.0, 5.0, 0.1)
        n2 = st.slider("Nota do 2º Bimestre", 0.0, 10.0, 5.0, 0.1)
        
        st.divider()
        st.info("**Regra IF:** Média mínima 6.0 para aprovação direta.")

    # Cálculos
    media = (n1 + n2) / 2
    status, icone, tipo_alerta = calcular_status(media)

    with col_display:
        st.markdown(f"### 📊 Análise de Rendimento")
        
        # Dashboard de Métricas
        m1, m2, m3 = st.columns(3)
        
        with m1:
            st.metric("Média Atual", f"{media:.1f}", delta=f"{media-6.0:.1f}" if media != 6.0 else None)
        
        with m2:
            st.metric("Status", status)
            
        with m3:
            # Cálculo de objetivo
            objetivo = "Meta Atingida" if media >= 6.0 else f"Faltam {6.0 - media:.1f}"
            st.metric("Objetivo", objetivo)

        # Barra de Progresso Visual
        st.markdown(f"**Progresso para Aprovação (Meta 6.0):**")
        progresso = min(media / 6.0, 1.0) # Normaliza até 100% da meta
        st.progress(progresso)

        # 4. Painel de Feedback Contextual
        st.markdown("---")
        if tipo_alerta == "success":
            st.balloons()
            st.success(f"### {icone} Excelente Trabalho!\nO aluno demonstrou domínio dos conteúdos e superou a média mínima.")
        elif tipo_alerta == "warning":
            st.warning(f"### {icone} Atenção Necessária\nO aluno está em recuperação. Recomenda-se revisão dos tópicos do 1º bimestre.")
        else:
            st.error(f"### {icone} Alerta de Desempenho\nRendimento crítico. Necessário agendamento de tutoria pedagógica.")

    # 5. Detalhes Adicionais em Expander (Clean UI)
    with st.expander("🔍 Ver memória de cálculo e detalhes"):
        st.write(f"""
        - **Soma das Notas:** {n1 + n2}
        - **Divisor:** 2
        - **Média Final:** {media:.2f}
        - **Distância da Meta:** {abs(6.0 - media):.2f} pontos.
        """)

if __name__ == "__main__":
    main()
