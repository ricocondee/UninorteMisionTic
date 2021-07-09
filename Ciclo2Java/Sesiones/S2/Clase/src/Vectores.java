package Ciclo2Java.Sesiones.S2.Clase.src;

import java.util.Scanner;

public class Vectores {
    public static void main(String[] args) throws Exception {
        Scanner input = new Scanner(System.in);
        int N, i; // Variable para almacenar el número de elementos del array
        System.out.println("Digite la cantidad de edades a ingresar");
        N = input.nextInt(); // Capturar el valor ingresado por teclado
        int Edades[] = new int[N]; // Definición del array
        float promedio = 0; // Variable para calcular el promedio

        // tomar los datos del array
        System.out.println("-----------Ingreso de Edades----------------");
        for (i = 0; i < N; i++) {
            System.out.println("Digite la edad " + (i + 1));
            Edades[i] = input.nextInt();
        }

        // Imprimir los datos del array
        System.out.println("-----------Impresión de Edades----------------");
        for (i = 0; i < N; i++) {
            System.out.println("Edad " + (i + 1) + " = " + Edades[i]);
            promedio = promedio + Edades[i]; // Sumando todas las edades
        }
        promedio = promedio / N;
        System.out.printf("El promedio de las edades es: %.2f", promedio);

    }
}