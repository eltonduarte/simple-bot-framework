# Framework simples para automações web

## Como utilizar?

### Passo 1: Instalar os módulos reutilizáveis 

Você precisará extrair a pasta "reusable-code" no diretório de instalação do python ou do ambiente virtual
```
C:\Users\<username>\AppData\Local\Programs\Python\Python312\Lib\
```

Até o momento temos os seguintes módulos:

```python
config # configurações iniciais do processo
open_program_file # abre algum executável  
make_browser, # cria a sessão com o browser
log_to_file, # cria o log de execução do processo
taskkill, # mata os processos
wait_for_conditions, # validações em janelas e objetos
```


### Passo 2: Instalar as dependências
Você também precisará ter as bibliotecas instaladas no seu computador  

Execute os comandos abaixo:

```
pip install -r requirements.txt
```

### Passo 3: Template

Use o arquivo "template.py" para iniciar a automação:

```python
""" Template Para Automações Web
    Data criação: 30/04/2024
    Ultima atualização: 
"""

# Importação dos módulos 
from reusable_code import make_browser, log_to_file, taskkill, wait_for_conditions, config                            
from pathlib import Path
from time import sleep

# Variáveis globais
base_dir = Path(__file__).resolve().parent
base_config = config.config_inicial(base_dir)

try:
    # Mata os processos pré-processamento
    taskkill.process("chrome.exe", "excel.exe", "saplogon.exe")
    log_to_file.info(f"Pré-processamento realizado com sucesso", f"{base_config['arquivo_log']}")
    sleep(1)

    # Início da sessão com o navegador
    bot_web = make_browser.chrome()
    log_to_file.info(f"Sessão com o webdriver criada com sucesso", f"{base_config['arquivo_log']}")
    sleep(1)
    
    # Abre o endereço desejado
    bot_web.get(f"{base_config['endereco_site']}")
    log_to_file.info("Página acessada com sucesso", f"{base_config['arquivo_log']}")
    sleep(1)

    # Verifica se a janela existe
    if not wait_for_conditions.window_exists(bot=bot_web, title="Google"): 
        raise Exception("Janela [Google] não existe")
    sleep(1)

    # Inserir a descrição da ação...
    log_to_file.info("Inserir descrição do log...", f"{base_config['arquivo_log']}")
    sleep(1)
    
except Exception as error_message:
    log_to_file.error(f'{error_message}', f"{base_config['arquivo_log']}")

finally:    
    # Fecha a sessão com o navegador
    bot_web.close()
    log_to_file.error("Fim do processamento", f"{base_config['arquivo_log']}")