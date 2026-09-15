import os
import pyaes

def decrypt_file(file_name, key):
    """Descriptografa um arquivo específico usando AES-CTR."""
    try:
        # 1. Abrir e ler o arquivo criptografado
        with open(file_name, "rb") as file:
            file_data = file.read()

        # 2. Configurar a descriptografia AES
        aes = pyaes.AESModeOfOperationCTR(key)
        decrypt_data = aes.decrypt(file_data)

        # 3. Restaurar o nome original removendo a extensão '.ransomwaretroll'
        original_file_name = file_name[:-16]  # Remove os últimos 18 caracteres correspondentes à extensão
        
        with open(original_file_name, "wb") as new_file:
            new_file.write(decrypt_data)

        # 4. Remover o arquivo criptografado
        os.remove(file_name)
        print(f"[+] Arquivo descriptografado com sucesso: {file_name} -> {original_file_name}")

    except Exception as e:
        print(f"[-] Erro ao processar o arquivo {file_name}: {e}")

def main():
    # Mesma chave utilizada na criptografia
    key = b"testeransomwares"
    
    # Extensão alvo que indica que o arquivo está criptografado
    target_extension = ".ransomwaretroll"

    print("[*] Iniciando varredura para descriptografia...")

    # Percorrer os arquivos no diretório atual
    for file_name in os.listdir():
        # Ignorar diretórios e o próprio script
        if os.path.isdir(file_name) or file_name.endswith(".py"):
            continue

        # Verificar se o arquivo possui a extensão de criptografia
        if file_name.endswith(target_extension):
            decrypt_file(file_name, key)

    print("[*] Processo de descriptografia concluído!")

if __name__ == "__main__":
    main()
