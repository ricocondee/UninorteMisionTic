import paquetes.ClaseHija_Resta;
import paquetes.ClaseHija_Suma;

public class Herencia {
    public static void main(String[] args) throws Exception {
        
        ClaseHija_Suma sumas = new ClaseHija_Suma();
        sumas.pedirDatos();
        sumas.sumar();
        System.out.print("El resultado de la suma es: ");
        sumas.mostrarResultado();

        ClaseHija_Resta restas = new ClaseHija_Resta();
        restas.pedirDatos();
        restas.restar();
        System.out.print("El resultado de la resta es: ");
        restas.mostrarResultado();
    }
}
