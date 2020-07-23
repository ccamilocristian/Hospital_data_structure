import numpy as np
class Paciente():
    def __init__(self, nombre, edad, ID,  eps, HospitalAsignado,estrato, enfermedades, citas, base, base_hospitales):
        """
        
        *nombre=Relaciona el nombre y apellido del paciente
        
        *edad= Relaciona la edad del paciente
        
        *ID=Relaciona la identificación del paciente.
        
        *HospitalAsignado=Relaciona el hospital en donde esta asignado el paciente.
        
        *estrato=Relaciona el estrato en el que vive el paciente.
        
        *enfermedades=Relaciona el listado de enfermedades que tiene el paciente. 
        
        *citas= Relaciona el listado de citas que tiene el paciente.
        
        *base=relaciona la base de datos donde se encuetran los clientes según el hospital.
        """
        self.nombre=nombre
        self.edad=edad
        self.ID=ID
        self.eps=eps
        self.HospitalAsignado=HospitalAsignado
        self.estrato=estrato
        self.enfermedades=enfermedades
        self.citas=citas
        self.base=base
        self.base_hospitales=base_hospitales
        
    def CalcularCostoCita(self):
        """
        
        *La función relaciona el cálculo del costo de la cita para el paciente en cuestión. Para este método es necesario la edad del paciente.
        """
        costo_cita=np.where(50000-self.edad*400<6000, 6000, 50000-self.edad*400)
        print("La cita tiene un costo de:",costo_cita)
        
    def CalcularCostoMedicamentos(self):
        """
        
        *La función relaciona la edad y el estrato para calcular el costo de los medicamentos.
        """
        costo_medica=np.where(20000-self.edad*400+self.estrato*3000<5000, 5000,
                              np.where(20000-self.edad*400+self.estrato*3000>18000,18000, 20000-self.edad*400+self.estrato*3000 ))
        print("El costo de los medicamentos es:",costo_medica)
        
    def ActualizarNombre(self, nombreActualizado):
        """
        **nombreActualizado=Relaciona el nombre por el cual será actualizado el paciente.
        
        * La función relaciona la información del paciente con la variable nombreActualizado para actualizarlo en la base.
        """
        print("Nombre anterior:", self.nombre)
        self.nombre=nombreActualizado
        for i in range(len(self.base[self.HospitalAsignado])):
            if self.base[self.HospitalAsignado][i]['ID']==self.ID:
                self.nombre=nombreActualizado
                dic={"nombre":self.nombre, "edad":self.edad, "ID":self.ID, "EPS":self.eps, "Hospital":self.HospitalAsignado, "estrato":self.estrato, "enfermedades":self.enfermedades, "Citas":self.citas}
                self.base[self.HospitalAsignado][i].update(dic)
                print("Nombre actualizado a:", self.nombre)
            else:
                pass        
        
        
    def ImprimirDatos(self):
        print("#####################")
        print("Paciente ID {}".format(self.ID))
        print("######################")
        print("{}, {} Años".format(self.nombre,self.edad))
        print("EPS: {}".format(self.eps))
        print("Hospital Asignado: {}".format(self.HospitalAsignado))
        print("Enfermedades: {}".format(self.enfermedades))
        print("Citas Pendientes: {}".format(self.citas))
        print("######################")
        
    def ActualizarEdad(self, edadActualizado):
        """
        
        **edadActualizado=Relaciona la edad por el cual será actualizada el paciente.
        
        * La función relaciona la información del paciente con la variable edadActualizado para actualizarlo en la base.
        """
        
        print("Edad anterior:", self.edad)
        for i in range(len(self.base[self.HospitalAsignado])):
            if self.base[self.HospitalAsignado][i]['ID']==self.ID:
                self.edad=edadActualizado
                dic={"nombre":self.nombre, "edad":self.edad, "ID":self.ID, "EPS":self.eps, "Hospital":self.HospitalAsignado, "estrato":self.estrato, "enfermedades":self.enfermedades, "Citas":self.citas}
                self.base[self.HospitalAsignado][i].update(dic)
                print("Edad actualizado a:", self.edad)
            else:
                pass
        
        
        
    def ActualizarID(self, idActualizado):
        """
        
        **idActualizado=Relaciona la identiciación por el cual será actualizada el paciente.
        
        *La función relaciona la información del paciente con la variable idActualizado para actualizarlo en la base.
      
        """
        print("Id anterior", self.ID)
        for i in range(len(self.base[self.HospitalAsignado])):
            if self.base[self.HospitalAsignado][i]['ID']==self.ID:
                self.ID=idActualizado
                dic={"nombre":self.nombre, "edad":self.edad, "ID":self.ID, "EPS":self.eps, "Hospital":self.HospitalAsignado, "estrato":self.estrato, "enfermedades":self.enfermedades, "Citas":self.citas}
                self.base[self.HospitalAsignado][i].update(dic)
                print("Id actualizado a:", self.ID)
            else:
                pass        
        
    def TrasladarPaciente(self):
        """
        
        *La función relaciona la información del paciente para ser trasladado a otro Hospital a través de un input.
        """
        
        print("Eps del paciente:",self.eps)
        
        for nomeps in self.base_hospitales.keys():
            if nomeps==self.eps:
                print("Hospitales para trasladar: \n")
                print(self.base_hospitales[self.eps])
                otroHospital=input("Escriba el hospital a donde se realizará el traslado: ")
                
                if otroHospital in self.base_hospitales[self.eps]:
                    
                    for i in range(len(self.base[self.HospitalAsignado])):
                        if self.base[self.HospitalAsignado][i]['ID']==self.ID:
                            del self.base[self.HospitalAsignado][i]
                            self.HospitalAsignado=otroHospital
                            dic={"nombre":self.nombre, "edad":self.edad, "ID":self.ID, "EPS":self.eps, "Hospital":self.HospitalAsignado, "estrato":self.estrato, "enfermedades":self.enfermedades, "Citas":self.citas}
                            self.base[self.HospitalAsignado].append(dic)
                            #print("Traslado exitoso de hospital")
                        else:
                            pass
                    print("Cliente trasladado a:",self.HospitalAsignado)
                else:
                    print("El hospital designado no se encuentra dentro de las opciones de la eps")
    
    def diccionario(self):
        """
        
        *La función relaciona la información del paciente en un diccionario exportable. 
        """
        dic={"nombre":self.nombre, "edad":self.edad, "ID":self.ID, "EPS":self.eps, "Hospital":self.HospitalAsignado, "estrato":self.estrato, "enfermedades":self.enfermedades, "Citas":self.citas}
        print(dic)
        return dic
    
