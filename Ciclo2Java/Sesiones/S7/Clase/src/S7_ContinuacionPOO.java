import java.util.Scanner;
public class S7_ContinuacionPOO {
    public static void main(String[] args) throws Exception {
        S7_Producto[] productos = new S7_Producto[100];
        Scanner input = new Scanner(System.in);

        System.out.println("Digite la cantidad de productos a ingresar");
        int n = input.nextInt();
        String productos_a_pedir = "";
        input.nextLine();
        for(int i = 0; i<n; i++){
            System.out.println("Ingrese en una sóla línea y separados por espacios los datos");
            //input.nextLine();
            String linea[] = input.nextLine().split(" ");
            //String linea[] = input.nextLine().split(" ");
            /*
            System.out.println("Digite el código del producto");
            int cod = input.nextInt();
            System.out.println("Digite el precio del producto");
            int precio = input.nextInt();       
            System.out.println("Digite la cantidad en bodega del producto");
            int cantidadB = input.nextInt();
            System.out.println("Digite la cantidad mínima del producto");
            int cantidadMin = input.nextInt();
            */
            
            //productos[i] = new Producto(Integer.parseInt(input.next()), Integer.parseInt(input.next()), Integer.parseInt(input.next()), Integer.parseInt(input.next()));
            productos[i] = new S7_Producto(Integer.parseInt(linea[0]), Integer.parseInt(linea[1]), Integer.parseInt(linea[2]), Integer.parseInt(linea[3]));

            //productos[i] = new Producto(cod, precio, cantidadB, cantidadMin);
            if(productos[i].solicitar()){
                //System.out.println("Alerta generada para el código " + productos[i].getCodigo());
                productos_a_pedir = productos_a_pedir + ", "+productos[i].getCodigo();
            }
        }
        System.out.println("Los productos a pedir: "+productos_a_pedir);
        
        int codigo, cantidadProductosComprar;
        System.out.println("Digite el producto");
        codigo = input.nextInt();
        System.out.println("Digite la cantidad a Comprar");
        cantidadProductosComprar = input.nextInt();
        //Buscar producto en el array
        for(int i = 0; i<n; i++){
            if(productos[i].getCodigo() == codigo){
                System.out.println(productos[i].CalcularTotalPagar(cantidadProductosComprar));
            }
        }
        

        //Cambiar la cantidad mínima requerida
        System.out.println("Digite el producto");
        codigo = input.nextInt();
        
        //int cantidadMinima = input.nextInt();
        boolean existeProducto = false;
        for(int i = 0; i<n; i++){
            if(productos[i].getCodigo() == codigo){
                System.out.println("Digite la cantidad  mínima");
                productos[i].setcMinRequerida(input.nextInt());
                System.out.println("El productos "+codigo+" se modificó");
                existeProducto = true;
                break; // Romper ciclo en el caso de que encuentre el producto
            }
        }

        if(existeProducto == false){
            System.out.println("El productos "+codigo+" no existe");
        }

        /*Cast
        */
        /*
        System.out.println("Cast");
        int a = 7;
        float b = 4.56f;
        //Coversión
        a = (int) b;   //Cast explícito
        System.out.println(a);
        b = a; //Cast explícito
        System.out.println(b);

        double d = 20.5;
        long l = (long) d;
        System.out.println(l);

        l = 40000;
        short s;
        s = (short) l;
        System.out.println(s);
        */
        


        
        /*
        int precio;
        System.out.println("HEjemplo Encapsulamiento");

       
        //Crear un objeto de la clase Producto
        Producto p1 = new Producto(7,1000,100,10); // Creación del objeto
        //Imprimir el código del objeto p1
        System.out.println(p1.getCodigo());
        System.out.println(p1.getpCompra());
        System.out.println("Ingrese el precio");
        precio = input.nextInt();
        p1.setpCompra(precio);
        System.out.println("El precio para el producto: "+p1.getCodigo()+"es:"+p1.getpCompra());
        */
        input.close();  //
     }
}