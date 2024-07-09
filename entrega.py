#REQUERIMENTOS
#Crear un arbol binario de busqueda para ordenar a los empleados
#El empleado debe poder mostrar su informacion


class Employee:
  def __init__(self, Nombre, Apellido, Email, Telefono, Especialidad, Cedula, Horas):
      self.Nombre = Nombre
      self.Apellido = Apellido
      self.Email = Email
      self.Telefono = Telefono
      self.Especialidad = Especialidad
      self.cedula = Cedula
      self.Horas = Horas
      self.salario = 5800


  def CalcularSalario(self):
     return self.Horas*self.salario

  def getInfo(self):

      return (f"""Empleado:
                  Nombre: {self.Nombre}
                  Apellido: {self.Apellido}
                  Email: {self.Email}
                  Especialidad: {self.Especialidad}
                  Documento de identidad: {self.cedula}
                  Horas asignadas: {self.Horas}
                  Salario: {self.CalcularSalario()}
              """)



class Arbol:

    def __init__(self, employee=None):

      self.nodo =  employee
      self.right = None
      self.left = None


    def insert(self, nodo):

        if not self.nodo:

            self.nodo = nodo

            return



        if self.nodo == nodo:

            return



        if nodo.cedula < self.nodo.cedula:

            if self.left:

                self.left.insert(nodo)

                return

            self.left = Arbol(nodo)

            return



        if self.right:

            self.right.insert(nodo)

            return

        self.right = Arbol(nodo)


    def delete(self, nodo):

        if self == None:

            return self

        if self.right == None:

            return self.left

        if self.left == None:

            return self.right

        if nodo.cedula < self.nodo.cedula:

            if self.left:

                self.left = self.left.delete(nodo)

            return self

        if nodo.cedula > self.nodo.cedula:

            if self.right:

                self.right = self.right.delete(nodo)

            return self

        min_larger_node = self.right

        while min_larger_node.left:

            min_larger_node = min_larger_node.left

        self.nodo = min_larger_node.nodo

        self.right = self.right.delete(min_larger_node.nodo)

        return self


    def printPrueba(self):
      print(self.left)
      print(self.right)
      print(self.nodo.cedula)

    def exists(self, cedula):
      current_node = self  # Assuming `root` is the root node

      while current_node is not None:
          if cedula == current_node.nodo.cedula:
              return current_node.nodo.getInfo()  # Assuming `getInfo` retrieves desired info
          elif cedula < current_node.nodo.cedula:
              current_node = current_node.left
          else:
              current_node = current_node.right

      return "El empleado no existe"  # Employee not found message
      print(self.nodo.cedula)


    def inorder(self, nodos):

        if self.left is not None:

            self.left.inorder(nodos)

        if self.nodo is not None:

            nodos.append(self.nodo)

        if self.right is not None:

            self.right.inorder(nodos)

        return nodos

    

def testFunc():
  employee1=Employee("A","B","C",12,"ASD",12345,16)
  employee2=Employee("ASD","FDB","GC",15,"ASD",12455,13)
  employee3=Employee("ADFG","BDSFG","CGDFSG",12,"ASD",123323,13)
  employee4=Employee("ADFG","BSDF","CHD",12,"ASD",1643498,12)
  arb = Arbol()
  arb.insert(employee3)
  arb.insert(employee2)
  arb.insert(employee1)
  arb.insert(employee4)

  arb.delete(employee2)
  arb.printPrueba()
  print(arb.exists(12445))

testFunc()