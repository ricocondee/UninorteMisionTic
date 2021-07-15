
//crear una clase en java
    //* definir nombre de la clase
    //* definir atributos de la clase
    //* definir metodos de la clase

class Estudiante{
    // atributos
    private int documento;
    private String nombre;
    private int edad;
    private String curso;

    //constructor vacio: crea un objeto sin valores, se usa cuando solo se va a enviar un parametro
    //public: se puede acceder desde cualquier clase
    //private: solo se puede acceder desde la misma clase, evita que se modifique desde clases externas
    public Estudiante(){

    }

    //constructor con parametros: crea un objeto con valores
    public Estudiante(int id, String name,  int age, String course){
        this.documento = id; // asigna al atributo documento el valor del parametro doc
        this.nombre = name;
        this.edad = age;
        this.curso = course;
    }

    //definir metodos
    //metodo imprimir
    public void imprimir(){
        System.out.println("El alumno "+nombre+" con id de estudiante "+documento+" tiene "+edad+" años y cursa la materia de "+curso);
    }
}

public class S4_POO {
    public static void main(String[] args) throws Exception {
        System.out.println("Ejemplo 1 Programacion orientada a objetos (POO)\n");
        //crear un objeto de la clase Estudiante
        Estudiante estudiante1 = new Estudiante();// crear un objeto de la clase Estudiante vacio
        Estudiante estudiante2 = new Estudiante(200171465, "Emanuel Rico Conde", 21, "Progamacion en Java" ); // crear un objeto de la clase Estudiante con parametros

        //llamar el metodo imprimir
        estudiante1.imprimir();
        System.out.println("");
        estudiante2.imprimir();

    }
}
