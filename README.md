# university_backend


necesita arreglos aun, importante debo de verificar que MySQL esté corriendo la base de datos.



prmero verificar si esta instalado y funcionan las dependencias:

Para correr el servidor de Python (Flask), seguir estos pasos:

Primero, asegúrate de estar en el directorio correcto en el proyecto:


cd university_backend
Activa el entorno virtual:
En Windows:

venv\Scripts\activate
En MacOS/Linux:

source venv/bin/activate
Verifica que tienes todas las dependencias instaladas:

pip install flask flask-sqlalchemy flask-cors pymysql cryptography

Para ejecutar el servidor, hay dos formas:

Método 1 - Usando el archivo run.py:

python run.py

Método 2 - Usando variables de entorno de Flask:

# En Windows:
set FLASK_APP=app
set FLASK_ENV=development
flask run

# En MacOS/Linux:
export FLASK_APP=app
export FLASK_ENV=development
flask run
Si todo está correcto, deberías ver algo como esto en la terminal:

 * Serving Flask app 'app'
 * Debug mode: on
 * Running on http://127.0.0.1:5000 (Press CTRL+C to quit)
 * Reloader: active
 * Debugger is active!
 * Debugger PIN: xxx-xxx-xxx
Esto significa que tu servidor está corriendo en localhost:5000.

Para probar que el servidor está funcionando:

Abre tu navegador
Ve a http://localhost:5000/api/auth/login
Si recibes un error 405 Method Not Allowed, eso es normal porque esta ruta solo acepta POST. Esto confirma que tu servidor está funcionando correctamente.

Para detener el servidor:

Presiona Ctrl + C en la terminal


para instalar:

# Activar el entorno virtual
# En Windows:
venv\Scripts\activate
# En MacOS/Linux:
source venv/bin/activate

# Instalar las dependencias necesarias
pip install flask
pip install flask-sqlalchemy
pip install flask-cors
pip install pymysql
pip install cryptography


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
