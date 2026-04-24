import streamlit as st

# Configuração da Página
st.set_page_config(
    page_title="Portal do Aluno - IF",
    page_icon="🎓",
    layout="centered"
)

def calcular_media(n1: float, n2: float) -> float:
    return (n1 + n2) / 2

def main():
    # Estilização Customizada via CSS (Opcional para dar um toque "IF")
    st.markdown("""
        <style>
        .main {
            background-color: #f5f7f9;
        }
        .stButton>button {
            width: 100%;
            border-radius: 5px;
            height: 3em;
            background-color: #2e7d32;
            color: white;
        }
        </style>
    """, unsafe_allow_html=True)

    # Sidebar com Informações Adicionais
    with st.sidebar:
        st.header("Configurações")
        st.info("O cálculo segue as normas institucionais de média aritmética simples.")
        st.divider()
        st.write("**Critério de Aprovação:**")
        st.write("- Média ≥ 6.0: **Aprovado**")
        st.write("- Média < 6.0: **Recuperação**")

    # Cabeçalho Principal
    st.title("🎓 Sistema de Gestão de Notas")
    st.subheader("Cálculo de Rendimento Acadêmico")
    st.markdown("---")

    # Card de Entrada de Dados
    with st.container():
        st.write("### 📝 Insira as Notas")
        col1, col2 = st.columns(2)
        
        with col1:
            nota1 = st.number_input("1º Bimestre", min_value=0.0, max_value=10.0, value=0.0, step=0.1, help="Insira a nota do primeiro período.")
        
        with col2:
            nota2 = st.number_input("2º Bimestre", min_value=0.0, max_value=10.0, value=0.0, step=0.1, help="Insira a nota do segundo período.")

    st.write("") # Espaçamento
    
    if st.button("📊 Analisar Desempenho"):
        media = calcular_media(nota1, nota2)
        
        # Área de Resultado
        st.markdown("### 🎯 Resultado Final")
        
        # Uso de st.metric para destaque visual
        res_col1, res_col2 = st.columns([1, 2])
        
        with res_col1:
            st.metric(label="Média Final", value=f"{media:.1f}", delta=f"{media - 6.0:.1f}" if media >= 6.0 else f"{media - 6.0:.1f}")
        
        with res_col2:
            if media >= 6.0:
                st.balloons()
                st.success(f"**PARABÉNS!** O aluno atingiu os requisitos e está **APROVADO**.")
            elif media >= 4.0:
                st.warning(f"**RECUPERAÇÃO.** O aluno ainda tem chance de aprovação via exame final.")
            else:
                st.error(f"**REPROVADO.** O rendimento está abaixo do mínimo exigido.")

        # Expander com detalhes técnicos
        with st.expander("Ver detalhes do cálculo"):
            st.write(f"Cálculo realizado: ({nota1} + {nota2}) / 2 = {media}")
            st.progress(media / 10)

if __name__ == "__main__":
    main()
