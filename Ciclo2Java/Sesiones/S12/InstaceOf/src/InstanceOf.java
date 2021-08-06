public class InstanceOf {
    public static void main(String[] args) throws Exception {
        Taxis taxi1 = new Taxis();
        if (taxi1 instanceof Vehiculos) {
            System.out.println("Taxi es un taxi y tambien un vehiculo");
        }

        Vehiculos taxi2 = new Taxis();
            Taxis.Verificacion(taxi2);
    }
}
