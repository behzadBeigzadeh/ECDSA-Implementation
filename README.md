
# Elliptic Curve Digital Signature Algorithm (ECDSA) Implementation

This project demonstrates the implementation of the Elliptic Curve Digital Signature Algorithm (ECDSA) using Python. The algorithm is a cryptographic standard widely used for securing digital communications, including Bitcoin and blockchain technologies. It employs elliptic curve arithmetic to generate digital signatures and verify their authenticity.

This implementation uses the SECP256K1 curve, a standard used in Bitcoin, and includes functionality for key generation, message signing, and signature verification. The project is developed for educational purposes to showcase how ECDSA works at a low level, without relying on cryptographic libraries.
## Features

- **Elliptic Curve Arithmetic**:
  - Implements point addition, doubling, and scalar multiplication on the SECP256K1 curve.
- **Key Generation**:
  - Generates a private key and the corresponding public key.
- **Digital Signature**:
  - Signs a given message using the private key.
- **Signature Verification**:
  - Verifies the authenticity of a digital signature using the public key.
- **Hashing**:
  - Uses SHA-512 to hash messages before signing.
- **Custom Implementation**:
  - Avoids cryptographic libraries to provide a step-by-step mathematical understanding of ECDSA.
## How to Use

1. **Clone the Repository**:
   Clone the repository to your local machine:
   ```bash
   git clone https://github.com/your-username/ECDSA-Implementation.git
   cd ECDSA-Implementation
   
2. Run the Script: Ensure you have Python installed, then execute the script:
python ECDSA.py

3. Key Operations:

    The script generates a random private key and the corresponding public key.
    Signs a message using the private key.
    Verifies the signature using the public key.

4. Customize the Message: Edit the message in the script (e.g., msg = b'your-message') to test with custom inputs.

5. Dependencies:

    This implementation does not rely on any external libraries other than Python's standard hashlib and random modules.
   
---
Private Key: A randomly generated key unique to the session.
Public Key: The corresponding public key computed from the private key.
Message: The message to be signed and verified.
Signature: A pair of integers (r, s) representing the ECDSA signature.
Verification: Confirms if the signature is valid or not for the given message.

### ** Example Outputs**
Provide examples of the script’s output to give users an idea of what to expect. For instance:

```markdown
## Example Outputs

When you run the script, it generates the following output:

```plaintext
Private key: 0x1c8b5c7e2fa5e9e7d7f8...
Public key: (0x5ab3f46e10e493d6c3c7..., 0x8c3e2b4f7d9c5b2d7f8...)
Message: behzad!
Signature: (0x2f1e4b5c9a8d7e6f4b3a..., 0x1e4f6b7d8c3a9e2b5f6d...)
Verification: okeye

Message: i am behzad!
Verification: invalid



