#-*- coding: utf-8 -*-

from openerp import models, fields, api
class calculadora(models.Model):
	_name = 'calculadora'
	capitalinicial = fields.Float()
	capitalfinal = fields.Float()
	interes = fields.Float()
	temps = fields.Integer()
	#retencio = none
	interesos = fields.Float()

	@api.one
	def calcula(self):
		#Codi per fer càlculs
		self.capitalfinal = format(self.capitalinicial * ((1 + self.interes) ** self.temps))
		self.interesos = format(self.capitalfinal - self.capitalinicial)


"""
class Calculadora:

    def __init__(self):

        # Variables de clase
        self.capital_inicial = 100000
        self.capital_final = None
        self.interes = 0.0865
        self.temps = 15
        self.retencio = None
        self.interesos = 0;

    def cap_final(self):
        self.capital_final = self.capital_inicial * ((1 + self.interes) ** self.temps)
        print self.capital_final

    def int_generats(self):
        interesos = self.capital_final - self.capital_inicial
        print interesos

    #def ret_aplicada(selfself):


if __name__ == '__main__':

    # Creacio de l'objecte
    calc = Calculadora()
    calc.cap_final()
    calc.int_generats()
"""
