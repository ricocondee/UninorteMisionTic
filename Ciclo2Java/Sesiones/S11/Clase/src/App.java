public class App {
    public static void main(String[] args) throws Exception {
        System.out.println("Ejemplo SobreEscritura-Polimorfismo-Abstracción");
        //Instanciar una Persona
        //Persona p1  = new Persona();
        //Persona p2 = new Persona(7,"Maria");//Instanciando un objeto del tipo Persona
        //p2.Printed();//Llamada al método Printed de la clase persona
        //Imprimir el documento de la persona p1
        //System.out.println("El documento es: "+p2.getDocumento());

        //Creación de un objeto de tipo estudiante 
        Estudiante e1 = new Estudiante(57,"Marcela", "Java");
        e1.Printed(); //Llamada al método Printed de la clase Estudiante

        Profesor p1 = new Profesor(111,"Carmen", 100);
        p1.Printed();//Llamada al método Printed del profesor.
        p1.horasAsignadas = 27;
        p1.Printed();
    }
}