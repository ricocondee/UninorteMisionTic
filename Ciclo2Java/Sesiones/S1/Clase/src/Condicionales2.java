import java.util.Scanner;
public class Condicionales2 {
    public static void main(String[] args) throws Exception {
        Scanner ingreso = new Scanner(System.in);
        int ht, he, salario;
        System.out.println("Hora trabajadas: ");
        ht =  ingreso.nextInt();
        if (ht > 40){
            he = ht - 40;
            salario = (he * 20) + (40 * 16);
        }
        else{
            salario = ht * 16;
        }
        System.out.println("El salario semanal es de: $"+ salario);
        ingreso.close();
    }
}