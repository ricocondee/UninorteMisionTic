public class Producto {
    //Definir atributos
    private int codigo;
    private String descripcion;
    private int pCompra;
    private int pVenta;
    private int cBodega;
    private int cMinRequerida;
    private int cMaxPermitida;
    private final float descuento = 0.01f;

    //Definir los constructores
    public Producto(){

    }

    public Producto(int codigo, String descripcion, int pCompra, int pVenta, int cBodega, int cMinRequerida){
        this.codigo = codigo;
        this.descripcion = descripcion;
        this.pCompra = pCompra;
        this.pVenta = pVenta;
        this.cBodega = cBodega;
        this.cMinRequerida = cMinRequerida;
        this.cMaxPermitida = 2000;
    }
    
    //Constructor con un solo parámetro
    public Producto(int codigo ){
        this.codigo = codigo;
    }

    //Métodos Set: Asignar valores a cada atributo
    public void setCodigo(int codigo){ //Asignar al atributo codigo un valor
        this.codigo = codigo;
    }

    public void setDescripcion(String descripcion){
        this.descripcion = descripcion;
    }

    public void setpCompra(int pCompra){
        
        if(pCompra > 10000){
            System.out.println("El precio no se puede modificar");
        }
        else
        {
            this.pCompra = pCompra;
            System.out.println("El preciose modificó correctamente"+this.pCompra);
        }
    }

    public void setpVenta(int pVenta){
        this.pVenta = pVenta;
    }

    public void setcBodega(int cBodega){
        this.cBodega = cBodega;
    }

    public void setcMinRequerida(int cMinRequerida){
        if(cMinRequerida < 0){
            this.cMinRequerida = 0;
        }
        else{
            this.cMinRequerida = cMinRequerida;
        }
    }

    //Método get: Se emplea para obtener el dato de un tributo
    public int getCodigo(){
        return codigo;
    }

    public String getDescripcion(){
        return descripcion;
    }

    public int getpCompra(){
        return pCompra;
    }

    public int getpVenta(){
        return pVenta;
    }

    public int getcBodega(){
        return cBodega;
    }

    public int getcMinRequerida(){
        return cMinRequerida;
    }

    public int getcMaxPermitida(){
        return cMaxPermitida;
    }

    public boolean solicitar(){
        if(cBodega < cMinRequerida){
            return true;
        }
        else{
            return false;
        }
    }

    public float CalcularTotalPagar(int CantidadUnidadesCompra){
        return ((pCompra * CantidadUnidadesCompra)-(pCompra * CantidadUnidadesCompra*descuento));
        //100*10 - (100*10*0.01) = 1000-10; = 990;
    }

    public double CalcularValorFacturaConDescuento(int TotalVentasSinDescuento){
        return ((TotalVentasSinDescuento)-(TotalVentasSinDescuento*descuento));
    }

    public void Mostrar(){
        System.out.print(codigo+"-"+descripcion+"-"+pCompra+"-"+pVenta+cBodega+
        "-"+cMinRequerida+"-"+cMaxPermitida);
    }
}