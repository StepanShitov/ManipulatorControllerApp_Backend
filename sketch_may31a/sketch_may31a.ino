String incomingByte ;    

void setup() {

  Serial.begin(9600);

  pinMode(13, OUTPUT);

}
void loop() {

  if (Serial.available() > 0) {

  incomingByte = Serial.readStringUntil('\n');

    if (incomingByte == "1") {
      analogWrite(3, 50);
      Serial.write("music");      
      delay(2000);
      analogWrite(3, 0);
    }

    else if (incomingByte == "2") {
      digitalWrite(13, HIGH);
      Serial.write("led");
      delay(2000);
      digitalWrite(13, LOW);
    }
    else{

     analogWrite(3, 50);
      Serial.write("music");      
      delay(2000);
      analogWrite(3, 0);

    }

  }

}
