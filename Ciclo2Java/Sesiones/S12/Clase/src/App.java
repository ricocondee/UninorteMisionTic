class Main {
    public static void main(String[] args) {
        Taxi myTaxi = new Taxi();// instanciando un objeto
        String frenar = myTaxi.frenar(4);
        String acelerar = myTaxi.acelerar(10);
        System.out.println(frenar);

        System.out.println(acelerar);
    }
}
