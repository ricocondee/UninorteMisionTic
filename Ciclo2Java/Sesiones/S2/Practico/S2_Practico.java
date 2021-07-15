import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class S2_Practico {
    public static void main(String[] args) throws Exception {
        Scanner input = new Scanner(System.in);
        System.out.println("¿Cuantos productos va a ingresar?");
        var lenArrays = input.nextInt();
        int codigoProducto[] = new int[lenArrays];
        int cantidadBodega[] = new int[lenArrays];
        int cantidadMinima[] = new int[lenArrays];
        int c;

        System.out.println("Ingresa los codigos de productos");
        for (c = 0; c < codigoProducto.length; c++) {
            System.out.printf("Introduce el codigo %d: ", c + 1);
            codigoProducto[c] = input.nextInt();
        }

        System.out.println("Ingresa las cantidades de productos");
        for (c = 0; c < cantidadBodega.length; c++) {
            System.out.printf("Introduce la cantidad del producto %d: ", c + 1);
            cantidadBodega[c] = input.nextInt();
        }

        System.out.println("Ingresa las cantidades minimas requeridas");
        for (c = 0; c < cantidadMinima.length; c++) {
            System.out.printf("Introduce la cantidad minima del producto %d: ", c + 1);
            cantidadMinima[c] = input.nextInt();
        }

        System.out.println("Ingresa el codigo del producto.");
        var codigo = input.nextInt();
        int r;
        for(r = 0; r < lenArrays; r++){
            if (codigo == codigoProducto[r]) {
                System.out.println("Cantidad del producto en bodega es de: " + cantidadBodega[r] + " unidades");
                System.out.println("Cantidad minima requerida es de: " + cantidadMinima[r] + " unidades");
                if (cantidadMinima[r] > cantidadBodega[r]) {
                    System.out.println("Se deben pedir: " + (cantidadMinima[r] - cantidadBodega[r]) + " unidades");
                } else {
                    System.out.println("Se deben vender minimo: " + (cantidadBodega[r] - cantidadMinima[r]) + " unidades");
                }
            } 
        }

        Map<Integer, Integer> dic = new HashMap<Integer, Integer>();

        // cantidad de producto / codigo de producto
        var cantProducto = input.nextInt();
        var diccCodigo = input.nextInt();
        System.out.println("Ingresa los codigos de productos");
        for (c = 0; c < lenArrays; c++) {
            System.out.printf("Introduce el codigo %d: ", c + 1);
            dic.put(cantProducto, diccCodigo);
        }


        var max = Integer.MIN_VALUE;
        var min = Integer.MAX_VALUE;
        var minCodigo = 0;
        var maxCodigo = 0;

        for (int j : cantidadBodega) {
            if (j > max) {
                max = j;
                maxCodigo = dic.get(max);
            }

        }
        System.out.println("Codigo con mayor numero de unidades: " + maxCodigo);
        for (int k : cantidadBodega) {
            if (k < min) {
                min = k;
                minCodigo = dic.get(min);
            }
        }
        System.out.println("Codigo con menor numero de unidades: " + minCodigo);
        input.close();
    }
}