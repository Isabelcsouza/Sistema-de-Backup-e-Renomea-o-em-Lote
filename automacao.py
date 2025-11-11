import os
import shutil

home_usuario = "C:\\Automacao_pastas"

pasta_original = "Arquivos"
caminhoPasta_original = os.path.join(home_usuario, pasta_original)

print('\nIniciando processo de cópia e renomeação...')
print(f'\nVerificando o caminho para {caminhoPasta_original}')

if not os.path.exists(caminhoPasta_original):
    print(f"ERRO: A pasta '{pasta_original}' não foi encontrada")
    exit()
else:
    print(f"A pasta '{pasta_original}' foi encontrada com sucesso!")

pasta_copia = "Arquivos_renomeados"
caminhoPasta_copia = os.path.join(home_usuario, pasta_copia)

print(f"\nCriando cópia da pasta '{pasta_original}'...\n")
if os.path.exists(caminhoPasta_copia):
    print(f"Pasta de cópia '{pasta_copia}' já existe. Removendo pasta existente...")
    shutil.rmtree(caminhoPasta_copia)

try:
    shutil.copytree(caminhoPasta_original, caminhoPasta_copia)
    print('\nCopia criada com sucesso!')
except Exception as e:
    print(f"Erro ao criar cópia da pasta: {e}")
    exit()

print('\nRenomeando arquivos na pasta cópia...\n')

arquivos_copia =[]
for item in os.listdir(caminhoPasta_copia):
    item_caminhoCompleto = os.path.join(caminhoPasta_copia, item)
    if os.path.isfile(item_caminhoCompleto):
        arquivos_copia.append(item)

arquivos_copia.sort()

cont_arquivosRenomeados = 0
for i, arquivoAntigo in enumerate(arquivos_copia):
    nome_base, extensao = os.path.splitext(arquivoAntigo)

    novo_arquivo = f"documentos_{i + 1:02d}{extensao}"

    caminho_arquivos_antigo = os.path.join(caminhoPasta_copia, arquivoAntigo)
    caminho_arquivos_novo = os.path.join(caminhoPasta_copia, novo_arquivo)

    try:
        os.rename(caminho_arquivos_antigo, caminho_arquivos_novo)
        print(f"Renomeado: {arquivoAntigo} -> {novo_arquivo}")
        cont_arquivosRenomeados += 1
    except Exception as e:
        print(f"Erro ao renomear arquivo '{arquivoAntigo}': {e}")

print('\nProcesso Concluído!')
print(f"Pasta original (intacta): '{caminhoPasta_original}'")
print(f"Pasta com arquivos renomeados: '{caminhoPasta_copia}'")
print(f"Total de arquivos: {cont_arquivosRenomeados}")