def compruebaMail (mailUsuario):
	
	'''
	La función evalúa un mail recin¿bido en busca de la @
	si tiene una @ es correcto
	si tiene mas de una @ es incorrecto
	si tiene @ al final es incorrecto

	>>> compruebaMail('jesusperez.ipn@gmail.com')
	True

	>>> compruebaMail('jesusperez.ipn@@gmail.com')
	False

	>>> compruebaMail('jesusperez.ipngmail.com@')
	False

	>>> compruebaMail('jesusperez.ipngmail.com')
	False

	'''
	arroba=mailUsuario.count('@') 

	if (arroba!=1 or mailUsuario.rfind('@')==(len(mailUsuario)-1) or mailUsuario.find('@')==0):
		return False
	else:
		return True

import doctest
doctest.testmod()