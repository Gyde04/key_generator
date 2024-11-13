# 🔐 RSA Key Generator

A Python-based tool for generating secure RSA public and private key pairs using the `cryptography` library. Ideal for security applications, this tool simplifies the creation and storage of cryptographic keys with a straightforward, reliable implementation.

---

## 🚀 Features

- 🔑 **2048-bit RSA Key Generation**: Provides strong encryption and decryption.
- 📄 **PEM Format Output**: Keys are generated in a widely-used, easily portable format.
- 🔒 **Secure Key Generation**: Utilizes the industry-standard `cryptography` library for robust security.
- 🗂️ **Automatic Key File Creation**: Saves keys in `.pem` files for easy storage and usage.
- 🛠️ **Simple and Flexible**: Minimal setup and straightforward usage.

---

## 📋 Prerequisites

Ensure the following are installed:

- **Python** 3.x
- **pip** (Python package manager)

---

## 🔧 Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/Gyde04/key_generator.git
   cd key_generator
   ```

2. **Install Required Packages**
   ```bash
   pip3 install cryptography
   ```

---

## 💻 Usage

Generate RSA key pairs by running the following command:

```bash
python3 generate_keys.py
```

The script will generate two files:
- **`private_key.pem`**: Contains the private key.
- **`public_key.pem`**: Contains the public key.

Both keys will also display in the terminal for immediate viewing.

---

## 📁 Output Format

The generated keys are in **PEM** format:

### Private Key Example
```
-----BEGIN PRIVATE KEY-----
[Base64 encoded private key]
-----END PRIVATE KEY-----
```

### Public Key Example
```
-----BEGIN PUBLIC KEY-----
[Base64 encoded public key]
-----END PUBLIC KEY-----
```

---

## 🔐 Security Considerations

- 🚫 **Do not share** your private key.
- 🔒 Store private keys securely, ideally with restricted access.
- 🔐 Use appropriate file permissions to protect key files.
- 🛡️ For additional security, consider encrypting the private key with a password.
- 📥 **Update** the cryptography library to the latest version to stay protected.

---

## 🛠️ Technical Details

| Property         | Value                 |
|------------------|-----------------------|
| **Key Type**     | RSA                   |
| **Key Size**     | 2048 bits             |
| **Format**       | PKCS#8 (Private), SubjectPublicKeyInfo (Public) |
| **Encoding**     | PEM (Base64 encoded DER) |

---

## 🤝 Contributing

Contributions are welcome! To contribute:

1. **Fork** the repository.
2. **Create** a feature branch:
   ```bash
   git checkout -b feature/improvement
   ```
3. **Commit** your changes:
   ```bash
   git commit -am 'Add new feature'
   ```
4. **Push** to the branch:
   ```bash
   git push origin feature/improvement
   ```
5. **Create a Pull Request** for review.

---

## 🔍 Common Issues and Solutions

- **Issue**: *Script not found*
  - **Error**: `python3: can't open file 'generate_keys.py': [Errno 2] No such file or directory`
  - **Solution**: Ensure you are in the directory containing `generate_keys.py`.

- **Issue**: *Module not found*
  - **Error**: `ModuleNotFoundError: No module named 'cryptography'`
  - **Solution**: Install the required package with:
    ```bash
    pip3 install cryptography
    ```

---

## 📞 Contact

For questions or suggestions, find me on **GitHub**: [@Gyde04](https://github.com/Gyde04)

---

## 🙏 Acknowledgments

- **Cryptography.io** for providing the robust `cryptography` library.
- The open-source community for ongoing inspiration and support.

---

## 📝 License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## ⚠️ Disclaimer
This tool is for educational and development purposes. For production use, follow best practices in key management and security protocols.

---
