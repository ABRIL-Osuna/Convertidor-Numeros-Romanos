
def  conversion_entero_romano ( entero ):
    numeros  = [ 100 , 90 , 50 , 40 , 10 , 9 , 5 , 4 , 1 ]
    romanos  = [ 'C' , 'XC' , 'L' , 'XL' , 'X' , 'IX' , 'V' , 'IV' , 'I' ]

    numeral  =  ''
    i  =  0

    while  entero  >  0 :
        for  _  in  range ( entero  //  numeros [ i ]):
            numeral  +=  romanos [ i ]
            entero  -=  numeros [ i ]

        i  +=  1
    
    return numeral

x= int (input("Ingresa el numero decimal:"))
print ( conversion_entero_romano (x)) # 'XLV'
