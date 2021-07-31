public class Estudiante extends Persona {
    //Definición de atributos
    private String curso;

    //Definción del constructor en la clase derivada
    public Estudiante(int id, String nombre, String curso){
        super(id, nombre);//Llamada al constructor de la superclase
        this.curso = curso;
    }

    //Definición del set y el get para los atributos de la subclase
    public void setCurso(String curso){
        this.curso = curso;
    }

    public String getCurso(){
        return curso;
    }

    @Override  //Realiza un sobreescritura del métod
    public void Printed(){ //Sobreescritura de métodos y también hay polimorfismo
        System.out.println("Los datos del estudiante son: id: "+getid()+
        " nombres: "+getNombre()+" curso: "+curso);
    }
}