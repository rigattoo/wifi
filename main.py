
import subprocess
import re
import json
from datetime import datetime
import os

def obter_redes_salvas_windows():
    """Obtém a lista de redes Wi-Fi salvas no Windows"""
    try:
        resultado = subprocess.run(['netsh', 'wlan', 'show', 'profiles'], 
                                 capture_output=True, text=True, check=True)
        redes = re.findall(r":\s(.*)", resultado.stdout)
        return [rede.strip() for rede in redes if rede.strip()]
    except Exception as e:
        print(f"Erro ao obter redes: {str(e)}")
        return []

def obter_senha_windows(nome_rede):
    """Obtém a senha de uma rede Wi-Fi específica no Windows"""
    try:
        resultado = subprocess.run(['netsh', 'wlan', 'show', 'profile', 
                                 nome_rede, 'key=clear'], 
                                 capture_output=True, text=True, check=True)
        senha_match = re.search(r"Conte.do da Chave\s*:\s(.*)", resultado.stdout)
        return senha_match.group(1).strip() if senha_match else "Não encontrada"
    except Exception as e:
        print(f"Erro ao obter senha para {nome_rede}: {str(e)}")
        return "Erro"

def gerar_relatorio():
    """Gera um relatório das redes Wi-Fi e senhas salvas"""
    redes = obter_redes_salvas_windows()
    relatorio = {
        "data": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "redes": []
    }

    for rede in redes:
        relatorio["redes"].append({
            "nome": rede,
            "senha": obter_senha_windows(rede)
        })

    return relatorio

def salvar_relatorio(relatorio):
    """Salva o relatório em um arquivo JSON"""
    nome_arquivo = f"wifi_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    with open(nome_arquivo, 'w') as f:
        json.dump(relatorio, f, indent=2)
    return nome_arquivo

if __name__ == "__main__":
    print("=== Auditoria de Redes Wi-Fi Salvas ===")
    print("AVISO: Este script só acessa redes às quais este computador já se conectou.\n")
    
    relatorio = gerar_relatorio()
    
    print("\nRedes encontradas:")
    for rede in relatorio["redes"]:
        print(f"Rede: {rede['nome']} | Senha: {rede['senha']}")
    
    arquivo = salvar_relatorio(relatorio)
    print(f"\nRelatório salvo em: {os.path.abspath(arquivo)}")