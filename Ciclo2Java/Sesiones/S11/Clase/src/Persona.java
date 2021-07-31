public abstract class Persona {
    //Definición de atributos
    private int id;
    private String nombre;

    //Definir el constructor
    public Persona(int id, String nombre ){
        this.id = id;
        this.nombre = nombre;
    }

    //Definir métodos set y get
    public void setid(int id){
        this.id = id;
    }

    public void setNombre(String nombre){
        this.nombre = nombre;
    }

    public int getid(){
        return id;
    }

    public String getNombre(){
        return nombre;
    }

    /*
    public void Printed(){//Método sin abstracción
        System.out.println("Los datos de la persona son id: "+id+" nombre:"+nombre);
    }
    */
    //Definición del método abstracto
    public abstract void Printed();
}