milista=["Eva", "Valentin", "Luz","Jesus"]
milista.append("Ronja")#agrega un nuevo elemento al final
milista.insert(4,"Garfield")#agrega un elemento en medio
milista.extend(["Canarios","Bosch"])#agrega varios elementos a la vez
milista.remove("Jesus")#milista.remove(5)
milista.pop()
print(milista[:])#imprime toda la lista
print(milista.index("Eva"))#devuelve le numero de indice
print("Flavia" in milista)#comprueba si esxiste el elemento en la lista

milista2=["Arnulfo","Ana"]*2
milista3=milista+milista2
print(milista3)