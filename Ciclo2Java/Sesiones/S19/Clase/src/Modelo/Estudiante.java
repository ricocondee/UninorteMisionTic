package Modelo;

public class Estudiante {
    //Definición de atributos.
    private int Id;
    private int Documento;
    private String Nombre;
    private String Apellido;
    private int Celular;

    //Crear los constructores
    public Estudiante() {
    }

    public Estudiante(int id, int documento, String nombre, String apellido, int celular) {
        Id = id;
        Documento = documento;
        Nombre = nombre;
        Apellido = apellido;
        Celular = celular;
    }

    
    //Definir Métodos Getter y Setters
    public int getId() {
        return Id;
    }

    public void setId(int id) {
        Id = id;
    }

    public int getDocumento() {
        return Documento;
    }

    public void setDocumento(int documento) {
        Documento = documento;
    }

    public String getNombre() {
        return Nombre;
    }

    public void setNombre(String nombre) {
        Nombre = nombre;
    }

    public String getApellido() {
        return Apellido;
    }

    public void setApellido(String apellido) {
        Apellido = apellido;
    }

    public int getCelular() {
        return Celular;
    }

    public void setCelular(int celular) {
        Celular = celular;
    }   
}