/* Reto 3 Uninorte, Mision tic 2022
Realizado por Emanuel Rico Conde @ricocondee
ID de estudiante: 200171465 */

import javafx.application.Application;
import javafx.fxml.FXMLLoader;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.stage.Stage;

public class Reto3 extends Application {
    public static void main(String[] args) throws Exception {
        /* SchoolGradingSystem reto3 = new SchoolGradingSystem(); reto3.loadData();
        System.out.printf("%.2f\n", reto3.stat1());
        System.out.println(reto3.stat2());
        System.out.println(reto3.stat3());  
        System.out.println(reto3.stat4()); */
        launch(args);
    }

    @Override
    public void start(Stage Reto3Stage) throws Exception {
        FXMLLoader GUI = new FXMLLoader(getClass().getResource("GUIreto3.fxml"));
        Parent root = GUI.load();
        Scene frame = new Scene(root);
        Reto3Stage.setTitle("Reto 3 GUI");
        Reto3Stage.setScene(frame);
        Reto3Stage.show();
        
    }
}