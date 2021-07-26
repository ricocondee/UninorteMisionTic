//import otros.S8_Ejemplo2;//importa un archivo especifico de
import paquetes.*;
public class S8_otraClase{
    public static void main(String args[]){
        System.out.println(S8_Ejemplo2.atributo);
        S8_Ejemplo2.metodo();
        S8_Producto p1 = new S8_Producto(); // crea un objeto con valores predeterminados
        System.out.println(p1.getCodigo());

    }
}