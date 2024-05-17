class CuentaCorriente():

    def __init__(self, nCuenta, titular, saldo):
        self.nCuenta=nCuenta
        self.titular=titular
        self.saldo=saldo

    def infCuenta(self):
        return "N° cuenta " + self.nCuenta + ". Titular: " + self.titular + ". Saldo: " + str(self.saldo)
    
    def ingresarDinero(self, dineroIngresar):

        self.saldo+=dineroIngresar
    
    def retirarDinero(self, dineroRetirar):

        self.saldo-=dineroRetirar

class CuentaJoven(CuentaCorriente):

    def __init__(self, nCuenta, titular, saldo, bonus_promocion=0):
        super().__init__(nCuenta,titular, saldo)
        self.bonus_promocion=bonus_promocion
        saldo+=bonus_promocion

    def getBonus(self):
        return self.bonus_promocion
    
    def infCuenta(self):
        return super().infCuenta() + " Bonu: " + str(self.bonus_promocion)

cuenta1=CuentaCorriente("001","Silver",2500)
cuenta2=CuentaJoven("002","Silver2",2500)

print(cuenta1.infCuenta())

cuenta1.ingresarDinero(500)
cuenta1.retirarDinero(100)

print(cuenta1.infCuenta())

cuenta2.ingresarDinero(200)
print(cuenta2.infCuenta())
