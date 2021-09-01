package Modelo;

import java.sql.Connection;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;

public class DaoEstudiante {
    public String registrarEstudiante(Estudiante estudiante) {
        // Establecer la conexión a la base de datos
        Connect objConexion = new Connect();
        String mensaje = "";

        // Realizar el insert a la base de datos.
        try (Connection conn = objConexion.connect(); Statement stmt = conn.createStatement()) {
            String sql = "INSERT INTO Estudiantes(Documento, Nombre, Apellido, Celular)" + "VALUES("
                    + estudiante.getDocumento() + "," + "'" + estudiante.getNombre() + "'" + "," + "'"
                    + estudiante.getApellido() + "'" + "," + estudiante.getCelular() + ");";
            stmt.executeUpdate(sql);
            mensaje = "El estudiante se registró exitosamente";
        } catch (SQLException error) {
            mensaje = error.getMessage();
        }
        return mensaje;
    }

    public void consultarEstudiante(Estudiante estudiante) {
        // Establecer la conexión a la base de datos
        Connect objConexion = new Connect();
        String sql = "SELECT * FROM Estudiantes WHERE Documento=" + estudiante.getDocumento();
        try (Connection conn = objConexion.connect(); Statement stmt = conn.createStatement()) {
            ResultSet resultado = stmt.executeQuery(sql);
            estudiante.setId(Integer.parseInt(resultado.getString(1)));
            estudiante.setNombre(resultado.getString(3));
            estudiante.setApellido(resultado.getString(4));
            estudiante.setCelular(Integer.parseInt(resultado.getString(5)));
        } catch (SQLException error) {
            System.out.println(error.getMessage());
        }
    }

    public String modificarEstudiante(Estudiante estudiante) {
        // Establecer la conexión a la base de datos
        Connect objConexion = new Connect();
        String mensaje = "";

        // Realizar el update a la base de datos.
        try (Connection conn = objConexion.connect(); Statement stmt = conn.createStatement()) {
            String sql = "UPDATE Estudiantes SET " + "Nombre='" + estudiante.getNombre() + "'" + "," + "Apellido='"
                    + estudiante.getApellido() + "'" + "," + "Celular=" + estudiante.getCelular()
                    + " WHERE Documento = " + estudiante.getDocumento();
            stmt.executeUpdate(sql);
            mensaje = "El estudiante se modificó exitosamente";
        } catch (SQLException error) {
            mensaje = error.getMessage();
        }
        return mensaje;
    }

    public String eliminarEstudiante(Estudiante estudiante) {
        // Establecer la conexión a la base de datos
        Connect objConexion = new Connect();
        String mensaje = "";

        try (Connection conn = objConexion.connect(); Statement stmt = conn.createStatement()) {
            String sql = "DELETE FROM Estudiantes Where Documento=" + estudiante.getDocumento();
            stmt.executeUpdate(sql);
            mensaje = "El estudiante se eliminó exitosamente";
        } catch (SQLException error) {
            mensaje = error.getMessage();
        }
        return mensaje;
    }
}