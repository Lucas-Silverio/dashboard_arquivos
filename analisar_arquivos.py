from pathlib import Path
import os
import time

def coletar_dados_dir(pasta: str):
    arquivos = []
    for item in Path(pasta).rglob('*'):
        if item.is_file():
            try:
                stat = item.stat()
                arquivos.append({
                    'nome': item.name,
                    'caminho': str(item.resolve()),
                    'tamanho_MB': round(stat.st_size / (1024 * 1024), 2),
                    'criado_em': time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(stat.st_birthtime)),
                    'modificado_em': time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(stat.st_birthtime)),
                    'extensao': item.suffix.lower() if item.suffix else 'sem_extensao'
                })
            except Exception as e :
                print(f"Erro ao acessar {item}: {e}")
    return arquivos