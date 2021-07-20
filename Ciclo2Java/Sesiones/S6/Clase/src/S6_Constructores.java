/*class MiClase {
   int x;
   MiClase(){
       x=10;
   }
}
class ConstructorDemo {
   public static void main(String[] args) {
      MiClase t1= new MiClase();
      MiClase t2= new MiClase();
       System.out.println(t1.x + " - "+t2.x);
      t2.x  = 45;
      System.out.println(t1.x + " - "+t2.x);
   }
}

*/
class Universidad {
    public static void main(String[] args) {
        // Instanciar un objeto de la clase Estudiante
        String nombre = "Maria";
        float nota1 = 4;
        float nota2 = 3.4f;
        float nota3 = 2;
        Estudiante e1 = new Estudiante(nombre, nota1, nota2, nota3);
        System.out.println(e1.getNombre());
        e1.setNombre("Juan");
        System.out.println(e1.getNombre() + " El promedio es: " + e1.Promediar());
        double maximo = Math.max(67, 42);
        System.out.println("maximo: " + maximo);
        double raizc = Math.sqrt(729);
        System.out.println("raiz cuadrada: " + raizc);
    }
}
