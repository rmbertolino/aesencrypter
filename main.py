from aesencrypter import EncryptString, DecryptString

# Secret-Key : DUENDESRUGBYCLUB_9211a124-443d-47e3-9b5e-6263d9df5c47
# Identificador de comercio : 40ae4bcd-6a07-4e60-9d5d-714d8aea33b5
# Frase : 3mSbreV1MGzszTrmnw1ULUr5hg4Fl0pz0TdgJpot/Cw=

ip = "181.164.122.231"
secret_key = "DUENDESRUGBYCLUB_9211a124-443d-47e3-9b5e-6263d9df5c47"
SUCURSALID = ""

CALLBACKSUCCESS = "https://sedevirtualdev.herokuapp.com/api/notifications/paypertic/"
CALLBACKCANCEL = "https://sedevirtualdev.herokuapp.com/api/notifications/paypertic/"
MONTO = "3524"
CALLBACKPENDING = "https://sedevirtualdev.herokuapp.com/api/notifications/paypertic/"

COMERCIO = "40ae4bcd-6a07-4e60-9d5d-714d8aea33b5"
SUCURSALCOMERCIO = ""
TRANSACCIONCOMERCIOID = "e25892d5-2290-421f-b773-0e5a37e3772d"
#PRODUCTO[0] = "Cuota Enero"
#MONTOPRODUCTO[0] = "521"

HASH = ip + secret_key + COMERCIO + MONTO

print(f'CALLBACKSUCCESS: {EncryptString(CALLBACKSUCCESS, secret_key)}')
print(f'CALLBACKCANCEL: {EncryptString(CALLBACKCANCEL, secret_key)}')
print(f'MONTO: {EncryptString(MONTO, secret_key)}')
print(f'CALLBACKPENDING: {EncryptString(CALLBACKPENDING, secret_key)}')
print(f'SUCURSALCOMERCIO: {EncryptString(SUCURSALCOMERCIO, secret_key)}')
print(f'HASH: {EncryptString(HASH, secret_key)}')
#d = DecryptString(e, CALLBACKSUCCESS)
