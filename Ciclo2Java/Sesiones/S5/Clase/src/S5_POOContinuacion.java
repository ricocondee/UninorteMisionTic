import java.util.Scanner;

public class S5_POOContinuacion {
    public static void main(String[] args) throws Exception {
        System.out.println("Ejemplo de encapsulamiento\n");
        Scanner input = new Scanner(System.in);

        // crear un objeto de la clase Producto
        S5_Producto p1 = new S5_Producto(7, 1000, 50, 10); // creacion del objeto
        // Impresion del codigo del Producto
        System.out.println("Codigo de producto: " + p1.getCodigo());
        System.out.println("Precio actual del producto: " + p1.getPrecioCompra());
        System.out.println("Quiere actualizar el precio? (si/no)");
        String validar;
        validar = input.nextLine();
        if(validar.equals("si")){
            System.out.println("Ingrese el precio nuevo");
            var precio = input.nextInt();
            p1.setPrecioCompra(precio);
            System.out.println("Cantidad en bodega: " + p1.getCantidadBodega());
            System.out.println("Cantidad minima requerida: " + p1.getCantidadMinima());
        }
        else{
            System.out.println("Cantidad en bodega: " + p1.getCantidadBodega());
            System.out.println("Cantidad minima requerida: " + p1.getCantidadMinima());
            System.out.println(validar);
        }
        input.close();

        // se pudo haber creado la clase producto dentro de este mismo archivo pero se
        // recomienda hacerlo en archivos diferentes como buenas practicas
    }
}
