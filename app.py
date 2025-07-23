import streamlit as st
import pandas as pd
import pickle
import sklearn  


# Título do app
st.title('Telecom X2 – Previsão de Evasão de Clientes (Churn)')

# Instrução
st.write('Faça o upload do arquivo CSV com os dados tratados (com as mesmas colunas usadas no treino):')

# Upload do arquivo
uploaded_file = st.file_uploader("Escolha o arquivo CSV", type="csv")

# Se um arquivo for carregado
if uploaded_file is not None:
    try:
        # Ler o arquivo em um DataFrame
        df = pd.read_csv(uploaded_file)
        
        # Mostrar os primeiros registros para conferência
        st.write('Dados carregados:')
        st.dataframe(df.head())

        # Carregar modelo treinado
        st.write('Carregando modelo preditivo...')
        with open('modelo_logistico.pkl', 'rb') as file:
            modelo = pickle.load(file)

        # Colunas corretas usadas no treinamento
        colunas_features = ['Idoso', 'Meses_Com_Empresa', 'Cobranca_Mensal', 'Cobranca_Total',
                            'Genero_Male', 'Tem_Parceiro_Yes', 'Tem_Dependentes_Yes', 'Telefone_Fixo_Yes',
                            'Multiplas_Linhas_No phone service', 'Multiplas_Linhas_Yes',
                            'Tipo_Internet_Fiber optic', 'Tipo_Internet_No',
                            'Seguranca_Online_No internet service', 'Seguranca_Online_Yes',
                            'Backup_Online_No internet service', 'Backup_Online_Yes',
                            'Protecao_Dispositivo_No internet service', 'Protecao_Dispositivo_Yes',
                            'Suporte_Tecnico_No internet service', 'Suporte_Tecnico_Yes',
                            'Streaming_TV_No internet service', 'Streaming_TV_Yes',
                            'Streaming_Filmes_No internet service', 'Streaming_Filmes_Yes',
                            'Tipo_Contrato_One year', 'Tipo_Contrato_Two year',
                            'Fatura_Digital_Yes', 'Metodo_Pagamento_Credit card (automatic)',
                            'Metodo_Pagamento_Electronic check', 'Metodo_Pagamento_Mailed check']

        # Selecionar as features no DataFrame
        X_novos_dados = df[colunas_features]

        # Realizar previsões
        st.write('Gerando previsões de churn...')
        previsoes = modelo.predict(X_novos_dados)

        # Adicionar coluna de previsão no DataFrame
        df['Churn_Previsto'] = previsoes

        # Exibir resultados
        st.write('Resultados com previsão de churn:')
        st.dataframe(df[['Churn_Previsto']].head())
        

    except Exception as e:
        st.error(f"Ocorreu um erro ao carregar o modelo ou realizar previsões: {e}")

else:
    st.warning('Por favor, faça upload de um arquivo CSV para iniciar.')