class Hospital():
    def __init__(self, Capacidad, EPS, institucion, pacientes, base_hospitales):
        """
        
        *Capacidad= Relaciona la cantidad de pacientes que tiene capacidad el hospital para atender. 
        
        *EPS= Relaciona la EPS a la que pertenece el hospital.
        
        *institucion= Relaciona el nombre del hospital a revisar.
       
        *pacientes= Relaciona el listado de pacientes que se encuentran en el hospital.
        
        *base_hospitales=Relaciona la base de los hospitales y el listado de pacientes en el mismo
        
        """
        self.Capacidad=Capacidad
        self.pacientes=pacientes
        self.EPS=EPS
        self.institucion=institucion
        self.base=base_hospitales
        
    def verificarEPS(self, eps_validar):
        """
        
        *La función relaciona la informacion de cada hospital y valida si la variable se encuentra en el listado de posibilidades.
        """
        print("Eps a validar:", eps_validar)

        if self.EPS==eps_validar:              
            print("La EPS a validar corresponde a EPS del Hospital")
        else:
            print("La EPS no corresponde a la EPS del hospital")
    
    def imprimirInfo(self):

        print("#####################")
        print("Hospital: {}".format(self.institucion))
        print("######################")
        print("Pacientes: ")
        for i in range(len(self.base[self.institucion])):
            print("Nombre: ",self.base[self.institucion][i]['nombre'])
            print("edad: ",self.base[self.institucion][i]['edad'])
            print("ID: ",self.base[self.institucion][i]['ID'])
            print("estrato: ",self.base[self.institucion][i]['estrato'])
            print("enfermedades: ",self.base[self.institucion][i]['enfermedades'])
            print("Citas: ",self.base[self.institucion][i]['Citas'])
            print("-------------")
        print("EPS: {} ".format(self.EPS))
        print("Capacidad disponible: {} ".format(self.Capacidad-len(self.pacientes)))
        print("Capacidad Total: {} ".format(self.Capacidad))
        print("######################")   
        

    
    def crear_paciente(self, nombre, edad, ID, estrato, enfermedades, citas):
       """
        
       * La función recibe la infomación de nuevos pacientes y los agrega al diccionario del hospital en cuestión. 
       """
       for i in range(len(self.base.keys())):
            if list(self.base)[i]==self.institucion:
                dic={"nombre":nombre, "edad":edad, "ID":ID, "EPS":self.EPS, "Hospital":self.institucion, "estrato":estrato, "enfermedades":enfermedades, "Citas":citas}
                self.pacientes.append(dic)
                print("creacion paciente nuevo")
            else:
                pass