m = False
while m == False:
    try:
        metros = float(input('fale uma distancia em metros '))
        print (metros*1000, 'KM')
        print (metros*100, 'HM')
        print (metros*10, 'DAM')
        print (metros/10, 'DM')
        print (metros/100, 'CM')
        print (metros/1000, 'MM')
        m = True
    except:
        print ('eu falei uma distancia em METROS, não pode ser uma letra')
        print ('tente novamente')