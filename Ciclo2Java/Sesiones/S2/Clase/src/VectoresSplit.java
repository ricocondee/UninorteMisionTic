package Ciclo2Java.Sesiones.S2.Clase.src;

import java.util.Scanner;

public class VectoresSplit {
    public static void main(String[] args) throws Exception {
        Scanner input = new Scanner(System.in);
        var datoEntrada = "";
        System.out.println("Ingrese los datos separado por espacio");
        datoEntrada = input.nextLine();
        // datoEntrada = datoEntrada.replaceAll(" ", ","); //Reemplazando 1 espacio en blanco por ,
        String datosArray[] = datoEntrada.split("\\s+"); // \\s+ permite ingresar varios espacios en el split
        System.out.println(datosArray.length);
        for (int i = 0; i < datosArray.length; i++) {
            System.out.println(datosArray[i]);
        }

    }
}
