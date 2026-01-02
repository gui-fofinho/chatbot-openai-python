# Chat IA com Python e Streamlit

Um projeto de **Chat de Inteligência Artificial** desenvolvido em **Python**, utilizando a **API da OpenAI** e a biblioteca **Streamlit** para criar uma interface web interativa.

O projeto foi desenvolvido durante o **Curso da Hashtag Programação**, com foco em aprendizado prático de consumo de APIs, criação de interfaces e gerenciamento de estado. O **Streamlit** é responsável tanto pelo **front-end** quanto pelo **back-end**, tornando o projeto simples de rodar e entender.

---

## Tecnologias Utilizadas
![Python](https://img.shields.io/badge/Python-3.10+-blue?style=flat-square&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-Web-ff0000?style=flat-square&logo=streamlit)
![OpenAI](https://img.shields.io/badge/OpenAI_API-GPT-412991?style=flat-square&logo=openai)

---

## Como Funciona

O fluxo da aplicação é simples e direto:

1. O usuário digita uma mensagem na interface web
2. A mensagem é enviada para a **API da OpenAI**
3. A IA gera uma resposta
4. O histórico da conversa é mantido na tela durante a execução

---

## Pré-requisitos

Antes de rodar o projeto, você precisa ter instalado em sua máquina:

- Python 3.10 ou superior
- Conta na OpenAI (para gerar a API Key)

---

## Instalação das Dependências

No terminal, execute:

```bash
pip install openai streamlit
```
## Configuração da API Key da OpenAI

Por segurança, a API Key **NÃO fica no código**. Ela deve ser configurada como variável de ambiente.

### Windows (Prompt de Comando ou PowerShell)

1. Execute o comando:
```bash
setx OPENAI_API_KEY "sua-chave-aqui"
```
2. Após executar esse comando:
```txt
- Feche o terminal
- Abra novamente
```

### Linux / macOS

Execute o comando:
```bash
export OPENAI_API_KEY "sua-chave-aqui"
```

## Como Rodar o Projeto

**IMPORTANTE:**
Este projeto **não deve ser executado** com `python arquivo.py`.

Use obrigatoriamente o comando do Streamlit:

1. Execute o comando:
```bash 
streamlit run nome_do_arquivo.py
```
Exemplo:
```bash 
streamlit run app.py
```
2. Após isso:
```txt
- O navegador será aberto automaticamente
- O chat estará pronto para uso
```

## Funcionalidades

- Interface de chat interativa
- Envio de mensagens para a IA
- Respostas em tempo real
- Histórico de mensagens mantido durante a sessão
- Código simples e didático

## Estrutura do Projeto
```txt
📦 Chat-IA-Streamlit
 ┣ 📄 app.py
 ┣ 📄 README.md
 ```
 ## Observações

Este projeto tem fins **educacionais**.

**Ideal para quem está aprendendo:**

- Consumo de APIs
- Streamlit
- Integração com IA


**Pode ser facilmente expandido com:**

- Histórico salvo em arquivo
- Interface personalizada
- Novos modelos de IA

## Autor

Projeto desenvolvido por **Guilherme Matté**Durante o Curso da Hashtag Programação




