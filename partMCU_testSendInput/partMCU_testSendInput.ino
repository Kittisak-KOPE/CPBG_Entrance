void setup() {
  pinMode(8 , INPUT);
  Serial.begin(9600);
}

void loop() {
    int touchedSensor = digitalRead(8);
    Serial.println(touchedSensor);
    delay(1000);
}
