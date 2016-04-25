def B2I(b):
    assert type(b) is bytes
    return int.from_bytes(b, byteorder='big')

def I2B(i, length):
    assert type(i) is int
    assert type(length) is int and length >= 0
    return int.to_bytes(i, length, byteorder='big')

def HMAC_SHA256(key, msg):
    import hmac
    return hmac.new(key, msg, 'sha256').digest()

def SYSTEM(command, stdin=None):
    from subprocess import Popen, PIPE
    proc = Popen(command, stdin=PIPE, stdout=PIPE, stderr=PIPE)
    stdout, stderr = proc.communicate(stdin)
    return stdout, stderr, proc.returncode

def RSA_DECRYPT(skfilename, ciphertext):
    assert type(skfilename) is str
    assert type(ciphertext) is bytes
    stdout, stderr, retcode = SYSTEM((
        'openssl', 'rsautl', '-decrypt', '-inkey', skfilename
    ), ciphertext)
    assert retcode == 0 and stderr == b''
    return stdout

def TLS_PRF(secret, label, seed, n_bytes):
    assert type(secret) is bytes
    assert type(label) is bytes
    assert type(seed) is bytes
    assert type(n_bytes) is int and n_bytes >= 0
    last_A = label + seed
    result = b''
    while len(result) < n_bytes:
        last_A = HMAC_SHA256(secret, last_A)
        result += HMAC_SHA256(secret, last_A + label + seed)
    return result[:n_bytes]

def AES128CBC_DECRYPT(secret_key, ini_vector, ciphertext):
    assert type(secret_key) is bytes and len(secret_key) == 16
    assert type(ini_vector) is bytes and len(ini_vector) == 16
    assert type(ciphertext) is bytes and len(ciphertext) % 16 == 0
    stdout, stderr, retcode = SYSTEM((
        'openssl', 'enc', '-aes-128-cbc', '-d', '-nopad',
        '-K', ''.join('%02x'%x for x in secret_key),
        '-iv', ''.join('%02x'%x for x in ini_vector)
    ), ciphertext)
    assert retcode == 0 and stderr == b''
    return stdout
