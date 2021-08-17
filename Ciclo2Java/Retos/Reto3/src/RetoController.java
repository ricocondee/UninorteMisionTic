/* Reto 3 Uninorte, Mision tic 2022
Realizado por Emanuel Rico Conde @ricocondee
ID de estudiante: 200171465 */

import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.scene.control.Button;
import javafx.scene.control.TextArea;
import javafx.scene.control.TextField;

public class RetoController {

    @FXML
    private TextField ExamsQuantity;

    @FXML
    private TextArea TotalRecords;

    @FXML
    private TextArea OutPutResults;

    @FXML
    private Button SendButton;

    @FXML
    void Calculate(ActionEvent event) {
        String exams = ExamsQuantity.getText();
        String records = TotalRecords.getText();
        R3_SchoolGradingSystem reto3G = new R3_SchoolGradingSystem();
        reto3G.loadData(exams, records);
        String results = String.format("%.2f\n%d\n%s\n%s",reto3G.stat1(),reto3G.stat2(),reto3G.stat3(),reto3G.stat4());
        OutPutResults.setText(results);
    }

}
