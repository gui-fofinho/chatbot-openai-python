# 🤖 Chat IA com Python e Streamlit  

Este projeto consiste em um **Chat de Inteligência Artificial** desenvolvido em **Python**, utilizando a **API da OpenAI** e a biblioteca **Streamlit** para a interface web.

O projeto foi desenvolvido durante o **Curso da Hashtag Programação**, com foco em aprendizado prático de:
- consumo de APIs  
- criação de interfaces simples  
- gerenciamento de estado (histórico do chat)  

O **Streamlit** é responsável tanto pelo **front-end** quanto pelo **back-end**, tornando o projeto simples de rodar e entender.

---

## 🚀 Como funciona  

- O usuário digita uma mensagem na interface web  
- A mensagem é enviada para a **API da OpenAI**  
- A IA gera uma resposta  
- O histórico da conversa é mantido na tela durante a execução  

---

## 📌 Pré-requisitos  

Antes de rodar o projeto, você precisa ter instalado em sua máquina:

- **Python 3.10 ou superior**  
- **Conta na OpenAI** (para gerar a API Key)  

---

## 📦 Instalação das dependências  

No terminal, execute:

```bash
pip install openai streamlit
🔑 Configuração da API Key da OpenAI
Por segurança, a API Key NÃO fica no código.
Ela deve ser configurada como variável de ambiente.

▶️ Windows (Prompt de Comando ou PowerShell)
bash
Copiar código
setx OPENAI_API_KEY "sua-chave-aqui"
Após executar esse comando:

feche o terminal

abra novamente

▶️ Linux / macOS
bash
Copiar código
export OPENAI_API_KEY="sua-chave-aqui"
▶️ Como rodar o projeto
⚠️ IMPORTANTE:
Este projeto não deve ser executado com python arquivo.py.

Use obrigatoriamente o comando do Streamlit:

bash
Copiar código
streamlit run nome_do_arquivo.py
Exemplo:

bash
Copiar código
streamlit run app.py
Após isso:

o navegador será aberto automaticamente

o chat estará pronto para uso

🧠 Funcionalidades
Interface de chat interativa

Envio de mensagens para a IA

Respostas em tempo real

Histórico de mensagens mantido durante a sessão

Código simples e didático

📁 Estrutura do projeto (exemplo)
text
Copiar código
📦 Chat-IA-Streamlit
 ┣ 📄 app.py
 ┣ 📄 README.md
🛠 Tecnologias utilizadas
Python

Streamlit

OpenAI API

📚 Observações
Este projeto tem fins educacionais

Ideal para quem está aprendendo:

APIs

Streamlit

Integração com IA

Pode ser facilmente expandido com:

histórico salvo em arquivo

interface personalizada

novos modelos de IA

👨‍💻 Autor
Projeto desenvolvido por Guilherme Matté
Durante o Curso da Hashtag Programação
