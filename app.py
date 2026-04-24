import streamlit as st

# Configuração da Página
st.set_page_config(
    page_title="Analytics Acadêmico | IF",
    page_icon="📈",
    layout="wide"
)

# Funções de Lógica
def calcular_media(n1: float, n2: float) -> float:
    return (n1 + n2) / 2

def calcular_final(media_atual: float) -> float:
    # Exemplo de regra: (Média + Final) / 2 = 5.0 -> Logo: Final = 10 - Média
    return max(0.0, 10.0 - media_atual)

def main():
    # Estilização Avançada
    st.markdown("""
        <style>
        [data-testid="stMetricValue"] { font-size: 45px; font-weight: bold; }
        .stProgress > div > div > div > div { background-color: #2e7d32; }
        .main-card {
            background-color: #ffffff;
            padding: 20px;
            border-radius: 15px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            margin-bottom: 20px;
        }
        </style>
    """, unsafe_allow_html=True)

    # Header de Impacto
    st.title("📈 Dashboard de Desempenho Acadêmico")
    st.caption("Sistema Integrado de Gestão de Notas - Instituto Federal")
    st.divider()

    # Layout em Colunas (Input na Esquerda, Visual na Direita)
    col_input, col_viz = st.columns([1, 1.5], gap="large")

    with col_input:
        st.subheader("📋 Lançamento de Notas")
        with st.container():
            n1 = st.slider("Nota do 1º Bimestre", 0.0, 10.0, 5.0, 0.1)
            n2 = st.slider("Nota do 2º Bimestre", 0.0, 10.0, 5.0, 0.1)
            
            st.info("💡 Arraste os seletores para simular o resultado em tempo real.")

    media = calcular_media(n1, n2)

    with col_viz:
        # Gráfico Gauge (Velocímetro)
        fig = go.Figure(go.Indicator(
            mode = "gauge+number",
            value = media,
            domain = {'x': [0, 1], 'y': [0, 1]},
            title = {'text': "Média Calculada", 'font': {'size': 24}},
            gauge = {
                'axis': {'range': [None, 10], 'tickwidth': 1},
                'bar': {'color': "#1f77b4"},
                'steps': [
                    {'range': [0, 4], 'color': "#ff4b4b"},
                    {'range': [4, 6], 'color': "#ffa500"},
                    {'range': [6, 10], 'color': "#2e7d32"}
                ],
                'threshold': {
                    'line': {'color': "black", 'width': 4},
                    'thickness': 0.75,
                    'value': 6.0
                }
            }
        ))
        fig.update_layout(height=350, margin=dict(l=20, r=20, t=50, b=20))
        st.plotly_chart(fig, use_container_width=True)

    # Painel de Status Inferior
    st.markdown("---")
    res_col1, res_col2, res_col3 = st.columns(3)

    with res_col1:
        status = "APROVADO" if media >= 6.0 else "RECUPERAÇÃO" if media >= 4.0 else "REPROVADO"
        cor = "normal" if media >= 6.0 else "inverse"
        st.metric("Situação Atual", status, delta=None, delta_color=cor)

    with res_col2:
        st.metric("Média Final", f"{media:.2f}", delta=f"{media-6.0:.1f}", delta_color="normal")

    with res_col3:
        if media < 6.0:
            nota_necessaria = calcular_final(media)
            st.metric("Precisa na Final", f"{nota_necessaria:.1f}", delta="Cuidado", delta_color="inverse")
        else:
            st.metric("Margem de Segurança", f"{media-6.0:.1f}", delta="Seguro", delta_color="normal")

    # Mensagens de Feedback Dinâmico
    if media >= 6.0:
        st.success(f"### 🎉 Excelente! \nVocê superou a meta institucional por **{media-6.0:.2f}** pontos.")
    elif media >= 4.0:
        st.warning(f"### ⚠️ Atenção! \nVocê está em recuperação. Precisará de uma nota **{calcular_final(media):.1f}** no exame final.")
    else:
        st.error("### 🛑 Alerta! \nRendimento crítico. Procure a coordenação pedagógica para orientação.")

    # Tabela de Histórico (Simulada via Session State)
    with st.expander("📊 Simulações Salvas"):
        if 'historico' not in st.session_state:
            st.session_state.historico = []
            
        if st.button("Salvar Simulação"):
            st.session_state.historico.append({"N1": n1, "N2": n2, "Média": media})
            
        if st.session_state.historico:
            st.table(st.session_state.historico)

if __name__ == "__main__":
    main()
