public class S7_Producto {
    //Definir atributos
    private int codigo;
    private int pCompra;
    private int cBodega;
    private int cMinRequerida;
    private int cMaxPermitida;
    private final float descuento = 0.01f;

    //Definir los constructores
    public S7_Producto(){

    }

    public S7_Producto(int codigo, int pCompra, int cBodega, int cMinRequerida){
        this.codigo = codigo;
        this.pCompra = pCompra;
        this.cBodega = cBodega;
        this.cMinRequerida = cMinRequerida;
        this.cMaxPermitida = 2000;
    }
    
    //Constructor con un solo parámetro
    public S7_Producto(int codigo ){
        this.codigo = codigo;
    }

    //Métodos Set: Asignar valores a cada atributo
    public void setCodigo(int codigo){ //Asignar al atributo codigo un valor
        this.codigo = codigo;
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

    public int getpCompra(){
        return pCompra;
    }

    public int getcBodega(){
        return cBodega;
    }

    public int getcMinRequerida(){
        return cMinRequerida;
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
}
