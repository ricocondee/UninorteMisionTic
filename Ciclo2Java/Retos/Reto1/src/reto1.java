/* Reto 1 Uninorte, Mision tic 2022
Realizado por Emanuel Rico Conde @ricocondee
ID de estudiante: 200171465 */

import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class reto1 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int Examenes = Integer.parseInt(input.nextLine());
        Map<Double, String> dic = new HashMap<Double, String>();
        dic.put(1.0, "armando");
        dic.put(2.0, "nicolas");
        dic.put(3.0, "daniel");
        dic.put(4.0, "maria");
        dic.put(5.0, "marcela");
        dic.put(6.0, "alexandra");
        
        double matriz[][] = new double[Examenes][4];
        double si = 0, no = 0;
        double test = matriz[0][0], test2 = matriz[0][0];
        String genero[] = { "m", "f" };
        String destacadoMath = "";
        String m, f;
        int siM = 0, noM = 0, siF = 0, noF = 0;
        var deficiente = 0;

        for (int i = 0; i < Examenes; i++) {
            String linea[] = input.nextLine().split(" ");
            for (int j = 0; j < 4; j++) {
                matriz[i][j] = Double.parseDouble(linea[j]);
            }
        }

        for (int i = 0; i < Examenes; i++) {
            if (matriz[i][3] >= 0.0 & matriz[i][3] <= 3.0) {
                no += 1;
                deficiente += 1;
                if (matriz[i][1] == 0.0) {
                    noM += 1;
                } else {
                    noF += 1;
                }
            } else if (matriz[i][3] > 3.0 & matriz[i][3] <= 6.0) {
                no += 1;
                if (matriz[i][1] == 0.0) {
                    noM += 1;
                } else {
                    noF += 1;
                }
            } else if (matriz[i][3] > 6.0 & matriz[i][3] <= 8.0) {
                si += 1;
                if (matriz[i][1] == 0.0) {
                    siM += 1;
                } else {
                    siF += 1;
                }
            } else if (matriz[i][3] > 8.0 & matriz[i][3] <= 9.0) {
                si += 1;
                if (matriz[i][1] == 0.0) {
                    siM += 1;
                } else {
                    siF += 1;
                }
            } else if (matriz[i][3] > 9.0 & matriz[i][3] <= 10.0) {
                si += 1;
                if (matriz[i][1] == 0.0) {
                    siM += 1;
                } else {
                    siF += 1;
                }
            }
        }

        for (int p = 0; p < matriz.length; p++) {
            for (int q = 0; q < matriz[p].length; q++) {
                if (matriz[p][q] > test && matriz[p][3] != 0.0 && matriz[p][2] == 1.0) {
                    test = matriz[p][3];
                    test2 = matriz[p][0];
                }
            }
        }

        for (int i = 0; i < Examenes; i++) {
            if (matriz[i][0] == test2 && matriz[i][2] == 1.0 && matriz[i][3] == test) {
                destacadoMath = dic.get(test2);
            }
        }

        var porcentaje = si / Examenes;
        System.out.printf("%.2f\n", porcentaje);
        System.out.println(deficiente);
        if (siM > siF) {
            m = genero[0];
            System.out.println(m);
        } else if (siM < siF) {
            f = genero[1];
            System.out.println(f);
        }
        System.out.println(destacadoMath);
        input.close();
    }
}