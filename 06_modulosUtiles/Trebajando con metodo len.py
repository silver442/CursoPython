class Agenda():

    def __init__(self):
        
        self.miAgenda={}

    def agregarPersonas(self, nombre, telefono):

        self.miAgenda[nombre]=telefono

    def __len__(self):

        return len(self.miAgenda)

agendaPersonal=Agenda()

agendaPersonal.agregarPersonas("Juan", "465458746")
agendaPersonal.agregarPersonas("Maria", "5632478952")
agendaPersonal.agregarPersonas("Juansdd", "465458746")
agendaPersonal.agregarPersonas("Mariadsd", "5632478952")

print(len(agendaPersonal))