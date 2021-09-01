import javafx.fxml.FXML;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.control.TextField;
import javafx.event.ActionEvent;

import Modelo.Estudiante;
import Modelo.DaoEstudiante;// importar los modelos necearios

public class S19_EstudianteController {

    @FXML
    private TextField documentoEstudiante;

    @FXML
    private Label idEstudiante;

    @FXML
    private TextField nombreEstudiante;

    @FXML
    private TextField apellidoEstudiante;

    @FXML
    private TextField celularEstudiante;

    @FXML
    private Button registrarEstudianteButton;

    @FXML
    private Button consultarEstudianteButton;

    @FXML
    private Button modificarEstudianteButton;

    @FXML
    private Button eliminarEstudianteButton;

    @FXML
    void consultarEstudiante(ActionEvent event) {
        //Capturar los datos de las vistas.
        int doc = Integer.parseInt(documentoEstudiante.getText());
        //Crear una instancia de Estudiante vacia
        Estudiante estudiante = new Estudiante();
        //Setiar el atributo documento
        estudiante.setDocumento(doc);
        //Crear un objeto de tipo DaoEstudiante
        DaoEstudiante daoEstudiante = new DaoEstudiante();
        //Llamar el método consultarEstudiante del Dao
        daoEstudiante.consultarEstudiante(estudiante);

        //Asignar a las cajas de texto los valores
        idEstudiante.setText(""+estudiante.getId());
        documentoEstudiante.setText(""+estudiante.getDocumento());
        nombreEstudiante.setText(estudiante.getNombre());
        apellidoEstudiante.setText(estudiante.getApellido());
        celularEstudiante.setText(""+estudiante.getCelular());
    }

    @FXML
    void eliminarEstudiante(ActionEvent event) {
        //Capturar los datos de las vistas.
        int doc = Integer.parseInt(documentoEstudiante.getText());
        String nom = nombreEstudiante.getText();
        String apell = apellidoEstudiante.getText();
        int cel = Integer.parseInt(celularEstudiante.getText());

        //Crear una instancia de Estudiante
        Estudiante estudiante = new Estudiante(0, doc, nom, apell, cel);
        DaoEstudiante daoEstudiante = new DaoEstudiante();
        System.out.println(daoEstudiante.eliminarEstudiante(estudiante));
    }

    @FXML
    void modificarEstudiante(ActionEvent event) {
        //Capturar los datos de las vistas.
        int doc = Integer.parseInt(documentoEstudiante.getText());
        String nom = nombreEstudiante.getText();
        String apell = apellidoEstudiante.getText();
        int cel = Integer.parseInt(celularEstudiante.getText());

        //Crear una instancia de Estudiante
        Estudiante estudiante = new Estudiante(0, doc, nom, apell, cel);
        DaoEstudiante daoEstudiante = new DaoEstudiante();
        System.out.println(daoEstudiante.modificarEstudiante(estudiante));
    }

    @FXML
    void registrarEstudiante(ActionEvent event) {
        //Capturar los datos de las vistas.
        int doc = Integer.parseInt(documentoEstudiante.getText());
        String nom = nombreEstudiante.getText();
        String apell = apellidoEstudiante.getText();
        int cel = Integer.parseInt(celularEstudiante.getText());

        //Crear una instancia de Estudiante
        Estudiante estudiante = new Estudiante(0, doc, nom, apell, cel);
        DaoEstudiante daoEstudiante = new DaoEstudiante();
        System.out.println(daoEstudiante.registrarEstudiante(estudiante));
    }

}