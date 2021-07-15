public class S5_Producto {
    // definicion de atributos
    private int codigo;
    private int precioCompra;
    private int cantidadBodega;
    private int cantidadMinima;

    // definicion de constructores
    public S5_Producto(){

    }
            //se puede usar solo un atributo en el constructor
    public S5_Producto(int codigo, int precioCompra, int cantidadBodega, int cantidadMinima){
        this.codigo = codigo;
        this.precioCompra = precioCompra;
        this.cantidadBodega = cantidadBodega;
        this.cantidadMinima = cantidadMinima;
    }

    // metodo Set
    //Set para asignar valores a cada atributo
    public void setCodigo(int codigo){
        this.codigo = codigo;
    }

    public void setPrecioCompra(int precioCompra){
        if (precioCompra > 1000){
            System.out.println("El precio no se puede aumentar a el actual");
        }
        else{
            this.precioCompra = precioCompra;
            System.out.println("El precio se modifico correctamente, el nuevo precio es: " + precioCompra);
        }
    }

    public void setCantidadBodega(int cantidadBodega){
        this.cantidadBodega = cantidadBodega;
    }

    public void setCantidadMinima(int cantidadMinima){
        this.cantidadMinima = cantidadMinima;
    }

    // metodo Get
    //Get para obtener valores de un atributo encapsulado o private
    public int getCodigo(){
        return codigo;
    }

    public int getPrecioCompra(){
        return precioCompra;
    }

    public int getCantidadBodega(){ 
        return cantidadBodega;
    }

    public int getCantidadMinima(){
        return cantidadMinima;
    }
}
