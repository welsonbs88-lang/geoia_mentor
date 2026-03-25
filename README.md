GeoAI Mentor

Chatbot inteligente com memória conversacional, desenvolvido com LangChain, para orientar geocientistas na transição para Ciência de Dados e Inteligência Artificial.


Sobre o Projeto

O GeoAI Mentor é um assistente virtual especializado que atua como mentor de carreira para profissionais de Geociências, como Geofísica e Geologia.


Problema

Profissionais de Geociências geralmente possuem forte base em:

Matemática
Física
Modelagem

Porém, enfrentam dificuldades ao migrar para:

Ciência de Dados
Machine Learning
Inteligência Artificial


Principais desafios:

Escolher a linguagem de programação ideal
Entender como reaproveitar conhecimentos técnicos
Criar projetos relevantes para portfólio


Solução

O GeoAI Mentor oferece:

Respostas especializadas e didáticas
Orientação personalizada
Continuidade de contexto (memória de conversa)

Diferencial: o chatbot lembra interações anteriores, entregando respostas mais inteligentes e conectadas — como um mentor real.


Tecnologias Utilizadas

Python
LangChain
OpenAI (GPT-3.5 Turbo)
dotenv


Configuração do Ambiente


1. Crie um ambiente virtual

python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows


2. Instale as dependências

pip install langchain langchain-openai python-dotenv


3. Configure as variáveis de ambiente

Crie um arquivo .env na raiz do projeto:

OPENAI_API_KEY=sua_chave_aqui


Como Executar

Execute o script principal:

python chatbot_mentor.py

O programa irá simular uma conversa automaticamente utilizando uma lista de perguntas pré-definidas.


Exemplos de Interação

Antes (sem memória)
Pergunta: Eu sou geofísico e quero migrar para a área de dados. Qual linguagem devo aprender?
Resposta: Você pode começar com Python.

Pergunta: E que tipo de projeto posso criar?
Resposta: Você pode criar projetos de análise de dados.

Respostas genéricas e desconectadas.


Depois (com memória usando RunnableWithMessageHistory)
Pergunta: Eu sou geofísico e quero migrar para a área de dados. Qual linguagem devo aprender?
Resposta: Como geofísico, você já tem uma base forte em matemática e modelagem. Recomendo começar com Python...

Pergunta: E que tipo de projeto de portfólio eu poderia criar usando essa linguagem?
Resposta: Considerando sua experiência em Geofísica, você pode criar projetos envolvendo análise de dados sísmicos, modelagem geológica ou interpretação de dados espaciais...

O chatbot mantém contexto e personaliza a resposta.


Arquitetura do Projeto

O projeto foi construído utilizando LangChain Expression Language (LCEL), seguindo uma arquitetura em pipeline:


Prompt Template → Modelo LLM → Output Parser

1. Prompt Template

ChatPromptTemplate.from_messages([
    ("system", "Você é o 'GeoAI Mentor'..."),
    ("placeholder", "{historico}"),
    ("human", "{query}"),
])

Responsável por:

Definir a personalidade do chatbot
Inserir o histórico da conversa
Receber a entrada do usuário


2. Modelo LLM

ChatOpenAI(model="gpt-3.5-turbo", temperature=0.7)

Responsável por:

Gerar respostas inteligentes
Manter tom amigável e didático


3. Output Parser

StrOutputParser()

Responsável por:

Garantir que a saída seja uma string limpa


Memória Conversacional (Diferencial)

A memória é implementada com:

RunnableWithMessageHistory

cadeia_com_memoria = RunnableWithMessageHistory(
    runnable=geoai_chain,
    get_session_history=obter_historico_por_sessao,
    input_messages_key="query",
    history_messages_key="historico",
)


Como funciona

Cada conversa possui um session_id
O histórico é armazenado em memória (InMemoryChatMessageHistory)
O chatbot utiliza esse histórico para responder de forma contextual


Gerenciamento de Sessões

memoria_sessoes = {}

def obter_historico_por_sessao(session_id: str):

Implementação simples e eficiente para simular múltiplos usuários.


Fluxo de Execução

Carrega variáveis de ambiente
Inicializa o modelo LLM
Cria o prompt com contexto
Monta a cadeia (prompt | model | parser)
Adiciona memória com RunnableWithMessageHistory
Executa perguntas simuladas
Exibe respostas no terminal
