package Ciclo2Java.Sesiones.S1.Practica;

import java.util.Scanner;

public class Practico {
    public static void main(String[] args) throws Exception {
        Scanner ingreso = new Scanner(System.in);

        // Estructura condicional simple
        /* System.out.println("Cantidad actual de la mercancia almacenada: ");
        int cantbodega, cantreq;
        cantbodega = ingreso.nextInt();
        System.out.println("Cantidad minima requerida de la mercancia: ");
        cantreq = ingreso.nextInt();
        if (cantbodega < cantreq) {
            System.out.println("Es necesario hacer el pedido al proveedor.");
            System.out.println("Se debe pedir la cantidad de: " + (cantreq - cantbodega));
        } 
        if (cantbodega > cantreq) {
            System.out.println("No es necesario hacer el pedido al proveedor.");
        }
        ingreso.close(); */

        // Estructura condicional doble
        /* System.out.println("Cantidad actual de la mercancia almacenada: ");
        int cantbodega, cantreq;
        cantbodega = ingreso.nextInt();
        System.out.println("Cantidad minima requerida de la mercancia: ");
        cantreq = ingreso.nextInt();
        if (cantbodega < cantreq) {
            System.out.println("Es necesario hacer el pedido al proveedor.");
            System.out.println("Se debe pedir la cantidad de: " + (cantreq - cantbodega));
        } else {
            System.out.println("No es necesario hacer el pedido al proveedor.");
        }
        ingreso.close(); */

        // Estructura condicional multiple
        /* System.out.println("Cantidad actual de la mercancia almacenada en bodega: ");
        int cantbodega, cantreq;
        cantbodega = ingreso.nextInt();
        System.out.println("Cantidad minima requerida de la mercancia: ");
        cantreq = ingreso.nextInt();
        var venta = cantbodega - cantreq;
        if (cantbodega < cantreq){
            System.out.println("Es necesario hacer el pedido al proveedor.");
            System.out.println("Cantidad a pedir: "+ (cantreq- cantbodega));
        }
        else if (cantbodega > cantreq && venta > 10){
            System.out.println("No es necesario hacer el pedido al proveedor.");
            System.out.println("Se deben vender "+ venta + " unidades.");
        }
        else if (cantbodega > cantreq && venta < 10){
            System.out.println("No es necesario hacer el pedido al proveedor.");
            System.out.println("Se deben vender "+ venta + " unidades. Alerta generada");
        }
        ingreso.close(); */

        // Estructura condicional Anidada
        /* System.out.println("Cantidad actual de la mercancia almacenada en bodega: ");
        int cantbodega, cantreq, cantcom, valorcom, valorbox;
        cantbodega = ingreso.nextInt();
        System.out.println("Cantidad minima requerida de la mercancia: ");
        cantreq = ingreso.nextInt();
        var venta = cantbodega - cantreq;
        if (cantbodega < cantreq){
            System.out.println("Es necesario hacer el pedido al proveedor.");
            System.out.println("Cantidad a comprar: ");
            cantcom = ingreso.nextInt();
            System.out.println("Valor de la unidad");
            valorcom = ingreso.nextInt();
            var total = valorcom * cantcom;
            System.out.println("Valor en caja");
            valorbox = ingreso.nextInt();
            if (total < valorbox){
                System.out.println("Si se puede realizar el pedido");
            }
            else{
                System.out.println("No se puede realizar el pedido");
            }
        }
        else;
        if (cantbodega > cantreq){
            System.out.println("No es necesario hacer el pedido al proveedor.");
            System.out.println("Se deben vender "+ venta + " unidades");
            if (venta < 10){
                System.out.println("Alerta generada");
            }
            else;
        }
        else;
        ingreso.close(); */

        // Estructura dependiendo de o segun
        int semana, totalcom;
        System.out.println("Dia de la semana en numero");
        semana = ingreso.nextInt();
        System.out.println("Valor de la compra");
        totalcom = ingreso.nextInt();
        switch(semana)
        {
            case 1:
                var descuento = totalcom*0.05;
                var total = totalcom - descuento;
                System.out.println("El total a pagar es: " + total);
                break;

            case 2:
                var descuento2 = totalcom*0.03;
                var total2 = totalcom - descuento2;
                System.out.println("El total a pagar es: " + total2);
                break;

            case 3:
                var descuento3 = totalcom*0.10;
                var total3 = totalcom - descuento3;
                System.out.println("El total a pagar es: " + total3);
                break;
            case 4:
                var descuento4 = totalcom*0.04;
                var total4 = totalcom - descuento4;
                System.out.println("El total a pagar es: " + total4);
                break;
            case 5:
                var descuento5 = totalcom*0.06;
                var total5 = totalcom - descuento5;
                System.out.println("El total a pagar es: " + total5);
                break;
            case 6:
                var descuento6 = totalcom*0.02;
                var total6 = totalcom - descuento6;
                System.out.println("El total a pagar es: " + total6);
                break;
            case 7:
                var descuento7 = totalcom*0.05;
                var total7 = totalcom - descuento7;
                System.out.println("El total a pagar es: " + total7);
                break;
        }
        ingreso.close();
    }
}