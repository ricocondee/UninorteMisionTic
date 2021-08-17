/* Reto 2 Uninorte, Mision tic 2022
Realizado por Emanuel Rico Conde @ricocondee
ID de estudiante: 200171465 */

import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class R2_SchoolGradingSystem {
    private int Examenes;
    private String genero[] = { "m", "f" };
    private String lineaMatriz[];
    private double matriz[][];
    private int deficiente = 0;
    private double si = 0, no = 0;
    private int siF = 0, siM = 0, noM = 0, noF = 0;
    private String m, f, generoMejor;
    private String destacadoMath = "";
    private Map<Double, String>  dic = new HashMap<Double, String>();
        

    public R2_SchoolGradingSystem() {
        matriz = new double[18][4];
    }

    public void readData() {
        Scanner input = new Scanner(System.in);
        Examenes = Integer.parseInt(input.nextLine());

        for (int i = 0; i < Examenes; i++) {
            lineaMatriz = input.nextLine().split(" ");
            //System.out.println(Arrays.toString(lineaMatriz));
            //System.out.println(i);
            for (int j = 0; j < 4; j++) {
                //System.out.println(j);
                //System.out.println((lineaMatriz[j]));
                matriz[i][j] = Double.parseDouble(lineaMatriz[j]);
            }
        }
        
        input.close();
    }

    public double question1() {
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
        var porcentaje = si / Examenes;
        return porcentaje;

    }

    public int question2() {
        return deficiente;
    }

    public String question3(){
        if (siM > siF) {
            m = genero[0];
            generoMejor = m;
        } 
        else if (siM < siF) {
            f = genero[1];
            generoMejor = f;
        }
        return generoMejor;
    }

    public String question4() {
        dic.put(1.0, "armando");
        dic.put(2.0, "nicolas");
        dic.put(3.0, "daniel");
        dic.put(4.0, "maria");
        dic.put(5.0, "marcela");
        dic.put(6.0, "alexandra");
        double test = matriz[0][0], test2 = matriz[0][0];

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
        return destacadoMath;

    }

    /* public double[][] getmatriz() {
        return matriz;
    }

    public void setmatriz(double[][] matriz) {
        this.matriz = matriz;
    } */

}