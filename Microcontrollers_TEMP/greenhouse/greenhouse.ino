// Definir el pin donde se conecta el sensor
const int sensorPin = A0; // Pin analógico A0 para leer los datos del sensor

// Variables para almacenar valores de humedad
int sensorValue = 0;
int soilMoisturePercent = 0;

// Configuración inicial
void setup() {
  Serial.begin(9600); // Iniciar la comunicación serial a 9600 bps
  Serial.println("Iniciando sensor de humedad del suelo...");
  
  pinMode(LED_BUILTIN, OUTPUT);
}

// Bucle principal
void loop() {
  // Leer el valor analógico del sensor
  sensorValue = analogRead(sensorPin);

  // Convertir el valor analógico (0-1023) a porcentaje (0-100%)
  soilMoisturePercent = map(sensorValue, 1023, 0, 0, 100); 
  // Ajustar los valores 1023 y 300 según el rango específico de tu sensor

  // Restringir el porcentaje al rango de 0 a 100
  soilMoisturePercent = constrain(soilMoisturePercent, 0, 100);

  if (soilMoisturePercent < 70) {
    digitalWrite(LED_BUILTIN, HIGH);
  } else {
    digitalWrite(LED_BUILTIN, LOW); 
  }

  // Imprimir los resultados en el monitor serial
  Serial.print("Valor analógico: ");
  Serial.print(sensorValue);
  Serial.print("  | Porcentaje de humedad: ");
  Serial.print(soilMoisturePercent);
  Serial.println("%");

  // Esperar medio segundo antes de la siguiente lectura
  delay(500);
}
