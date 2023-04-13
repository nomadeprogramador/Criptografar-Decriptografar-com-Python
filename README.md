# Criptografia
Um algoritmo capaz de criptografar e decriptografar utilizando python
Sobre o idioma: Fiz um mix de portugues e ingles no código algo que não é recomendável, contudo fiz isso apenas para ficar mais didático para o público brasileiro !

Como utilizar para criptografar  :
Para usar este script, você precisa ter o módulo "cryptography" instalado. Você pode instalá-lo usando o pip, digitando o seguinte comando no terminal:

pip install cryptography
Depois de instalar o módulo "cryptography", você pode executar o script digitando o seguinte comando no terminal:

python enc.py caminho_do_diretorio
Onde "enc.py" é o nome do arquivo Python que contém o script acima, e "caminho_do_diretório" é o caminho para o diretório que contém os arquivos que você deseja criptografar. Se você não especificar o caminho do diretório, ele usará o diretório padrão "arquivos".

O script então criará uma chave aleatória, salvará a chave em um arquivo "key.key" e usará essa chave para criptografar todos os arquivos no diretório especificado. Os arquivos criptografados serão sobrescritos com seus equivalentes criptografados.


Decriptografar:
python dec.py caminho_do_diretório
Onde "dec.py" é o nome do arquivo Python que contém o script acima, e "caminho_do_diretório" é o caminho para o diretório que contém os arquivos que você deseja descriptografar. Se você não especificar o caminho do diretório, ele usará o diretório padrão "arquivos".

O script primeiro verifica se o arquivo "key.key" está presente no diretório atual. Se a chave de criptografia não for encontrada, o script encerrará com um erro.

Em seguida, ele lista todos os arquivos no diretório especificado (exceto os arquivos de chave e os arquivos de script) e tenta descriptografá-los usando a chave de criptografia. Se a descriptografia for bem-sucedida, ele salvará o arquivo descriptografado com o mesmo nome e sobrescreverá o arquivo criptografado.




