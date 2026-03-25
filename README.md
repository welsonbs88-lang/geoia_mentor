GeoAI Mentor 🚀🧭
![Status](https://img.shields.io/badge/status-experimental-yellow) ![Python](https://img.shields.io/badge/python-3.8%2B-blue) ![License](https://img.shields.io/badge/license-MIT-green)

Chatbot inteligente com memória conversacional, construído com LangChain, para orientar profissionais de Geociências na transição para Ciência de Dados, Machine Learning e Inteligência Artificial.

Índice 📚
Visão Geral
Problema que Resolve
Solução
Principais Funcionalidades
Tecnologias
Pré-requisitos
Instalação e Configuração
Como Executar
Exemplos de Interação (antes / depois)
Arquitetura (visão geral)
Memória Conversacional e Sessões
Melhorias e Produção
Arquivos Importantes
Contribuição
Licença
Contato
Visão Geral 🧠
O GeoAI Mentor é um assistente virtual pensado para servir como mentor técnico e de carreira para profissionais de Geociências (ex.: Geofísica, Geologia). Ele fornece respostas didáticas, recomendações de projetos e orientações de transição de carreira, preservando o contexto das conversas por sessão.

Problema que Resolve ❗
Profissionais de geociências costumam ter:

Forte base em matemática, física e modelagem;
Dificuldade em escolher tecnologias, reaproveitar conhecimento e criar projetos relevantes para portfólio.
O GeoAI Mentor transforma esse conhecimento técnico em caminhos práticos para migrar à ciência de dados e IA.

Solução ✅
Respostas especializadas e contextualizadas;
Orientação personalizada por sessão;
Exemplos de projetos aplicados a dados geofísicos e espaciais;
Memória de conversas para continuidade e evolução das recomendações.
Principais Funcionalidades ✨
Memória de conversa por session_id;
Prompt templates para manter tom didático;
Pipeline com Prompt → LLM → Output Parser;
Simulações locais para demonstrar fluxo de uso.
Tecnologias 🧰
Camada	Ferramenta
Linguagem	Python 3.8+
Framework LLM	LangChain (LCEL)
Modelo	OpenAI (gpt-3.5-turbo)
Variáveis de ambiente	python-dotenv
Memória	InMemoryChatMessageHistory / RunnableWithMessageHistory
Pré-requisitos ⚙️
Python 3.8 ou superior
Conta OpenAI com API key
Git (opcional)
Instalação e Configuração 🛠️
Clone o repositório (opcional):
bash
git clone https://github.com/welsonbs88-lang/Geo-IA-Mentor.git
cd Geo-IA-Mentor
Crie e ative um ambiente virtual:
bash
python -m venv venv
# Linux / macOS
source venv/bin/activate
# Windows (PowerShell)
venv\Scripts\Activate.ps1
# Windows (cmd)
venv\Scripts\activate
Instale dependências:
bash
pip install -r requirements.txt
# se não houver requirements:
pip install langchain langchain-openai python-dotenv openai
Configure variáveis de ambiente: Crie um arquivo .env na raiz com:
Code
OPENAI_API_KEY=sua_chave_aqui
# Opcional: outras configs, ex:
# OPENAI_API_BASE=
# OTHER_CONFIG=valor
Observação: não commite o .env no repositório.

Como Executar ▶️
Execute o script principal de demonstração:

bash
python chatbot_mentor.py
O script realiza uma simulação de conversa com perguntas pré-definidas. Para usar interativamente ou integrar via API, adapte o ponto de entrada conforme a sua aplicação.

Parâmetros úteis (exemplos):

--session-id : id da sessão para simular histórico
--interactive : modo para inserir perguntas via terminal (se implementado)
Exemplos de Interação 💬
Antes (sem memória — respostas genéricas):

Pergunta: "Eu sou geofísico e quero migrar para a área de dados. Qual linguagem devo aprender?"
Resposta: "Você pode começar com Python."
Pergunta: "Que tipo de projeto posso criar?"
Resposta: "Você pode criar projetos de análise de dados."
Depois (com memória — contextualizado e progressivo):

Pergunta: "Eu sou geofísico e quero migrar para a área de dados. Qual linguagem devo aprender?"
Resposta: "Como geofísico, você já tem base em matemática e modelagem. Recomendo Python com foco em NumPy, Pandas, SciPy e visualização (Matplotlib/Seaborn)."
Pergunta: "Que tipo de projeto de portfólio posso criar usando essa linguagem?"
Resposta: "Sugerido: pipeline de pré-processamento e análise de dados sísmicos, extração de features e aplicação de modelos de detecção de anomalias; integração com GeoPandas para análise espacial."
Esses exemplos mostram como a memória permite respostas que consideram contexto prévio e entregam recomendações mais alinhadas ao histórico do usuário.

Arquitetura (visão geral) 🏗️
Fluxo lógico: Prompt Template → Modelo LLM → Output Parser → (memória) → saída

Exemplo do Prompt Template (LCEL):

py
ChatPromptTemplate.from_messages([
    ("system", "Você é o 'GeoAI Mentor' — um mentor didático e objetivo."),
    ("placeholder", "{historico}"),
    ("human", "{query}"),
])
Configuração do modelo:

py
ChatOpenAI(model="gpt-3.5-turbo", temperature=0.7)
Output parser:

py
StrOutputParser()
Memória Conversacional e Sessões 🧾
Implementação básica:

py
memoria_sessoes = {}

def obter_historico_por_sessao(session_id: str):
    return memoria_sessoes.get(session_id, InMemoryChatMessageHistory())
Uso com RunnableWithMessageHistory:

py
cadeia_com_memoria = RunnableWithMessageHistory(
    runnable=geoai_chain,
    get_session_history=obter_historico_por_sessao,
    input_messages_key="query",
    history_messages_key="historico",
)
Como funciona:

Cada conversa tem um session_id.
Ao receber uma query, o histórico da sessão é injetado no prompt.
A resposta é gerada e adicionada ao histórico para futuras interações.
Recomendações:

Para produção, troque InMemory por armazenamento persistente (Redis, banco de dados).
Defina políticas de retenção e anonimização para proteger dados sensíveis.
Melhorias e Produção 📈
Sugestões para evolução:

Persistir histórico em Redis/Postgres para escalabilidade.
Camada de autenticação e gerenciamento de sessões.
Monitoramento de custos do uso da API OpenAI.
Controle de versão dos prompts e testes automatizados de qualidade de respostas.
Integração com interfaces web (FastAPI/Streamlit) ou chat em tempo real.
Arquivos Importantes 📁
chatbot_mentor.py — script principal de execução/simulação
README.md — documentação do projeto
requirements.txt — dependências (se existir)
Módulos com a definição do pipeline LangChain (prompt, chain, memória)
Contribuição 🤝
Contribuições são bem-vindas:

Abra issues para bugs ou ideias;
Envie PRs com melhorias de código ou documentação;
Documente fluxos desejados (ex.: persistência, autenticação).
Fluxo sugerido:

Fork → criar branch com nome descritivo → commits claros → abrir PR.
Descreva mudanças e motivos no PR.
Licença 📝
Este projeto está sob licença MIT (ou ajuste conforme sua escolha). Atualize o cabeçalho conforme necessário.

Contato ✉️
Para dúvidas, sugestões ou parcerias: abra uma issue no repositório ou contate pelo perfil do GitHub.
