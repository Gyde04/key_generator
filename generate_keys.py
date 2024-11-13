from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend

def generate_keys():
    # Generate private key
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
    )

    # Generate public key
    public_key = private_key.public_key()

    # Serialize private key
    private_pem = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    )

    # Serialize public key
    public_pem = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )

    # Save private key to file
    with open('private_key.pem', 'wb') as f:
        f.write(private_pem)

    # Save public key to file
    with open('public_key.pem', 'wb') as f:
        f.write(public_pem)

    return private_pem, public_pem

# Generate the keys
private_key, public_key = generate_keys()

# Print the keys
print("Private Key:")
print(private_key.decode())
print("\nPublic Key:")
print(public_key.decode())
