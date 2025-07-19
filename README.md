# Auditor de Senhas Wi-Fi

Este script Python permite **auditar redes Wi-Fi salvas** e suas senhas em um computador Windows. Ele gera um relatório detalhado com os nomes das redes e suas respectivas senhas, salvando todas as informações em um arquivo JSON.

## ⚠️ Aviso Importante

Este script foi desenvolvido para **acessar apenas informações de redes Wi-Fi às quais seu computador já se conectou** e que possuem perfis salvos. Ele **não** tem a capacidade de "hackear" novas redes ou recuperar senhas de redes que você nunca acessou anteriormente. Utilize esta ferramenta de forma **responsável e ética**.

---

## Funcionalidades Principais

* **Lista de Redes Salvas:** O script identifica e lista todos os perfis de rede Wi-Fi que estão armazenados no seu sistema operacional Windows.
* **Recuperação de Senhas:** Para cada rede salva, ele tenta extrair a senha em texto claro. Caso a senha não esteja disponível ou esteja oculta pelo sistema, o script indicará "Não encontrada".
* **Geração de Relatório JSON:** Todas as informações coletadas (data da auditoria, nomes das redes e suas senhas) são compiladas em um relatório formatado em JSON para fácil visualização e armazenamento.
* **Fácil de Usar:** A execução do script é simples e direta, feita através da linha de comando.

---

## Requisitos

* **Sistema Operacional:** Windows
* **Linguagem:** Python 3.x

---

## Como Usar

Para começar a usar o Auditor de Senhas Wi-Fi, siga os passos abaixo:

1.  **Salve o Script:** Copie o código Python fornecido e salve-o em um arquivo com a extensão `.py` (por exemplo, `auditor_wifi.py`).
2.  **Abra o Terminal:** Abra o Prompt de Comando (CMD) ou o PowerShell no seu Windows.
3.  **Navegue até o Diretório:** No terminal, use o comando `cd` para ir até o diretório onde você salvou o arquivo `auditor_wifi.py`.
    ```bash
    cd C:\caminho\para\seu\script
    ```
4.  **Execute o Script:** Uma vez no diretório correto, execute o script com o Python:
    ```bash
    python auditor_wifi.py
    ```

    Após a execução, o script exibirá as redes encontradas e suas senhas diretamente no console.

5.  **Acesse o Relatório:** Um arquivo JSON será criado no mesmo diretório do script, com um nome similar a `wifi_report_20250719_183000.json` (a data e hora refletirão o momento da execução). Este arquivo contém o relatório completo das redes e senhas.

---

## Exemplo de Saída no Console

=== Auditoria de Redes Wi-Fi Salvas ===
AVISO: Este script só acessa redes às quais este computador já se conectou.

Redes encontradas:
Rede: MinhaCasaWiFi | Senha: MinhaSenhaSegura123
Rede: Cafeteria_Gratis | Senha: Não encontrada
Rede: WiFi_Biblioteca_Publica | Senha: SenhaConvidadoBiblioteca

Relatório salvo em: C:\Users\SeuUsuario\Documentos\wifi_report_20250719_183000.json
