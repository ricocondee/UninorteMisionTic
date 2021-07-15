package Ciclo2Java.Sesiones.S1.Clase.src;

import java.util.Scanner;

//Dados los catetos de un triangulo, calcular la hipotenusa
public class S1_Secuencial2 {
    public static void main(String[] args) throws Exception{
        Scanner ingreso = new Scanner(System.in);
        double a, b, hip;
        System.out.println("Cateto A: ");
        a = ingreso.nextDouble();
        System.out.println("Cateto B: ");
        b =  ingreso.nextDouble();
        hip = Math.sqrt(Math.pow(a,2) + Math.pow(b,2));
        System.out.println("La hipotenusa del triangulo es: " + Math.round(hip));
        ingreso.close();
    }
    
}
