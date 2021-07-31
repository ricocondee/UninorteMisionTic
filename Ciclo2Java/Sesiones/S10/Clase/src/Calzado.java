public class Calzado extends Producto{
    private int talla;

    //Constructor Vacio
    public Calzado(){

    }

    //Constructor cuando hay herencia
    public Calzado(int codigo, String descripcion, int pCompra, int pVenta, int cBodega, int cMinRequerida, int talla){
        super(codigo, descripcion, pCompra, pVenta, cBodega, cMinRequerida);
        this.talla = talla;
    }
    public void setTalla(int talla){
        this.talla = talla;
    }

    public int getTalla(){
        return talla;
    }

    public void Mostrar(){
        System.out.println(getCodigo()+"-"+getDescripcion()+"-"+getpCompra()+"-"+getpVenta()+"-"+getcBodega()+
        "-"+getcMinRequerida()+"-"+getcMaxPermitida()+"-"+talla);
    }
}