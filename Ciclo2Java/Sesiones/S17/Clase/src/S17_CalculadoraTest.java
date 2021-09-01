import static org.junit.Assert.fail;
import static org.junit.jupiter.api.Assertions.assertEquals;
import org.junit.Test;

public class S17_CalculadoraTest {
    @Test
    public void testSuma() {
        System.out.println("suma");
        int numero1 = 4;
        int numero2 = 3;

        int resultadoExperado = 7;
        int resultadoObtenido = S17_Calculadora.suma(numero1, numero2);

        assertEquals(resultadoExperado, resultadoObtenido);

        if (resultadoExperado != resultadoObtenido) {
            fail("La prueba falló");
        }
    }

    @Test
    public void testResta() {
        System.out.println("resta");
        int numero1 = 4;
        int numero2 = 3;

        int resultadoExperado = 4;
        int resultadoObtenido = S17_Calculadora.resta(numero1, numero2);

        assertEquals(resultadoExperado, resultadoObtenido);
    }
}
