int trigPinLeft = 13;
int echoPinLeft = 12;
int trigPinCenter = 11;
int echoPinCenter = 10;
int trigPinRight = 9;
int echoPinRight = 8;

int distanceArr[3];
long duration, distance;

void setup() {
  Serial.begin(9600);
  pinMode(echoPinLeft, INPUT);
  pinMode(trigPinLeft, OUTPUT);
  pinMode(echoPinCenter, INPUT);
  pinMode(trigPinCenter, OUTPUT);
  pinMode(echoPinRight, INPUT);
  pinMode(trigPinRight, OUTPUT);
}

int getDistance(int trigPin, int echoPin) {
  digitalWrite(trigPin, LOW);
  delayMicroseconds(5);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  duration = pulseIn(echoPin, HIGH);
  distance = (duration/2) * 0.034;
  return distance;
}

void loop() {
  // Send a sound wave
  distanceArr[0] = getDistance(trigPinLeft, echoPinLeft);
  distanceArr[1] = getDistance(trigPinCenter, echoPinCenter);
  distanceArr[2] = getDistance(trigPinRight, echoPinRight);
  Serial.print("L");
  Serial.print(distanceArr[0]);
  Serial.println(); 
  Serial.print("C");
  Serial.print(distanceArr[1]);
  Serial.println();
  Serial.print("R");
  Serial.print(distanceArr[2]);
  Serial.println(); 
  delay(75);
}