import java.util.Scanner;

public class S10_Practico {
    public static void main(String[] args) throws Exception {
        
        Prenda[] productosP = new Prenda[100]; //Array para las prendas
        Calzado[] productosC = new Calzado[100]; //Array para el calzado
        String prendas_a_pedir = "";
        String calzado_a_pedir = "";

        Scanner leer = new Scanner(System.in);

        System.out.println("Digite la cantidad de prendas a ingresar");
        int np = leer.nextInt(); //Cantidad de prendas que se ingresaron

        System.out.println("Digite la cantidad de calzado a ingresar");
        int nc = leer.nextInt(); //Cantidad de calzado que se ingresaron

        //Ciclo para solicitar las prendas
        leer.nextLine();
        System.out.println("Ingreso de prendas");
        for(int i = 0; i<np; i++){
            System.out.println("Código Descripción PrecioCompra PrecioVenta CantidadBodega CantidadMinima Talla Planchado");
            String[] linea = leer.nextLine().split(" ");
            productosP[i] = new Prenda(Integer.parseInt(linea[0]), linea[1], Integer.parseInt(linea[2]), Integer.parseInt(linea[3]), Integer.parseInt(linea[4]), Integer.parseInt(linea[5]),linea[6], Boolean.parseBoolean(linea[7]));
        }
        
        //Ciclo para solicitar las calzado
        //leer.nextLine();
        System.out.println("Ingreso de calzado");
        for(int i = 0; i<nc; i++){
            System.out.println("Código Descripción PrecioCompra PrecioVenta CantidadBodega CantidadMinima Talla");
            String[] linea = leer.nextLine().split(" ");
            productosC[i] = new Calzado(Integer.parseInt(linea[0]), linea[1], Integer.parseInt(linea[2]), Integer.parseInt(linea[3]), Integer.parseInt(linea[4]), Integer.parseInt(linea[5]),Integer.parseInt(linea[6]));
        }

        int opcion = 0;
        System.out.print("\033[H\033[2J");
        while(opcion!=7){
            System.out.println("Menú opciones");
            System.out.println("Opción 1: Consultar producto");
            System.out.println("Opción 2: Verificar productos a pedir");
            System.out.println("Opción 3: Calzado con mayor cantidad de unidades");
            System.out.println("Opción 4: Prenda con mayor cantidad de unidades");
            System.out.println("Opción 5: Modificar cantidad mínima requerida en bodega");
            System.out.println("Opción 6: Vender producto");
            System.out.println("Opción 7: Salir");
            System.out.println("Digite la opción deseada");
            opcion = leer.nextInt();
            switch(opcion){
                case 1:
                    System.out.println("Digite el código del producto");
                    int codigo_producto = leer.nextInt();
                    System.out.println("Digite el tipo de producto (P: prenda, C: calzado)");
                    leer.nextLine(); 
                    String tipo = leer.nextLine();
                    boolean producto_existe = false;
                    if(tipo.equalsIgnoreCase("P")){
                        for(int i=0; i<np; i++){
                            if(codigo_producto == productosP[i].getCodigo()){
                                productosP[i].Mostrar();
                                producto_existe = true;
                            }
                        }
                    }
                    else if(tipo.equalsIgnoreCase("c")){
                        for(int i=0; i<nc; i++){
                            if(codigo_producto == productosC[i].getCodigo()){
                                productosC[i].Mostrar();
                                producto_existe = true;
                            }
                        }
                    }

                    if(producto_existe == false){
                        System.out.println("El producto: " + codigo_producto+" no existe");
                    }
                break;
                case 2:
                prendas_a_pedir = "";
                calzado_a_pedir = "";
                //Determinar las prendas a solicitar
                for(int i = 0; i<np; i++){     
                    if(productosP[i].solicitar()){
                        prendas_a_pedir = prendas_a_pedir + ", "+productosP[i].getCodigo();
                    }
                }
                System.out.println("Las prendas a pedir: "+prendas_a_pedir);
                
                //Determinar las prendas a solicitar
                for(int i = 0; i<nc; i++){     
                    if(productosC[i].solicitar()){
                        calzado_a_pedir = calzado_a_pedir + ", "+productosC[i].getCodigo();
                    }
                }
                System.out.println("El calzado a pedir: "+calzado_a_pedir);
        
                break;

                case 3:
                    int mayorCantidad = productosC[0].getcBodega();//Capturar la cantidad en bodega del primer objeto
                    int codigoProductoMayorCantidad = productosC[0].getCodigo();
                    for(int i = 0; i<nc; i++){
                        if(mayorCantidad < productosC[i].getcBodega()){
                            mayorCantidad = productosC[i].getcBodega();
                            codigoProductoMayorCantidad = productosC[i].getCodigo();
                        }
                    }
                    System.out.println("El código del calzado con mayor cantidad en bodega es: "+codigoProductoMayorCantidad);
                break;

                case 4:
                    mayorCantidad = productosP[0].getcBodega();//Capturar la cantidad en bodega del primer objeto
                    codigoProductoMayorCantidad = productosP[0].getCodigo();
                    for(int i = 0; i<nc; i++){
                        if(mayorCantidad < productosP[i].getcBodega()){
                            mayorCantidad = productosP[i].getcBodega();
                            codigoProductoMayorCantidad = productosP[i].getCodigo();
                        }
                    }
                    System.out.println("El código de la prenda con mayor cantidad en bodega es: "+codigoProductoMayorCantidad);

                    /*int codigo, cantidadProductosComprar;
                    System.out.println("Digite el producto");
                    codigo = leer.nextInt();
                    System.out.println("Digite la cantidad a Comprar");
                    cantidadProductosComprar = leer.nextInt();
                    //Buscar producto en el array
                    for(int i = 0; i<n; i++){
                        if(productos[i].getCodigo() == codigo){
                            System.out.println(productos[i].CalcularTotalPagar(cantidadProductosComprar));
                        }
                    }
                    */
                break;
                case 5:
                    //Cambiar la cantidad mínima requerida
                    System.out.println("Digite el código del producto");
                    int codigo = leer.nextInt();
                    System.out.println("Digite el tipo de producto (P: prenda, C: calzado)");
                    tipo = leer.next();
                    if(tipo.equalsIgnoreCase("P")){
                        boolean existeProducto = false;
                        for(int i = 0; i<np; i++){
                            if(productosP[i].getCodigo() == codigo){
                                System.out.println("Digite la cantidad  mínima");
                                productosP[i].setcMinRequerida(leer.nextInt());
                                System.out.println("El productos "+codigo+" se modificó");
                                existeProducto = true;
                                break; // Romper ciclo en el caso de que encuentre el producto
                            }
                        }
                        if(existeProducto == false){
                            System.out.println("El productos "+codigo+" no existe");
                        }
                    }
                    else{
                        boolean existeProducto = false;
                        for(int i = 0; i<nc; i++){
                            if(productosC[i].getCodigo() == codigo){
                                System.out.println("Digite la cantidad  mínima");
                                productosC[i].setcMinRequerida(leer.nextInt());
                                System.out.println("El productos "+codigo+" se modificó");
                                existeProducto = true;
                                break; // Romper ciclo en el caso de que encuentre el producto
                            }
                        }
                        if(existeProducto == false){
                            System.out.println("El productos "+codigo+" no existe");
                        }                        
                    }
                break;
                case 6: 
                    System.out.println("Digite el código del producto a vender: ");
                    int codigoProducto = leer.nextInt();
                    System.out.println("Digite el tipo de producto (P: prenda, C: calzado)");
                    tipo = leer.next();
                    System.out.println("Digite la cantidad a vender: ");
                    int cantidadVender = leer.nextInt();
                    producto_existe = false;
                    if(tipo.equalsIgnoreCase("p")){
                        for(int i = 0; i < np; i++){
                            if(productosP[i].getCodigo() == codigoProducto){
                                producto_existe = true;
                                if(cantidadVender <= productosP[i].getcBodega()){
                                    int totalFacturaSinDescuento = cantidadVender * productosP[i].getpVenta();
                                    double totalFacturaConDescuento = productosP[i].CalcularValorFacturaConDescuento(totalFacturaSinDescuento);
                                    System.out.println("Valor Factura sin Descuento: "+totalFacturaSinDescuento);
                                    System.out.println("Valor Factura con Descuento: "+totalFacturaConDescuento);
                                    productosP[i].setcBodega(productosP[i].getcBodega() - cantidadVender);
                                }
                                else{
                                    System.out.println("No se puede realizar la venta. El número de prendas a vender supera la cantidad en bodega");
                                }
                            }
                        }
                    }
                    else{
                        for(int i = 0; i < nc; i++){
                            if(productosC[i].getCodigo() == codigoProducto){
                                producto_existe = true;
                                if(cantidadVender <= productosC[i].getcBodega()){
                                    int totalFacturaSinDescuento = cantidadVender * productosC[i].getpVenta();
                                    double totalFacturaConDescuento = productosC[i].CalcularValorFacturaConDescuento(totalFacturaSinDescuento);
                                    System.out.println("Valor Factura sin Descuento: "+totalFacturaSinDescuento);
                                    System.out.println("Valor Factura con Descuento: "+totalFacturaConDescuento);
                                    productosC[i].setcBodega(productosC[i].getcBodega() - cantidadVender);
                                }
                                else{
                                    System.out.println("No se puede realizar la venta. El número de calzado a vender supera la cantidad en bodega");
                                }
                            }
                        }                        
                    }
                    if(producto_existe == false){
                        System.out.println("El producto no fue encontrado");
                    }
                break;
                case 7:
                    opcion = 7;
                    System.out.println("Gracias por usar el sistema");
                break;
                default:
                    System.out.println("La opción ingresada es incorrecta");
                    //System.out.print("\033[H\033[2J");
                break;
            }
            
        }
        leer.close();  //
    }
}
