import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.control.PasswordField;
import javafx.scene.control.TextField;
import javafx.fxml.FXMLLoader;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.stage.Stage;
import java.io.IOException;
import javafx.scene.control.Alert;


public class S15_LogInController {

    @FXML
    private PasswordField password;

    @FXML
    private TextField username;

    @FXML
    private Button loginButton;

    @FXML
    private Label MensajeError;

    @FXML
    void login(ActionEvent event) throws IOException {
        String UserName = username.getText();//obtener el valor del id usuario
        String Password = password.getText();//""        ""      ""    password
        String error = "";

        if (UserName.equalsIgnoreCase("Prueba") || UserName.contains("prueba")){
            error = "Usuario no valido";
        }

        else if (UserName.isEmpty() || Password.isEmpty()){
            error = "No pueden haber campos vacios";
        }

        else if (Password.length() < 6){
            error = "La contraseña debe tener por lo menos 6 caracteres";
        }

        else if (Password.equalsIgnoreCase(UserName)){
            error = "Tu contraseña no debe contener tu nombre de usuario";
        }

        if (error.isEmpty()){
            FXMLLoader vistaInicio = new FXMLLoader(getClass().getResource("Vista/S15_inicio.fxml"));
            Parent root = vistaInicio.load();
            S15_InicioController driver = vistaInicio.getController();
            Scene scene = new Scene(root);
            Stage stage = new Stage();
            stage.setTitle(UserName);
            stage.setScene(scene);
            stage.show();
        }

        else{
            MensajeError.setText(error);
//con alert
            Alert alert = new Alert(Alert.AlertType.ERROR);
            alert.setHeaderText(null);
            alert.setTitle("Error");
            alert.setContentText(error);
            alert.showAndWait(); 
        }


    }

}
