/* Reto 3 Uninorte, Mision tic 2022
Realizado por Emanuel Rico Conde @ricocondee
ID de estudiante: 200171465 */

public class R3_SchoolGradingSystem extends GradingSystem {
    
    public R3_SchoolGradingSystem(){

    }
    public void loadData(String exams, String records) {
        Examenes = Integer.parseInt(exams);
        String datos[] = records.split("\n");
        for (int i = 0; i < Examenes; i++) {
            lineaMatriz = datos[i].split(" ");
            for (int j = 0; j < 4; j++) {
                matriz[i][j] = Double.parseDouble(lineaMatriz[j]);
            }
        }
    }
}
