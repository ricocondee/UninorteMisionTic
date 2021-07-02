package Ciclo2Java.Sesiones.S1.Clase.src;

//Programa que lea una cantidad de grados centigrados y la pase a grados farenheigth
//la formula correspondiente para pasar de C a F es: r = 32 + (9 * c / 5)

import java.util.Scanner;
public class Secuencial1 {
    public static void main(String[] args) throws Exception {
        Scanner ingreso = new Scanner(System.in);
        double gradoC, gradoF;
        System.out.println("Grados centigrados (°C): ");
        gradoC = ingreso.nextDouble();
        gradoF = 32 + (9 * gradoC / 5);
        System.out.println(gradoC + "°C = " + gradoF + "°F");
        ingreso.close();
    }
}
