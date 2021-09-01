import java.io.IOException;
import java.sql.Connection;
import java.sql.ResultSet;
import java.sql.ResultSetMetaData;
import java.sql.SQLException;
import java.sql.Statement;
import Connection.S16_Connect;
import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.fxml.FXMLLoader;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.scene.control.Alert;
import javafx.scene.control.Button;
import javafx.scene.control.TextField;
import javafx.stage.Stage;
import javafx.scene.control.TextArea;

public class S16_InicioController {

    @FXML
    private TextField code;

    @FXML
    private TextField name;

    @FXML
    private TextField SellingPrice;

    @FXML
    private TextField ShopingPrice;

    @FXML
    private TextField StoreQuantity;

    @FXML
    private TextField MinimumQuantity;

    @FXML
    private TextField MaximumQuantity;

    @FXML
    private Button CreateButton;

    @FXML
    private TextArea productList;

    @FXML
    private Button updateButton;

    @FXML
    private Button sumarButton;
    
    @FXML
    private Button saleButton;

    @FXML
    void CreateProduct(ActionEvent event) { // throws SQLException {
        S16_Connect objConexion = new S16_Connect();// estandar

        Integer codigo = Integer.parseInt(code.getText());// captura del valor de la caja de texto
        String nombre = name.getText();
        int precioCompra = Integer.parseInt(ShopingPrice.getText());
        int precioVenta = Integer.parseInt(SellingPrice.getText());
        int cantidadBodega = Integer.parseInt(StoreQuantity.getText());
        int cantidadMinima = Integer.parseInt(MinimumQuantity.getText());
        int cantidadMaxima = Integer.parseInt(MaximumQuantity.getText());

        try (Connection conn = objConexion.connect(); Statement stmt = conn.createStatement()) {
            stmt.executeUpdate(
                    "INSERT INTO Productos (Codigo, Nombre, Precio_compra, Precio_venta, Cantidad_bodega, Cantidad_minima, Cantidad_maxima)"
                            + "VALUES(" + codigo + ",'" + nombre + "'," + precioCompra + "," + precioVenta + ","
                            + cantidadBodega + "," + cantidadMinima + "," + cantidadMaxima + ");"

            );

            Alert alert = new Alert(Alert.AlertType.ERROR);
            alert.setHeaderText(null);
            alert.setTitle("Productos");
            alert.setContentText("Producto ingresado correctamente");
            alert.showAndWait();

        } catch (SQLException errors) {
            Alert alert = new Alert(Alert.AlertType.ERROR);
            alert.setHeaderText(null);
            alert.setTitle("Productos");
            alert.setContentText(errors.getMessage());// obteniendo el mensaje de error
            alert.showAndWait();
        }

    }

    @FXML
    void viewProduct(ActionEvent event) {
        S16_Connect objConexion = new S16_Connect();// estandar
        String query = "SELECT * FROM Productos";
        productList.setEditable(false);
        try (Connection conn = objConexion.connect(); Statement stmt = conn.createStatement()) {
            ResultSet resultSet = stmt.executeQuery(query);
            ResultSetMetaData metadata = resultSet.getMetaData();
            int numeroColumnas = metadata.getColumnCount();// contar numero de columnas
            String productos = "";
            while (resultSet.next()) {
                for (int i = 1; i <= numeroColumnas; i++) {
                    if (i > 0) {
                        System.out.println(",");
                        String columnValue = resultSet.getString(i);// obtener el dato de cada columna o atributo
                        productos += metadata.getColumnName(i) + ":" + columnValue + "\n";
                    }
                }
            }
            productList.setText(productos);
        } catch (SQLException errors) {
            Alert alert = new Alert(Alert.AlertType.ERROR);
            alert.setHeaderText(null);
            alert.setTitle("Productos");
            alert.setContentText(errors.getMessage());// obteniendo el mensaje de error
            alert.showAndWait();
        }

    }

    @FXML
    void updateProduct(ActionEvent event) {
        S16_Connect objConexion = new S16_Connect();// estandar

        int cantMax = 200;
        try (Connection conn = objConexion.connect(); Statement stmt = conn.createStatement()) {
            stmt.executeUpdate("UPDATE Productos SET Cantidad_maxima = " + cantMax);

            Alert alert = new Alert(Alert.AlertType.ERROR);
            alert.setHeaderText(null);
            alert.setTitle("Productos");
            alert.setContentText("Cantidad maxima actualizada correctamente");
            alert.showAndWait();

        } catch (SQLException errors) {
            Alert alert = new Alert(Alert.AlertType.ERROR);
            alert.setHeaderText(null);
            alert.setTitle("Productos");
            alert.setContentText(errors.getMessage());// obteniendo el mensaje de error
            alert.showAndWait();
        }
    }

    @FXML
    void sumarProduct(ActionEvent event) {
        S16_Connect objConexion = new S16_Connect();// estandar
        String query = "SELECT SUM(Precio_compra) AS sumaProductos FROM Productos";
        productList.setEditable(false);
        try (Connection conn = objConexion.connect(); Statement stmt = conn.createStatement()) {
            ResultSet resultSet = stmt.executeQuery(query);
            ResultSetMetaData metadata = resultSet.getMetaData();
            int numeroColumnas = metadata.getColumnCount();// contar numero de columnas
            String productos = "";
            while (resultSet.next()) {
                for (int i = 1; i <= numeroColumnas; i++) {
                    if (i > 0) {
                        System.out.println(",");
                        String columnValue = resultSet.getString(i);// obtener el dato de cada columna o atributo
                        productos += metadata.getColumnName(i) + ":" + columnValue + "\n";
                    }
                }
            }
            productList.setText(productos);
        } catch (SQLException errors) {
            Alert alert = new Alert(Alert.AlertType.ERROR);
            alert.setHeaderText(null);
            alert.setTitle("Productos");
            alert.setContentText(errors.getMessage());// obteniendo el mensaje de error
            alert.showAndWait();
        }
    }

    @FXML
    void createSale(ActionEvent event) throws IOException {
        FXMLLoader vistaRegistro = new FXMLLoader(getClass().getResource("Vista/S16_registro.fxml"));
            Parent root = vistaRegistro.load();
            S16_RegistroVentaController driver = vistaRegistro.getController();
            Scene scene = new Scene(root);
            Stage stage = new Stage();
            stage.setTitle("");
            stage.setScene(scene);
            stage.show();
    } 

}
