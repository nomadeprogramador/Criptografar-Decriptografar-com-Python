from cryptography.fernet import Fernet
import os
import sys

#const
DIR_DEFAULT ='arquivos'
IGN_ARQ = [os.path.basename(__file__), 'key.key', 'enc.py', 'dec.py']
KEY_PATH='key.key'

def list_files(base_dir):
    all_files = []
    for entry in os.listdir(base_dir):
        full_path = os.path.abspath(os.path.join(base_dir, entry))
        if os.path.isdir(full_path):
            all_files += list_files(full_path)
        elif os.path.isfile(full_path) and entry is not IGN_ARQ:
            all_files.append(full_path)
    return all_files

def read_key(key_path):
    if not os.path.isfile(key_path):
        print(f'Chave de criptografia não encontrada {key_path}')
        sys.exit(1)
    with open (key_path,'rb') as key_file:
        key = key_file.read()
    return key

def decript_file(key,all_files):
    decripted_file = []
    for file in all_files:
        try:
            with open(file,'rb') as enc_file:
                content = enc_file.read()
            raw_content = Fernet(key).decrypt(content)
            with open(file,'wb') as dec_file:
                dec_file.write(raw_content)
            decripted_file.append(file)
        except Exception as e :
            print(f'{e}erro ao encriptografar')

    return decripted_file

def print_decripted_file(files:list):
    if decript_file:
        print(f' OS ARQUIVOS FORAM DECRIPTOGRAFADOs')
        for file in files:
            print(f'{file}')
    else:
        print('O arquivo não foi encriptografado')

def main():
    dir = sys.argv[1] if len(sys.argv)>1 else DIR_DEFAULT
    all_files=list_files(dir)
    key=read_key(KEY_PATH)
    decripted_files=decript_file(key,all_files)
    print_decripted_file(decripted_files)
if __name__ == '__main__':
    main()