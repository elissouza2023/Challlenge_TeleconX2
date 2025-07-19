<h1 align="center">📊 Jupyter Telecom X2: Previsão de Evasão de Clientes (Churn)</h1>

<div align="center">
  <img src="img1.jpg" alt="Visão geral do projeto Telecom X" width="600"/>
</div>

🎯 Visão Geral
Bem-vindo(a) ao repositório do Projeto Telecom X2, parte do desafio de Data Science do Programa ORACLE ONE – Alura (Turma G8). Este projeto tem como objetivo analisar a evasão de clientes (churn) e construir modelos preditivos eficazes para apoiar a Telecom X, uma empresa de telecomunicações, na redução de sua alta taxa de cancelamentos.

✨ Objetivo desta Etapa
Nesta fase, focamos em:

<p>✅ Preparação dos dados para Machine Learning</p>
<p>✅ Criação, avaliação e interpretação de modelos preditivos de churn</p>

<p>🔍 Fluxo de Trabalho</p>
<p>✔️ 1. Extração dos dados tratados</p>
Importação dos arquivos já tratados na fase de ETL para iniciar a modelagem preditiva.

<p>✔️ 2. Análise de correlação e seleção de variáveis</p>
Identificação das variáveis com maior impacto no cancelamento de clientes.

<p>✔️ 3. Preparação para modelagem</p>
Transformação de variáveis categóricas em dummies (OneHotEncoder), tratamento de valores ausentes e exclusão de colunas não preditivas, como IDs.

<p>✔️ 4. Split dos dados</p>
Divisão dos dados em treino (70%) e teste (30%) para garantir reprodutibilidade e avaliação justa dos modelos.

<p>✔️ 5. Criação dos modelos preditivos</p>
Foram criados dois modelos principais:

Regressão Logística: Utilizada como baseline, com alta interpretabilidade e bom desempenho em problemas de classificação binária.

Random Forest: Escolhido por sua robustez, capacidade de lidar com dados não linearmente separáveis e fornecimento de insights sobre a importância das variáveis.

<p>✔️ 6. Avaliação dos modelos</p>
Métricas utilizadas: accuracy, precision, recall, f1-score e ROC-AUC, garantindo análise completa da performance preditiva.

<p>✔️ 7. Interpretação e conclusões</p>
Foram extraídos insights estratégicos sobre os fatores que mais influenciam o churn, além de recomendações práticas para o negócio.

<p>📝 Resumo das Conclusões</p>
<p>🔹 Cobrança Total: Clientes com maior cobrança total (planos completos/pacotes agregados) têm menor taxa de cancelamento.</p>
<p>🔹 Meses com a Empresa: Clientes com mais tempo de relacionamento apresentam menor churn, reforçando a importância de estratégias de fidelização.</p>
<p> 🔹 Tipo de Contrato: Clientes com contrato mensal têm maior probabilidade de cancelar, enquanto contratos anuais ou bianuais demonstram retenção superior.</p>

<p>💡 Gráficos para suporte às conclusões</p>
<p>Foram gerados gráficos de barras e linhas para demonstrar visualmente o impacto destas variáveis:

Cancelamento por tipo de contrato

Cancelamento por meses com a empresa

Cancelamento por faixa de cobrança total

<p>🛠️ Tecnologias Utilizadas</p>
<p>✅ Python</p>
<p>✅ Pandas: Manipulação e análise de dados</p>
<p>✅ Seaborn & Matplotlib: Visualizações estatísticas e personalizadas</p>
<p>✅ Scikit-learn: Construção, avaliação e interpretação dos modelos de Machine Learning</p>

<p>📌 Conclusão</p>

<p>Este projeto aplicou com sucesso as técnicas de preparação de dados, modelagem e análise preditiva, consolidando conhecimentos fundamentais da especialização em Data Science no Programa Oracle ONE.</p>

