//Realizacion del contenido practico sesion 1
// Me gusta resolver todo en el mismo archivo, como puedes ver hay varias piezas de codigo comentadas,
// son cada uno de los ejercicios requeridos en el S1-ComponentePractico.txt, tal como yo los entendi, 
// para usarlos solo descomentalos uno por uno ya que en varios de ellos se repiten las mismas variables.

package Ciclo2Java.Sesiones.S1.Practica;

import java.util.Scanner;

public class Practico {
    public static void main(String[] args) throws Exception {
        Scanner ingreso = new Scanner(System.in);

        // Estructura condicional simple

/*         System.out.println("Cantidad actual de la mercancia almacenada: ");
        int cantidadBodega, cantidadRequerida;
        cantidadBodega = ingreso.nextInt();
        System.out.println("Cantidad minima requerida de la mercancia: ");
        cantidadRequerida = ingreso.nextInt();
        if (cantidadBodega < cantidadRequerida) {
            System.out.println("Es necesario hacer el pedido al proveedor.");
            System.out.println("Se debe pedir la cantidad de: " + (cantidadRequerida - cantidadBodega));
        }
        if (cantidadBodega > cantidadRequerida) {
            System.out.println("No es necesario hacer el pedido al proveedor.");
        }
        ingreso.close(); */

        // Estructura condicional doble

/*         System.out.println("Cantidad actual de la mercancia almacenada: ");
        int cantidadBodega, cantidadRequerida;
        cantidadBodega = ingreso.nextInt();
        System.out.println("Cantidad minima requerida de la mercancia: ");
        cantidadRequerida = ingreso.nextInt();
        if (cantidadBodega < cantidadRequerida) {
            System.out.println("Es necesario hacer el pedido al proveedor.");
            System.out.println("Se debe pedir la cantidad de: " + (cantidadRequerida - cantidadBodega));
        } else {
            System.out.println("No es necesario hacer el pedido al proveedor.");
        }
        ingreso.close(); */

        // Estructura condicional multiple

/*         System.out.println("Cantidad actual de la mercancia almacenada en bodega: ");
        int cantidadBodega, cantidadRequerida;
        cantidadBodega = ingreso.nextInt();
        System.out.println("Cantidad minima requerida de la mercancia: ");
        cantidadRequerida = ingreso.nextInt();
        var venta = cantidadBodega - cantidadRequerida;
        if (cantidadBodega < cantidadRequerida) {
            System.out.println("Es necesario hacer el pedido al proveedor.");
            System.out.println("Cantidad a pedir: " + (cantidadRequerida - cantidadBodega));
        } else if (cantidadBodega > cantidadRequerida && venta > 10) {
            System.out.println("No es necesario hacer el pedido al proveedor.");
            System.out.println("Se deben vender " + venta + " unidades.");
        } else if (cantidadBodega > cantidadRequerida && venta < 10) {
            System.out.println("No es necesario hacer el pedido al proveedor.");
            System.out.println("Se deben vender " + venta + " unidades. Alerta generada");
        }
        ingreso.close(); */

        // Estructura condicional Anidada

/*         System.out.println("Cantidad actual de la mercancia almacenada en bodega: ");
        int cantidadBodega, cantidadRequerida, cantidadComprar, valorUnidad, efectivoEnCaja;
        cantidadBodega = ingreso.nextInt();
        System.out.println("Cantidad minima requerida de la mercancia: ");
        cantidadRequerida = ingreso.nextInt();
        var venta = cantidadBodega - cantidadRequerida;
        if (cantidadBodega < cantidadRequerida) {
            System.out.println("Es necesario hacer el pedido al proveedor.");
            System.out.println("Cantidad a comprar: ");
            cantidadComprar = ingreso.nextInt();
            System.out.println("Valor de la unidad");
            valorUnidad = ingreso.nextInt();
            var total = valorUnidad * cantidadComprar;
            System.out.println("Valor en caja");
            efectivoEnCaja = ingreso.nextInt();
            if (total < efectivoEnCaja) {
                System.out.println("Si se puede realizar el pedido");
            } else {
                System.out.println("No se puede realizar el pedido");
            }
        } else
            ;
        if (cantidadBodega > cantidadRequerida) {
            System.out.println("No es necesario hacer el pedido al proveedor.");
            System.out.println("Se deben vender " + venta + " unidades");
            if (venta < 10) {
                System.out.println("Alerta generada");
            } else
                ;
        } else
            ;
        ingreso.close(); */

        // Estructura dependiendo de o segun

/*         int diaSemana, precioCompra;
        System.out.println("Dia de la Semana en numero");
        diaSemana = ingreso.nextInt();
        System.out.println("Valor de la compra");
        precioCompra = ingreso.nextInt();
        switch (diaSemana) {
            case 1:
                var descuento = precioCompra * 0.05;
                var total = precioCompra - descuento;
                System.out.println("El total a pagar es: " + total);
                break;

            case 2:
                var descuento2 = precioCompra * 0.03;
                var total2 = precioCompra - descuento2;
                System.out.println("El total a pagar es: " + total2);
                break;

            case 3:
                var descuento3 = precioCompra * 0.10;
                var total3 = precioCompra - descuento3;
                System.out.println("El total a pagar es: " + total3);
                break;
            case 4:
                var descuento4 = precioCompra * 0.04;
                var total4 = precioCompra - descuento4;
                System.out.println("El total a pagar es: " + total4);
                break;
            case 5:
                var descuento5 = precioCompra * 0.06;
                var total5 = precioCompra - descuento5;
                System.out.println("El total a pagar es: " + total5);
                break;
            case 6:
                var descuento6 = precioCompra * 0.02;
                var total6 = precioCompra - descuento6;
                System.out.println("El total a pagar es: " + total6);
                break;
            case 7:
                var descuento7 = precioCompra * 0.05;
                var total7 = precioCompra - descuento7;
                System.out.println("El total a pagar es: " + total7);
                break;
        }
        ingreso.close(); */

        // Estructura Ciclica While

/*         System.out.println("Total de productos comprados: ");
        int totalProductos, cantidadProducto, valorProducto;
        totalProductos = ingreso.nextInt();
        var i = 0;
        var totalFactura = 0;
        while (i < totalProductos) {
            System.out.println("Cantidad del producto " + (i + 1) + ":");
            cantidadProducto = ingreso.nextInt();
            System.out.println("Valor del producto " + (i + 1) + ":");
            valorProducto = ingreso.nextInt();
            var valor = (valorProducto * cantidadProducto);
            totalFactura += valor;
            i += 1;
        }
        System.out.println("Total factura: $" + totalFactura);
        ingreso.close(); */

        // Do While

/*         System.out.println("Total de productos comprados: ");
        int totalProductos, cantidadProducto, valorProducto;
        totalProductos = ingreso.nextInt();
        var i = 0;
        var totalFactura = 0;
        do {
            System.out.println("Cantidad del producto " + (i + 1) + ":");
            cantidadProducto = ingreso.nextInt();
            System.out.println("Valor del producto " + (i + 1) + ":");
            valorProducto = ingreso.nextInt();
            var valor = (valorProducto * cantidadProducto);
            totalFactura += valor;
            i += 1;
        } while (i < totalProductos);
        System.out.println("Total factura: $" + totalFactura);
        ingreso.close(); */

        // Integracion estructuras condicionales y ciclicas (while if-else) (for if-else)

        System.out.println("Cantidad de clientes: ");
        int clientes, totalProductos, cantidadProducto, valorProducto;
        clientes = ingreso.nextInt();
        var i = 0;
        var totalFactura = 0;
        var valorFacturas = 0;
        for (int j = 0; j < clientes; j++) {
            System.out.println("Cliente " + (j + 1));
            System.out.println("Total de productos comprados: ");
            totalProductos = ingreso.nextInt();
            i = 0;
            totalFactura = 0;
            while (i < totalProductos) {
                System.out.println("Cantidad del producto " + (i + 1) + ":");
                cantidadProducto = ingreso.nextInt();
                System.out.println("Valor del producto " + (i + 1) + ":");
                valorProducto = ingreso.nextInt();
                var valor = (valorProducto * cantidadProducto);
                totalFactura += valor;
                valorFacturas += valor;
                i += 1;
            }
            System.out.println("Total factura " + (j + 1) + ": $" + totalFactura);
        }
        System.out.println("Total comprado: $" + valorFacturas);
        ingreso.close();
    }
}