# Blum-Goldwasser
Crypto HW3

I implemented Blum-Goldwasser as was outlined in the cryptography slides. I took a log(log(N)) bit chunk out of the message and xor'ed it with an x. I then processed the x via a formula before taking another chunk and xor'ing. I do this until I get an encrypted message.

As for the decryption, it's mostly the same except I ran through another decryption algorithm which gave me the original x used by the encryption.

Output
----------------------------------------------------
Original  [1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0]

Encrypted [0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0]

Decrypted [1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0]

Original == Decrypted
