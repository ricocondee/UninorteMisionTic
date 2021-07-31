public class Prenda extends Producto{
    private String talla;
    private boolean planchado;

    //Constructor Vacio
    public Prenda(){

    }

    //Constructor cuando hay herencia
    public Prenda(int codigo, String descripcion, int pCompra, int pVenta, int cBodega, int cMinRequerida, String talla, boolean planchado){
        super(codigo, descripcion, pCompra, pVenta, cBodega, cMinRequerida);
        this.talla = talla;
        this.planchado = planchado;
    }

    public void setTalla(String talla){
        this.talla = talla;
    }

    public void setPlanchado(boolean planchado){
        this.planchado = planchado;
    }

    public String getTalla(){
        return talla;
    }

    public boolean getPlanchado(){
        return planchado;
    }

    public void Mostrar(){
        super.Mostrar();
        System.out.println("-"+talla+"-"+planchado);
        /*System.out.println(getCodigo()+"-"+getDescripcion()+"-"+getpCompra()+"-"+getpVenta()+"-"+getcBodega()+
        "-"+getcMinRequerida()+"-"+getcMaxPermitida()+"-"+talla+"-"+planchado);
        */
        
       
    }
}