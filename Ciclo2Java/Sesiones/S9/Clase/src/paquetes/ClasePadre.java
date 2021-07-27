package paquetes;
import java.util.Scanner;

public class ClasePadre {
    protected int valor1, valor2, resultado;
    Scanner input = new Scanner(System.in);


    // este metodo pide los valores al ususario
    public void pedirDatos(){
        System.out.print("Dame el primer valor: ");
        valor1 = input.nextInt();
        System.out.print("Dame el segundo valor: ");
        valor2 = input.nextInt();
    }

    // este metodo muestra el resultado al usuario
    public void mostrarResultado(){
        System.out.println(resultado);
    }
}
