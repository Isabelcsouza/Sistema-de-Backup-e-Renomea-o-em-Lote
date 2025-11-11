🤖 Prática de Automação com Python: Backup e Renomeação em Lote
Este repositório contém um script Python desenvolvido como uma solução prática para automação de tarefas do sistema de arquivos.

🎯 Objetivo do Programa
O objetivo é desenvolver um script em Python que automatiza duas tarefas críticas de organização: realizar uma cópia de segurança de uma pasta de documentos e, em seguida, renomear todos os arquivos na cópia de forma padronizada e sequencial.

✨ Funcionalidades Principais
O script executa as seguintes operações:


Verificação de Existência: Antes de tudo, verifica se a pasta de origem (Arquivos) realmente existe no local esperado.


Cópia de Segurança: Cria uma cópia completa da pasta original com o nome Arquivos_renomeados.


Limpeza Automática: Se a pasta de backup (Arquivos_renomeados) já existir de uma execução anterior, ela é totalmente removida antes da nova cópia, garantindo um backup limpo.


Renomeação em Lote: Percorre a pasta copiada e renomeia cada arquivo para o formato documentos_XX.extensao.


Preservação da Extensão: O processo de renomeação mantém a extensão original de cada arquivo (ex: .txt, .pdf, .jpg).


Numeração Padronizada: Utiliza numeração sequencial com dois dígitos (ex: 01, 02, 03...) para manter a ordem correta.


Relatório no Console: Exibe mensagens claras no console informando cada etapa do processo, desde a verificação até a conclusão.

📂 Estrutura de Pastas
O script opera sob uma estrutura de pastas pré-definida.

Antes da Execução
O script espera encontrar a pasta Arquivos dentro de C:\Automacao_pastas.

C:\Automacao_pastas
└─── Arquivos
        ├─── relatorio.txt
        ├─── tarefa.txt
        ├─── planilha.txt
        ├─── notas.txt
        ├─── dados.txt
        └─── contrato.txt
Após a Execução
A pasta original permanece intacta. Uma nova pasta Arquivos_renomeados é criada no mesmo nível, contendo os arquivos renomeados.

C:\Automacao_pastas
├─── Arquivos (Intacta)
│       ├─── relatorio.txt
│       ├─── tarefa.txt
│       │   ...
│
└─── Arquivos_renomeados
        ├─── documentos_01.txt
        ├─── documentos_02.txt
        ├─── documentos_03.txt
        ├─── documentos_04.txt
        ├─── documentos_05.txt
        └─── documentos_06.txt
(Nota: A ordem da numeração depende da ordenação alfabética dos nomes originais, conforme implementado no script.)

🚀 Como Usar
Clone este repositório:

Bash

git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio

Configure o Ambiente:

Este script está configurado para rodar em um caminho fixo (C:\Automacao_pastas). Certifique-se de criar esta pasta.

Dentro de C:\Automacao_pastas, crie a pasta de origem chamada Arquivos.

Adicione alguns arquivos de teste (ex: teste1.txt, foto.jpg, doc.pdf) dentro de C:\Automacao_pastas\Arquivos.

Execute o Script: Abra seu terminal ou prompt de comando e execute o arquivo Python:

Bash

python nome_do_seu_script.py
Verifique o Resultado: A pasta C:\Automacao_pastas\Arquivos_renomeados será criada (ou recriada) com todos os seus arquivos devidamente renomeados.

🖥️ Exemplo de Saída no Console
A execução do script produzirá um relatório detalhado no console similar ao abaixo:

Iniciando processo de cópia e renomeação...

Verificando o caminho para C:\Automacao_pastas\Arquivos
A pasta 'Arquivos' foi encontrada com sucesso!

Criando cópia da pasta 'Arquivos'...

Pasta de cópia 'Arquivos_renomeados' já existe. Removendo pasta existente...

Copia criada com sucesso!

Renomeando arquivos na pasta cópia...

Renomeado: contrato.txt -> documentos_01.txt
Renomeado: dados.txt -> documentos_02.txt
Renomeado: notas.txt -> documentos_03.txt
Renomeado: planilha.txt -> documentos_04.txt
Renomeado: relatorio.txt -> documentos_05.txt
Renomeado: tarefa.txt -> documentos_06.txt

Processo Concluído!
Pasta original (intacta): 'C:\Automacao_pastas\Arquivos'
Pasta com arquivos renomeados: 'C:\Automacao_pastas\Arquivos_renomeados'
Total de arquivos: 6

📚 Conceitos Praticados
Este projeto aplica diversos conceitos fundamentais de Python para automação e manipulação do sistema de arquivos:


Bibliotecas Nativas: Uso dos módulos os (para manipulação de caminhos, nomes, listagem e renomeação) e shutil (para operações de alto nível como copiar e remover árvores de diretórios).


Manipulação de Caminhos: Uso de os.path.join para criar caminhos de forma segura e os.path.exists para validação.


Operações de Diretório: shutil.copytree para cópia recursiva e shutil.rmtree para remoção recursiva.


Parsing de Nomes de Arquivos: os.path.splitext para separar de forma confiável o nome do arquivo de sua extensão.


Iteração e Enumeração: Uso de os.listdir para iterar sobre os arquivos e enumerate para gerar contadores sequenciais.

Tratamento de Exceções: Uso de try...except para capturar erros durante as operações de cópia e renomeação.
