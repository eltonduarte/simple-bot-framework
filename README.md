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
"""

# Importação dos módulos 
from reusable_code import make_browser, log_to_file, taskkill, wait_for_conditions, config                            
from pathlib import Path

# Construir caminhos dentro do projeto da seguinte forma: base_dir / 'subdir'.
base_dir = Path(__file__).resolve().parent
dict_path = config.path_project(base_dir)

try:
    # STEP: Mata os processos pré-processamento
    taskkill.process('chrome.exe', 'excel.exe', 'saplogon.exe')

    # STEP: Início da sessão com o navegador
    bot_web = make_browser.chrome()
    log_to_file.info("Sessão com o webdriver criada com sucesso", f"{dict_path['file_log']}")

    # STEP: Abre o endereço desejado
    bot_web.get("https://google.com.br")
    log_to_file.info('Página acessada com sucesso', f"{dict_path['file_log']}")

    # STEP: Verifica se a janela existe
    if not wait_for_conditions.window_exists(bot = bot_web, title = "Google"): 
        raise Exception('Janela [Google] não existe')

    # STEP: Inserir a descrição da ação...
    log_to_file.info("Inserir descrição do log...", f"{dict_path['file_log']}")

    
except Exception as error_message:
    log_to_file.error(f'{error_message}', 'log.txt')
    

finally:
    # STEP: Mata os processos pós-processamento
    taskkill.process('chrome.exe', 'excel.exe', 'saplogon.exe')

    # STEP: Fecha a sessão com o navegador
    bot_web.close()
    log_to_file.error('Fim do processamento', 'log.txt')
