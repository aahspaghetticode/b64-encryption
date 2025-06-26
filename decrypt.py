import base64
import sys

def is_base64(s):
    if not isinstance(s, str) or not s:
        return False
    try:
        s_clean = ''.join(s.strip().split())
        decoded = base64.b64decode(s_clean, validate=True)
        return base64.b64encode(decoded).decode() == s_clean
    except:
        return False

encoded = input("Encrypted string:")
if is_base64(encoded):
    decode = base64.b64decode(encoded.encode('utf-8'))
else:
    print("Invalid string. Exiting...")
    sys.exit()

keyi = input("Whats the key?")
key = keyi
#Remove padding to prevent brute-forcing everything before it

# Check for the FULL salt string representation (b'...') 
decoded_str = decode.decode()
salt_str = str(key)  # This matches how salt was inserted
if salt_str in decoded_str:
    # Remove the entire salt string
    decode1 = decoded_str.replace(salt_str, "", 1)
else:
    print("Invalid key or invalid string. Exiting...")
    sys.exit()

# Extract base64 payload from Python's bytes literal format
final = base64.b64decode(decode1[2:-1].encode('utf-8')).decode('utf-8')
print(final)

