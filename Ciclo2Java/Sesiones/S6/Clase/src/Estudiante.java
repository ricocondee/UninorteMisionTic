public class Estudiante {
    //Definición atributos
    private String Nombre;
    private float Nota1;
    private float Nota2;
    private float Nota3;

    //Definir el constructor
    Estudiante(String nombre, float nota1, float nota2, float nota3){
        this.Nombre = nombre;
        this.Nota1 = nota1;
        this.Nota2 = nota2;
        this.Nota3 = nota3;
    }

    //Definir los métodos set: Se debe realizar para cada atributo.
    public void setNombre(String nombre){
        this.Nombre = nombre;
    }

    public void setNota1(float nota1){
        this.Nota1 = nota1;
    }

    public void setNota2(float nota2){
        this.Nota2 = nota2;
    }

    public void setNota3(float nota3){
        this.Nota3 = nota3;
    }

    
    //Definir los métodos get: Se debe realizar para cada atributo.
    public String getNombre(){
        return Nombre; //Devuelve el valor almacenado en el atributo Nombre
    }

    public float getNota1(){
        return Nota1; //Devuelve el valor almacenado en el atributo Nota1
    }

    public float getNota2(){
        return Nota2; //Devuelve el valor almacenado en el atributo Nota2
    }

    public float getNota3(){
        return Nota3; //Devuelve el valor almacenado en el atributo Nota2
    }

    public float Promediar(){
        return (Nota1 + Nota2 + Nota3)/3;
    }

}