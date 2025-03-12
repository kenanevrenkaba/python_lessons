# print('Merhaba')

# String Format

urunAdi = uA = 'Elma'
urunFiyati = uF = 5
urunMiktarı = uM = 2.5
odenecekUcret = oU = urunFiyati * urunMiktarı 

# sonuc = str(urunMiktarı) + ' kg '+ urunAdi +' için ödemeniz gereken ücret ' + str(urunFiyati * urunMiktarı) + ' TL.'

# sonuc =  '{} kg {} için ödemeniz gereken ücret {} TL.' .format(uM, uA, oU)

# f-String

sonuc = f'{uM} kg {uA} için ödemeniz gereken ücret {oU} TL'

print(sonuc)