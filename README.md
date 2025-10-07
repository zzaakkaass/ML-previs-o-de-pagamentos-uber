🚗 Análise de Dados - Métodos de Pagamento Uber
📋 Sobre o Projeto
Este projeto faz parte da minha jornada de aprendizado em Python e Machine Learning, onde realizo uma análise exploratória inicial de uma base de dados real da Uber. O objetivo é entender os padrões de uso e preparar os dados para futuramente construir um modelo de previsão do método de pagamento.

🎯 Objetivos
Realizar análise exploratória dos dados da Uber

Entender a estrutura e qualidade do dataset

Identificar possíveis padrões nos métodos de pagamento

Preparar a base para futuros modelos de Machine Learning

📊 Dataset
O projeto utiliza um dataset real contendo informações sobre viagens da Uber, incluindo:

Dados de localização

Horários das viagens

Métodos de pagamento

Outras métricas relevantes

🛠️ Tecnologias Utilizadas
Python 3

Pandas - Para manipulação e análise de dados

Jupyter Notebook (opcional) - Para análise interativa

📁 Estrutura do Código
python
# Importação e carregamento dos dados
df = pd.read_csv("dados_uber.csv")

# Análise exploratória inicial
print(f"Dataset: {df.shape[0]:,} linhas e {df.shape[1]} colunas")
print(df.describe(include="all"))
print(df.info())
🔍 Funcionalidades Implementadas
✅ Carregamento e inspeção inicial do dataset

✅ Estatísticas descritivas completas

✅ Análise da estrutura de dados

✅ Identificação de valores nulos e tipos de dados

🚀 Próximos Passos
Limpeza e tratamento dos dados

Análise visual com Matplotlib/Seaborn

Feature engineering

Desenvolvimento do modelo de ML

Validação e ajustes do modelo

📈 Resultados Esperados
Ao final do projeto, pretendo ter um modelo capaz de prever com boa acurácia o método de pagamento que será utilizado em uma viagem da Uber, baseado em características como localização, horário e histórico.

💡 Aprendizados
Manipulação de dados com Pandas

Análise exploratória de dados

Preparação de dados para Machine Learning

Trabalho com datasets reais

📬 Contato
Isaque Carvalho Silva

LinkedIn: (https://www.linkedin.com/in/isaque-carvalho-silva-164554282/)

GitHub: (https://github.com/zzaakkaass/)
