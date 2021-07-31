public class Profesor extends Persona {
    //Definición de atributo
    protected int horasAsignadas;

    //Definición del constructor
    public Profesor(int id, String nombre, int horasAsignadas){
        super(id, nombre);
        this.horasAsignadas = horasAsignadas;
    }

    //Definir métodos set y métodos get
    public void setHorasAsignadas(int horasAsignadas){
        this.horasAsignadas = horasAsignadas;
    }

    public int getHorasAsignadas(){
        return horasAsignadas;
    }

    @Override
    public void Printed(){ //Sobreescritura de métodos y también hay polimorfismo
        System.out.println("Los datos del profesor son: id: "+getid()+
        " nombres: "+getNombre()+" horas asignadas: "+horasAsignadas);
    }

}