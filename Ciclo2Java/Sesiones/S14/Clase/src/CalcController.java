import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.scene.Node;
import javafx.scene.control.Button;
import javafx.scene.control.TextField;

public class CalcController {
    private double operando = 0;
    private String operador = null;
    private double total = 0;

    @FXML
    private TextField resultText;

    @FXML
    private Button Button7;

    @FXML
    private Button Button8;

    @FXML
    private Button Button9;

    @FXML
    private Button Button4;

    @FXML
    private Button Button1;

    @FXML
    private Button Button5;

    @FXML
    private Button Button2;

    @FXML
    private Button Button6;

    @FXML
    private Button Button3;

    @FXML
    private Button Button0;

    @FXML
    private Button ButtonLimpiar;

    @FXML
    private Button ButtonCalcular;

    @FXML
    private Button ButtonSuma;

    @FXML
    private Button ButtonResta;

    @FXML
    private Button ButtonMultiplicacion;

    @FXML
    private Button ButtonDivision;

    @FXML
    void addNumber(ActionEvent event) {
        Node node = (Node) event.getSource();
        String data = (String) node.getUserData();//Obtener el valor de la caja de texto
        if(resultText.getText().equals("0")){
            resultText.setText(data);
        }
        else{
            resultText.setText(resultText.getText() + data);
        }
    }

    @FXML
    void addOperator(ActionEvent event) {
        Node node = (Node) event.getSource();
        String data = (String) node.getUserData();//Obtener el valor de la caja de texto
        operando = Integer.parseInt(resultText.getText());

        if(operador !=null){
            switch(operador){
                case "+":
                    total += Integer.parseInt(resultText.getText());
                break;
                case "-":
                    total -= Integer.parseInt(resultText.getText());
                break;

                default:

                break;
            }
        }
        else{
            total = operando;
        }
        operador = data;
        resultText.setText("0");
    }

    @FXML
    void clean(ActionEvent event) {
        resultText.setText("0");
        total = 0;
        operando = 0;
        operador = null;
    }

    @FXML
    void calcular(ActionEvent event) {
        int numero = Integer.parseInt(resultText.getText());
        switch(operador){
            case "+":
                total += numero;
            break;
            case "-":
                total -= numero;
            break;

            case "*":
                total *= numero;
            break;

            case "/":
                total /= numero;
            break;

            default:
                total = numero;
            break;

        }
        resultText.setText(Double.toString(total));
        operador = null;
    }

}
