/* Reto 2 Uninorte, Mision tic 2022
Realizado por Emanuel Rico Conde @ricocondee
ID de estudiante: 200171465 */

public class Reto2 {
    public static void main(String[] args) throws Exception {
        R2_SchoolGradingSystem reto2 = new R2_SchoolGradingSystem(); reto2.readData();
        System.out.printf("%.2f\n", reto2.question1());
        System.out.println(reto2.question2());
        System.out.println(reto2.question3());  
        System.out.println(reto2.question4());
    }
}
