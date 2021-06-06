String incomingByte ;    

void setup() {

  Serial.begin(9600);

  pinMode(12, OUTPUT);
  pinMode(8, OUTPUT);
  pinMode(7, OUTPUT);

}
void loop() {

  if (Serial.available() > 0) {

  incomingByte = Serial.readStringUntil('\n');

    if (incomingByte == "1") {
      digitalWrite(12, HIGH);
      Serial.write("led");
      delay(5000);
      digitalWrite(12, LOW);
    }

    else if (incomingByte == "2") {
      digitalWrite(8, HIGH);
      Serial.write("led");
      delay(5000);
      digitalWrite(8, LOW);
    }
    else if (incomingByte == "3") {
      digitalWrite(7, HIGH);
      Serial.write("led");
      delay(5000);
      digitalWrite(7, LOW);
    }
    else{

     analogWrite(3, 50);
      Serial.write("music");      
      delay(2000);
      analogWrite(3, 0);

    }

  }

}
