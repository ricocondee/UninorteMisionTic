package Connection;

import java.sql.Statement;

import javafx.scene.control.Alert;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

public class S16_Connect {

    public Connection connect() {
        // Ruta donde está al db creada
        String url = "jdbc:sqlite:SQLite/DataBase/AlmacenV2.db"; 

        Connection conexion = null;

        try {
            // Creamos la conexión
            conexion = DriverManager.getConnection(url);
            System.out.println("Connection to SQLite has been stablished.");
        } catch (SQLException e) {
            System.out.println(e.getMessage());
        }
        return conexion;
    }

    public void create(String sql) {
        try (Connection conn = this.connect(); Statement stmt = conn.createStatement()) {
            stmt.executeUpdate(sql);
            Alert alert = new Alert(Alert.AlertType.INFORMATION);
            alert.setHeaderText(null);
            alert.setTitle("");
            alert.setContentText("Elemento agregado exitosamente");
            alert.showAndWait();
        } catch (SQLException e) {
            Alert alert = new Alert(Alert.AlertType.ERROR);
            alert.setHeaderText(null);
            alert.setTitle("Error");
            alert.setContentText(e.getMessage());
            alert.showAndWait();
            e.printStackTrace();
        }
    }
}
