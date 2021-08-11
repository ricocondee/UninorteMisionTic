import javafx.application.Application;
import javafx.fxml.FXMLLoader;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.stage.Stage;

public class App extends Application {
    @Override
    public void start(Stage primaryStage) throws Exception {
        // FXMLLoader fxmlLoader = new
        // FXMLLoader(getClass().getResource("ruta absoluta
        // del archivo fxml a mostrar"));
        FXMLLoader calc = new FXMLLoader(getClass().getResource("calculadora.fxml"));
        Parent root = calc.load();
        Scene scene = new Scene(root);

        primaryStage.setTitle("Calculadora");
        primaryStage.setScene(scene);
        primaryStage.show();
    }

    public static void main(String[] args) {
        launch(args);
    }
}