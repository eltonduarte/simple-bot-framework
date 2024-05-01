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