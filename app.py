import streamlit as st

def calcular_media(n1: float, n2: float) -> float:
    """Calcula a média aritmética simples entre duas notas."""
    return (n1 + n2) / 2

def main():
    st.set_page_config(page_title="Calculadora IF", page_icon="🎓")
    st.title("📊 Calculadora de Médias Acadêmicas")
    
    col1, col2 = st.columns(2)
    
    with col1:
        nota1 = st.number_input("Nota do 1º Bimestre:", min_value=0.0, max_value=10.0, step=0.1)
    
    with col2:
        nota2 = st.number_input("Nota do 2º Bimestre:", min_value=0.0, max_value=10.0, step=0.1)

    if st.button("Processar Resultado"):
        try:
            media = calcular_media(nota1, nota2)
            
            if media >= 6.0:
                st.success(f"Média Final: **{media:.2f}** - Aluno Aprovado!")
            else:
                st.warning(f"Média Final: **{media:.2f}** - Aluno em Recuperação.")
                
        except Exception as e:
            st.error(f"Erro ao processar os dados: {e}")

if __name__ == "__main__":
    main()
