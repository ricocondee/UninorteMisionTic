import javafx.collections.FXCollections;
import javafx.collections.ObservableList;
import javafx.event.ActionEvent;

import java.sql.Connection;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;

import Connection.S16_Connect;
import javafx.fxml.FXML;
import javafx.scene.control.Alert;
import javafx.scene.control.Button;
import javafx.scene.control.ChoiceBox;
import javafx.scene.control.TextField;

public class S16_RegistroVentaController {

    @FXML
    private ChoiceBox<String> cliente;

    @FXML
    private ChoiceBox<String> producto;

    @FXML
    private Button registro;

    @FXML
    private TextField cantidad;

    @FXML
    private Button crear;

    @FXML
    private void initialize() {
        obtenerListaCliente();
        obtenerListaProductos();
    }

    @FXML
    private TextField genero;

    @FXML
    private TextField cedula;

    @FXML
    private TextField nombre;

    @FXML
    private TextField apellidos;

    @FXML
    void crearCliente(ActionEvent event) {
        S16_Connect objConexion = new S16_Connect();// estandar
        int ced = Integer.parseInt(cedula.getText());
        String nom = nombre.getText();
        String apell = apellidos.getText();
        String gen = genero.getText();

        try (Connection conn = objConexion.connect(); Statement stmt = conn.createStatement()) {
            stmt.executeUpdate("INSERT INTO Clientes(Cedula, Nombre, Apellidos, Genero)" + "VALUES(" + ced + "," + "'"
                    + nom + "'" + "," + "'" + apell + "'" + "," + "'" + gen + "'" + ")");

            Alert alert = new Alert(Alert.AlertType.INFORMATION);
            alert.setHeaderText(null);
            alert.setTitle("");
            alert.setContentText("Cliente ingresado correctamente");
            alert.showAndWait();
        } catch (SQLException errors) {
            Alert alert = new Alert(Alert.AlertType.ERROR);
            alert.setHeaderText(null);
            alert.setTitle("ERROR");
            alert.setContentText(errors.getMessage());// obteniendo el mensaje de error
            alert.showAndWait();
        }
    }

    @FXML
    void registroVenta(ActionEvent event) {
        S16_Connect objConexion = new S16_Connect();// estandar
        int cli = Integer.parseInt(obtenerLlaveChoise(cliente.getValue()));
        int prod = Integer.parseInt(obtenerLlaveChoise(producto.getValue()));
        int cant = Integer.parseInt(cantidad.getText());

        objConexion.create(
                "INSERT INTO Ventas(Cliente, Producto, Cantidad)" + "VALUES(" + cli + "," + prod + "," + cant + ")");
    }

    String obtenerLlaveChoise(String cadena) {// obtener los id de los chicebox
        String partes[] = cadena.split(" ");
        String ultima = partes[partes.length - 2];
        return ultima;
    }

    ObservableList<String> client = FXCollections.observableArrayList("Se debe adicionar este cliente");

    void obtenerListaCliente() {
        S16_Connect objConexion = new S16_Connect();// estandar
        String query = "SELECT * FROM Clientes ORDER BY ID ASC";
        try (Connection conn = objConexion.connect(); Statement stmt = conn.createStatement()) {
            ResultSet resultSet = stmt.executeQuery(query);
            while (resultSet.next()) {
                client.add(resultSet.getInt("ID") + " " + resultSet.getString("Nombre"));
            }
            cliente.setItems(client);
            stmt.close();
            resultSet.close();
        } catch (SQLException error) {
            Alert alert = new Alert(Alert.AlertType.ERROR);
            alert.setHeaderText(null);
            alert.setTitle("ERROR");
            alert.setContentText(error.getMessage());
            alert.showAndWait();
        }
    }

    ObservableList<String> product = FXCollections.observableArrayList("Se debe adicionar este producto");

    void obtenerListaProductos() {
        S16_Connect objConexion = new S16_Connect();// estandar
        String query = "SELECT * FROM Productos ORDER BY Codigo ASC";
        try (Connection conn = objConexion.connect(); Statement stmt = conn.createStatement()) {
            ResultSet resultSet = stmt.executeQuery(query);
            while (resultSet.next()) {
                product.add(resultSet.getInt("Codigo") + " " + resultSet.getString("Nombre"));
            }
            producto.setItems(product);
            stmt.close();
            resultSet.close();
        } catch (SQLException error) {
            Alert alert = new Alert(Alert.AlertType.ERROR);
            alert.setHeaderText(null);
            alert.setTitle("ERROR");
            alert.setContentText(error.getMessage());
            alert.showAndWait();
        }
    }
}
