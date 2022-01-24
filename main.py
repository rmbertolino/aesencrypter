from aesencrypter import EncryptString, DecryptString
import random

# Secret-Key : DUENDESRUGBYCLUB_9211a124-443d-47e3-9b5e-6263d9df5c47
# Identificador de comercio : 40ae4bcd-6a07-4e60-9d5d-714d8aea33b5
# Frase : 3mSbreV1MGzszTrmnw1ULUr5hg4Fl0pz0TdgJpot/Cw=

ip = "181.164.122.231"
secret_key = "DUENDESRUGBYCLUB_9211a124-443d-47e3-9b5e-6263d9df5c47"
SUCURSALID = ""

CALLBACKSUCCESS = "https://sedevirtualdev.herokuapp.com/api/notifications/paypertic/"
CALLBACKCANCEL = "https://sedevirtualdev.herokuapp.com/api/notifications/paypertic/"
MONTOORI = "150000"
CALLBACKPENDING = "https://sedevirtualdev.herokuapp.com/api/notifications/paypertic/"

COMERCIO = "40ae4bcd-6a07-4e60-9d5d-714d8aea33b5"
SUCURSALCOMERCIO = ""
TRANSACCIONCOMERCIOID = "e25892d5-2290-421f-b773-0e5a37e37700"
#PRODUCTO[0] = "Cuota Enero"
#MONTOPRODUCTO[0] = "521"
# HASH = ip + secret_key + COMERCIO + MONTO

# print(f'CALLBACKSUCCESS: {EncryptString(CALLBACKSUCCESS, secret_key)}')
# print(f'CALLBACKCANCEL: {EncryptString(CALLBACKCANCEL, secret_key)}')
# print(f'MONTO: {EncryptString(MONTO, secret_key)}')
# print(f'SUCURSALCOMERCIO: {EncryptString(SUCURSALCOMERCIO, secret_key)}')
# print(f'CALLBACKPENDING: {EncryptString(CALLBACKPENDING, secret_key)}')

CALLBACKSUCCESS = EncryptString(CALLBACKSUCCESS, secret_key)
CALLBACKCANCEL = EncryptString(CALLBACKCANCEL, secret_key)
MONTO = EncryptString(MONTOORI, secret_key)
SUCURSALCOMERCIO= EncryptString(SUCURSALCOMERCIO, secret_key)
CALLBACKPENDING= EncryptString(CALLBACKPENDING, secret_key)

# print(f'HASH: {EncryptString(HASH, secret_key)}')
#d = DecryptString(e, CALLBACKSUCCESS)

line = '<html>'
line += '<head>'
line += '<meta name="referrer" content="no-referrer">'
line +='</head>'

line +='<body>'

line +='        <form method="post" action="https://sandboxpp.asjservicios.com.ar">'
            
line +=f'            <input type="hidden" name="CallbackSuccess" value=\"{CALLBACKSUCCESS}\" /> '
line +=f'            <input type="hidden" name="CallbackCancel" value="{CALLBACKCANCEL}" /> '
line +=f'            <input type="hidden" name="Comercio" value= "{COMERCIO}" />'
line +=f'            <input type="hidden" name="SucursalComercio" value="{SUCURSALCOMERCIO}" />'

line +=f'            <input type="hidden" name="TransaccionComercioId" value=\"{random.randint(0,9999999999)}\" />'
            
line +='            <label>Monto: </label>'
line +=f'            <input type="text" name="Monto" value="{MONTO}"/>' 
            
line +='            <label>Producto 1: </label>'
line +='            <input type="text" name="Producto[0]" value="Enero Cuota" />'
line +='  <label>Monto Producto 1: </label>'
line +=f'  <input type="text" name="MontoProducto[0]" value="{MONTOORI}" />'
            
line +='          <button type="submit">ENVIAR</button>'
line +='        </form>'
line +='    </body>'
line +=' </html>'


with open("form.html", "w") as text_file:
    text_file.write(line)