<h1 align="center">📊 Telecom X2 – Previsão de Evasão de Clientes (Churn)</h1> <div align="center"> <img src="img1.jpg" alt="Visão geral do projeto Telecom X" width="600"/> </div> <p align="center"> <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white"/> <img src="https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white"/> <img src="https://img.shields.io/badge/Scikit--Learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white"/> <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white"/> </p>
🎯 Visão Geral

Bem-vindo(a) ao repositório do Projeto Telecom X2, parte do desafio de Data Science do Programa ORACLE ONE – Alura (Turma G8).

Este projeto tem como objetivo analisar a evasão de clientes (churn) e construir modelos preditivos eficazes para apoiar a Telecom X na redução de sua alta taxa de cancelamentos.

✨ Objetivos desta Etapa

✅ Preparação avançada dos dados para Machine Learning
✅ Criação, avaliação, comparação e interpretação de modelos preditivos de churn
✅ Construção de aplicação web com Streamlit para deploy do modelo

🔍 Fluxo de Trabalho

Etapa	Descrição
1. Extração dos dados tratados	Importação dos arquivos já tratados na fase de ETL.
2. Análise de correlação e seleção de variáveis	Heatmap e seleção de variáveis mais impactantes no churn.
3. Preparação para modelagem	OneHotEncoder, tratamento de valores ausentes e exclusão de colunas não preditivas.
4. Split dos dados	Divisão treino (70%) e teste (30%) garantindo reprodutibilidade.
5. Modelagem preditiva	Regressão Logística como baseline + Random Forest para robustez.
6. Avaliação e comparação de modelos	Accuracy, Precision, Recall, F1-score e ROC-AUC.
7. Interpretação (Feature Importances)	Identificação das variáveis que mais influenciam o churn.
8. Visualizações de suporte	Gráficos de barras e linhas para interpretação clara dos insights.
9. Deploy com Streamlit	App para upload de novos dados e geração de previsões em tempo real.

📈 Resultados

🔬 Comparativo de Modelos
Modelo	Accuracy	Precision	Recall	F1-Score	ROC-AUC
Regressão Logística	Melhor desempenho	Superior ao RF	Alta	Alta	Excelente
Random Forest	Bom	Médio	Médio	Médio	Bom

✅ Conclusão: A Regressão Logística apresentou desempenho superior e interpretabilidade mais clara para o negócio.

🔎 Principais Insights

Cobrança Total: Clientes com maior cobrança total (planos completos/pacotes agregados) têm menor taxa de cancelamento.

Meses com a Empresa: Clientes com mais tempo de relacionamento apresentam menor churn, evidenciando a importância de estratégias de fidelização.

Tipo de Contrato: Contratos mensais têm maior churn; contratos anuais/bianuais demonstram maior retenção.

📊 Visualizações Criadas

✔️ Cancelamento por tipo de contrato
✔️ Cancelamento por meses com a empresa
✔️ Cancelamento por faixa de cobrança total

🛠️ Tecnologias Utilizadas

Python

Pandas – Manipulação e análise de dados

Seaborn &
Matplotlib – Visualizações estatísticas

Scikit-learn – Construção, avaliação e interpretação dos modelos

Streamlit – Deploy do modelo como aplicação web

🚀 Deploy do Modelo

✔️ Exportação como pickle (.pkl)
✔️ Criação de app interativo com Streamlit
✔️ Preparação para futuros deploys no Vercel e integração com PostgreSQL para ingestão de novos clientes

📌 Conclusão

Este projeto aplicou com sucesso:

✅ Preparação e limpeza avançada de dados
✅ Modelagem preditiva e comparação de algoritmos
✅ Interpretação estratégica para o negócio
✅ Deploy de modelo como aplicação web

Consolidando conhecimentos fundamentais de Data Science no Programa Oracle ONE – Alura.

