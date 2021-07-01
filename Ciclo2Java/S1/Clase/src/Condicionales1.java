// Un hombre desea saber cuánto dinero se genera por concepto de intereses sobre la cantidad 
// que tiene en inversión en el banco.  Él decidirá reinvertir los intereses siempre 
// y cuando éstos excedan a $7000,y en ese caso desea saber cuánto dinero tendrá finalmente 
// en su cuenta.

import java.util.Scanner;
public class Condicionales1 {
    public static void main(String[] args) throws Exception {
        Scanner ingreso = new Scanner(System.in);
        double cap, interes, pint;
        System.out.println("Digite el capital, $: ");
        cap= ingreso.nextDouble();
        System.out.println("Digite el interes, %: ");
        pint = ingreso.nextDouble();
        interes = cap * (pint/100);
        if (interes > 7000){
            cap = cap + interes;
        }
        System.out.println("El capital es de $: " + cap);
        ingreso.close();
    }
}