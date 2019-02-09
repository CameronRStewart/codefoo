import hashlib

def compare_hashes(a, b):
    m = hashlib.md5()
    m.update("madwire".encode('utf-8'))
