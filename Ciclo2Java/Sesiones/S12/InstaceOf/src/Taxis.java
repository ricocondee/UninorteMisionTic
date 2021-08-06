class Taxis extends Vehiculos {
    public static void Verificacion(Vehiculos a){
        if (a instanceof Taxis){
            ((Taxis)a).Potencia();
        }
        else{
            System.out.println("No es una instancia de Taxi");
        }
    }

    public void Potencia() {
        System.out.println("100");
    }
}
