# Monitor Baba-DOU

![Python](https://img.shields.io/badge/Python-00B8B5?style=for-the-badge&logo=python&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/GitHub%20Actions-922CF7?style=for-the-badge&logo=github-actions&logoColor=white)
![Por Emily Matias](https://img.shields.io/badge/Por-Emily%20Matias-FF69B4?style=for-the-badge)

Script automatizado para monitorar o Diário Oficial da União (DOU) de forma agendada, diariamente. Um ba-ba-DOU!

## Objetivo
Facilitar o **monitoramento** do DOU, substituindo a busca manual e repetitiva por uma automação com notificação.

## Como funciona?

`tl;dr`: O script consulta o DOU todo dia às **18h**, buscando o **nome exato** do usuário. Caso o encontre, dispara um **alerta** por e-mail.

1.  **Agendamento**: O GitHub Actions aciona o script todos os dias às **18h (horário de Brasília)**, equivalente às 21h UTC do GitHub.
2.  **Busca**: O script gera a URL de consulta com base na variável de ambiente pré-configurada, escapando caracteres especiais e inserindo aspas para busca exata do nome inserido pelo usuário.
3.  **Validação**: O sistema verifica se a página retornou resultados válidos ou a mensagem padrão de "não encontrado".
4.  **Alerta**: Caso o nome conste no DOU, um e-mail é disparado para notificar o usuário, contendo o link com a query de busca para acesso direto.

## ⚙️ Configuração
Para tudo isso acontecer, foram necessários:
- Um repositório do GitHub (com os Secrets abaixo configurados)
- Um e-mail de destino (de qualquer provedor)
- E um Gmail <s>além de torcer para ser aprovada em concursos</s>

> [!WARNING]
> ***Evite expor dados sensíveis no código***. Adicione os **Secrets** a seguir ao seu repositório do GitHub pela sua segurança, em `Settings > Secrets and variables > Actions`:

| Secret | Descrição do valor |
| :----- | :----------------- |
| `NOME_BUSCA` | O **nome completo** que será usado para a consulta. Ex: Fulano Beltrano da Silva |
| `EMAIL_USER` | Gmail que **enviará** a notificação. |
| `EMAIL_PASS` | **Senha de App** de 16 dígitos gerada na [Conta Google](https://myaccount.google.com/apppasswords), para login do Gmail de envio. |
| `EMAIL_DESTINO` | E-mail que **receberá** os alertas. |

## 🛠️ Tecnologias
* **Python 3.11**: Lógica principal e construção dinâmica de queries.
* **GitHub**: Repositório que permite armazenar e executar lógica e automação.
* **GitHub Actions**: Automação programada (Cron Job) executada diariamente.
* **Requests**: Biblioteca que realiza as requisições HTTP simulando um navegador real.
* **SMTP/Gmail**: Protocolo para envio das notificações de alerta.

---
> [!NOTE]
> Este projeto utiliza o ambiente **Node.js 24** no GitHub Actions para garantir compatibilidade com as diretrizes de 2026.
