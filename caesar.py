def cc_enc(text,keys):
    result=""
    for ch in text:
        if ch.isalpha():
            base=ord('A') if ch.isupper() else ord('a')
            result=result+chr((ord(ch)-base+keys)%26+base)
        else:
            result=result+ch
    return result

def cc_dec(text,keys):
    return cc_enc(text,-keys)

if __name__=="__main__":
    text=str(input("Enter text: "))
    key=int(input("Enter key: "))
    print("Original text:",text)
    enc_text=cc_enc(text,key)
    print("Encrypted text:",enc_text)
    dec_text=cc_dec(enc_text,key)
    print("Decrypted text:",dec_text)