package Connection;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

public class S15_Connect {

    public Connection connect() {
        // Ruta donde está al db creada
        String url = "jdbc:sqlite:SQLite/DataBase/Almacen.db"; 

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
}
