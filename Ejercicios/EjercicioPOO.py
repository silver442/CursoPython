class CuentaCorriente():
    nCuenta=""
    titular=""
    saldo=0

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
    
cuenta1=CuentaCorriente("001","Silver",2500)
cuenta2=CuentaCorriente("001","Silver",2500)

print(cuenta1.infCuenta())

cuenta1.ingresarDinero(500)
cuenta1.retirarDinero(100)

print(cuenta1.infCuenta())
