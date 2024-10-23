# university_backend


Hasta ahora se ha configurado la estructura básica del backend con Flask. Ahora necesitamos:

Conectar la aplicación JavaFX con el backend Flask. Para esto, necesitarás agregar dependencias HTTP en tu proyecto JavaFX:
En tu archivo pom.xml (si usas Maven) agrega:

xml

<dependency>
    <groupId>com.squareup.okhttp3</groupId>
    <artifactId>okhttp</artifactId>
    <version>4.9.1</version>
</dependency>

#Crear una clase de servicio en JavaFX para manejar las peticiones HTTP:


package services;

import okhttp3.*;
import org.json.JSONObject;
import java.io.IOException;

public class ApiService {
    private final OkHttpClient client = new OkHttpClient();
    private final String BASE_URL = "http://localhost:5000/api";
    private static final MediaType JSON = MediaType.parse("application/json; charset=utf-8");

    // Método para login
    public JSONObject login(String email, String password) throws IOException {
        JSONObject jsonBody = new JSONObject();
        jsonBody.put("email", email);
        jsonBody.put("password", password);

        RequestBody body = RequestBody.create(jsonBody.toString(), JSON);
        Request request = new Request.Builder()
                .url(BASE_URL + "/auth/login")
                .post(body)
                .build();

        try (Response response = client.newCall(request).execute()) {
            String responseBody = response.body().string();
            return new JSONObject(responseBody);
        }
    }

    // Método para registro
    public JSONObject register(JSONObject userData) throws IOException {
        RequestBody body = RequestBody.create(userData.toString(), JSON);
        Request request = new Request.Builder()
                .url(BASE_URL + "/auth/register")
                .post(body)
                .build();

        try (Response response = client.newCall(request).execute()) {
            String responseBody = response.body().string();
            return new JSONObject(responseBody);
        }
    }

    // Método para obtener cursos
    public JSONObject getCourses() throws IOException {
        Request request = new Request.Builder()
                .url(BASE_URL + "/courses")
                .get()
                .build();

        try (Response response = client.newCall(request).execute()) {
            String responseBody = response.body().string();
            return new JSONObject(responseBody);
        }
    }

    // Método para inscribir a un estudiante en un curso
    public JSONObject enrollStudent(String userId, int courseId) throws IOException {
        JSONObject jsonBody = new JSONObject();
        jsonBody.put("userId", userId);
        jsonBody.put("courseId", courseId);

        RequestBody body = RequestBody.create(jsonBody.toString(), JSON);
        Request request = new Request.Builder()
                .url(BASE_URL + "/courses/" + courseId + "/enroll")
                .post(body)
                .build();

        try (Response response = client.newCall(request).execute()) {
            String responseBody = response.body().string();
            return new JSONObject(responseBody);
        }
    }

    // Método para crear una tarea
    public JSONObject createAssignment(JSONObject assignmentData) throws IOException {
        RequestBody body = RequestBody.create(assignmentData.toString(), JSON);
        Request request = new Request.Builder()
                .url(BASE_URL + "/assignments")
                .post(body)
                .build();

        try (Response response = client.newCall(request).execute()) {
            String responseBody = response.body().string();
            return new JSONObject(responseBody);
        }
    }

    // Método para enviar una tarea
    public JSONObject submitAssignment(int assignmentId, JSONObject submissionData) throws IOException {
        RequestBody body = RequestBody.create(submissionData.toString(), JSON);
        Request request = new Request.Builder()
                .url(BASE_URL + "/assignments/" + assignmentId + "/submit")
                .post(body)
                .build(); // Cambiar a PUT si es necesario

        try (Response response = client.newCall(request).execute()) {
            String responseBody = response.body().string();
            return new JSONObject(responseBody);
        }
    }
}

#Utilizar la clase de servicio en tus controladores JavaFX para realizar peticiones HTTP al backend Flask:

package controller;

import javafx.fxml.FXML;
import javafx.fxml.Initializable;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.control.TextField;
import services.ApiService;

import java.net.URL;
import java.util.ResourceBundle;

public class MainController implements Initializable {

    @FXML
    private TextField txtUser ;
    @FXML
    private TextField txtPassword;
    @FXML
    private Button btnLogin;
    @FXML
    private Label lblMessage;

    private final ApiService apiService = new ApiService();

    @Override
    public void initialize(URL url, ResourceBundle resourceBundle) {
        btnLogin.setOnAction(event -> {
            String email = txtUser .getText();
            String password = txtPassword.getText();

            try {
                JSONObject response = apiService.login(email, password);
                lblMessage.setText("Bienvenido, " + response.getString("name"));
            } catch (IOException e) {
                lblMessage.setText("Error de conexión");
            }
        });
    }
}
