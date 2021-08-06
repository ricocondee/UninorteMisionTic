public class Taxi implements Vehiculo {
    int velocidad = 0;

    @Override
    public String frenar(int cuanto) {
        velocidad -= cuanto;
        return velocidad + "km/hora";
    }

    @Override // indica que el metodo esta siendo sobreescrito
    public String acelerar(int cuanto) {
        String cadena = "";
        velocidad += cuanto;
        if (velocidad > VelocidadMaxima)
            cadena = "Exceso de velocidad";
        cadena += "El taxi ha acelerado a " + velocidad + "km/hora";
        return cadena;
    }
}