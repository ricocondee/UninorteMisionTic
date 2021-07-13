package Ciclo2Java.Sesiones.S3.Clase.src;

//introduccion a matrices
import java.util.Scanner;
public class Matrices {
    public static void main(String[] args) throws Exception {
        System.out.println("Introducción a Arrays bidimensional");
        int numeros[][] = new int[2][2]; //Declaración de un array bidimensional de 2x2

        //Lectura de los elementos del array bidimensional
        for(int i = 0; i < 2; i++){
            for(int j=0; j < 2; j++){
                numeros[i][j] = 3;
            }
        }

        //Impresión de los elementos del array bidimensional
        for(int i = 0; i < 2; i++){
            for(int j=0; j < 2; j++){
                System.out.println("numeros["+i+"]["+j+"]"+numeros[i][j]);
            }
        }

        String[][] matriz = new String[3][2];
        for (int i = 0; i < 3; i++){ //Recorrido por filas			               
            for (int j = 0; j < 2; j++){
                System.out.println("matriz["+i+"]["+j+"]"+matriz[i][j]);
            }
        }

        //Recorrido por columnas
        for (int j = 0; j < 2; j++){ //Recorrido por filas			               
            for (int i = 0; i < 3; i++){
                System.out.println("matriz["+i+"]["+j+"]"+matriz[i][j]);
            }
        }


        System.out.println("Ejemplo Matriz String");
        //Llenar una matriz de M*N de datos núméricos
        //que deben ser almacenados como string.
        Scanner input = new Scanner(System.in);
        int M = 0, N =0, i, j;
        double suma = 0;
        
        
        while(M < 1 || N<1){ //Validar que no se ingresen tamaños negativos
            System.out.println("Ingrese el número de filas");
            M = input.nextInt();

            System.out.println("Ingrese el número de columnas");
            N = input.nextInt();
        }

        String[][] matriz_numeros = new String[M][N];

        //leer datos numéricos y almacenarlos como string
        for(i=0; i<M; i++){
            for(j=0; j<N; j++){
                System.out.println("Ingrese número");
                matriz_numeros[i][j] = input.next();
            }
        }

        //Sumar todos los valores de la matriz y mostrar el resultado
        //Recorrido por filas
        for(i=0; i<M; i++){
            for(j=0; j<N; j++){
                suma = suma + Double.parseDouble(matriz_numeros[i][j]); //Suma de los valores de la matriz
            }
        }

        System.out.println("El resultado de la suma de la matriz es: "+suma);
    }
}