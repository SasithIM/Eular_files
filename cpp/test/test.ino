// void setup(){
//     Serial.println("Hello world");
//     pinMode(4,  OUTPUT);
//     pinMode(7, OUTPUT);

//     digitalWrite(4, LOW);
//     digitalWrite(7, LOW);
// }

// void loop(){
//     digitalWrite(7, HIGH);
//     delay(100);
//     digitalWrite(7,LOW);
//     delay(1000);
// }


int ledPins[] = {5,6,7,9,10,11,12,13}; // Array for LED pins
int ledCount = 8; // Updated number of LEDs

void setup() {
  // Set all pins connected to LEDs as OUTPUT
  for (int i = 0; i < ledCount; i++) {
    pinMode(ledPins[i], OUTPUT);
  }
}

void loop() {
  // Light up LEDs from left to right
  for (int i = 0; i < ledCount; i++) {
    digitalWrite(ledPins[i], HIGH); // Turn LED on
    delay(100); // Wait for 200ms
    // digitalWrite(ledPins[i], LOW);  // Turn LED off
  }
  for (int i = 0; i < ledCount; i++){
    digitalWrite(ledPins[i],LOW);
    delay(100);

  }
}
