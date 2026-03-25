import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

# Instanciar o modelo ChatOpenAI
model = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.7)

# Criar o template de prompt com personalidade de GeoAI Mentor
prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        "Você é o 'GeoAI Mentor', um assistente especializado em ajudar geocientistas a migrar para a área de Ciência de Dados. Seja amigável e didático.",
    ),
    ("placeholder", "{historico}"),
    ("human", "{query}"),
])

# Parser para garantir saída como string
parser = StrOutputParser()

# Criar cadeia usando LangChain Expression Language (LCEL)
geoai_chain = prompt | model | parser

# Dicionário para armazenar histórico de sessões
memoria_sessoes = {}

# Função para obter histórico por sessão (padrão singleton)
def obter_historico_por_sessao(session_id: str) -> InMemoryChatMessageHistory:
    if session_id not in memoria_sessoes:
        memoria_sessoes[session_id] = InMemoryChatMessageHistory()
    return memoria_sessoes[session_id]

# Criar cadeia com memória
cadeia_com_memoria = RunnableWithMessageHistory(
    runnable=geoai_chain,
    get_session_history=obter_historico_por_sessao,
    input_messages_key="query",
    history_messages_key="historico",
)

# Lista com as perguntas
questions = [
    "Eu sou geofísico e quero migrar para a área de dados. Qual linguagem de programação devo aprender primeiro?",
    "E que tipo de projeto de portfólio eu poderia criar usando essa linguagem?",
]

# ID da sessão para esta conversa
session_id = "sessao_geofisico"

# Laço de repetição para enviar cada pergunta ao modelo com memória
for question in questions:
    response = cadeia_com_memoria.invoke(
        {"query": question},
        config={"configurable": {"session_id": session_id}}
    )
    print(f"Pergunta: {question}")
    print(f"Resposta: {response}")
    print()