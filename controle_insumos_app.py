
import streamlit as st
import json
import os

# Caminho do arquivo de dados
DATA_FILE = "consumo_insumos.json"

# Inicializa os dados se não existir
if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, "w") as f:
        json.dump({
            "21099-ET02: CORREIOS": 0,
            "21118-ET03: PEDIDOS": 0
        }, f)

# Carrega os dados atuais
with open(DATA_FILE, "r") as f:
    data = json.load(f)

# Título
st.title("📦 Controle de Consumo de Insumos")

st.subheader("Registre o uso com 1 clique!")

# Botões de uso
col1, col2 = st.columns(2)

with col1:
    if st.button("➕ 1x ET02 - CORREIOS"):
        data["21099-ET02: CORREIOS"] += 1
with col2:
    if st.button("➕ 1x ET03 - PEDIDOS"):
        data["21118-ET03: PEDIDOS"] += 1

# Mostrar totais
st.markdown("---")
st.metric("Total usado - 21099-ET02: CORREIOS", data["21099-ET02: CORREIOS"])
st.metric("Total usado - 21118-ET03: PEDIDOS", data["21118-ET03: PEDIDOS"])

# Confirmação para zerar os contadores
st.markdown("---")
with st.expander("🧹 Zerar (confirmação necessária)"):
    confirma = st.checkbox("Confirmar.")
    if st.button("Zerar agora"):
        if confirma:
            data = {
                "21099-ET02: CORREIOS": 0,
                "21118-ET03: PEDIDOS": 0
            }
            st.success("Contadores zerados!")
        else:
            st.warning("Você precisa marcar a confirmação antes de zerar.")

# Salvar os dados atualizados
with open(DATA_FILE, "w") as f:
    json.dump(data, f)
