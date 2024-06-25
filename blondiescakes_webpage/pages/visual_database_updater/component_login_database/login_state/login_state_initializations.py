from passlib.context import CryptContext


#initializations
crypto=CryptContext(schemes=["bcrypt"])


"""
hash=crypto.hash("XEn12434hjsER+rmu-U6g2")
pas="XEn3asER+rmuU6g2"
pas2="XEn12434hjsER+rmu-U6g2"
print(hash)

verify=crypto.verify(pas2,hash)
print(verify)"""