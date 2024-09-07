### Project Description:

This project involves generating cryptographic keys and performing encryption and decryption using RSA and AES algorithms. It includes two main programs:

1. **genkeys.py:**
   - **Purpose:** Generates public and private key pairs. The keys are saved in files named `name.pub` and `name.prv`, where `name` is the input provided by the user.

2. **crypt.py:**
   - **Purpose:** Handles encryption and decryption of files using AES and RSA. It encrypts plaintext files using AES, encrypts the AES key with RSA, and can also decrypt files by reversing the process.

### How to Execute the Project:

1. **Generate Keys:**
   - Execute `genkeys.py` to generate and save a public key and a private key. Provide the desired name for the key files when prompted.
   - **Instruction:** Run the `genkeys.py` program and input the desired name for the key files.

2. **Encrypt a File:**
   - Execute `crypt.py` with encryption mode to encrypt a plaintext file. Provide the public key file, input file, and output file where the encrypted data will be saved.
   - **Instruction:** Run the `crypt.py` program with encryption mode, specifying the public key file, input file, and output file.

3. **Decrypt a File:**
   - Execute `crypt.py` with decryption mode to decrypt an encrypted file. Provide the private key file, input encrypted file, and output file where the decrypted data will be saved.
   - **Instruction:** Run the `crypt.py` program with decryption mode, specifying the private key file, input file, and output file.

### Example Execution:

- To **generate keys**, execute: `python genkeys.py` and enter the desired name.

- To **encrypt a file**, execute: `python crypt.py --mode encrypt --pubkey name.pub --input plaintext.txt --output encrypted.txt`.

- To **decrypt a file**, execute: `python crypt.py --mode decrypt --privkey name.prv --input encrypted.txt --output decrypted.txt`.

This project ensures secure encryption and decryption of data using a combination of RSA and AES algorithms.
