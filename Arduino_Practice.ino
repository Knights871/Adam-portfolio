
//practice #1

void blinkLED (int time){
    digitalWrite(LED_BUILTIN, HIGH);
    delay(time);
    digitalWrite(LED_BUILTIN, LOW);
    delay(time;)
}
  

void setup() {
Serial.begin(9600);
pinMode(LED_BUILTIN, OUTPUT);


}

void loop() {
int voltage = analogRead(A0);
Serial.println(voltage);
if (voltage <300) {
  blinkLED(100);
} elif (voltage >= 300 && voltage <700){
  blinkLED(300);
} else{
  digitalWrite(LED_BUILTIN, LOW);
}
}


//practice #2

void setup(){
Serial.begin(9600);
pinMode(LED_BUILTIN, OUTPUT);
}

void loop(){
int value analogRead(A0);
Serial.println(value);
if (value > 500){
  digitalWrite(LED_BUILTIN, HIGH)}
else{
  digitalWrite(LED_BUILTIN, LOW)}
}




//practice #3


void flashFast(){
digitalWrite(LED_BUILTIN, HIGH);
delay(50);
digitalWrite(LED_BUILTIN, LOW);
}

void setup(){
  Serial.begin(9600);
  pinMode(LED_BUILTIN, OUTPUT);
}

void loop(){
  flashFast();
}






//practice #4


void setup(){
  Serial.begin(9600);
  pinMode(LED_BUILTIN, OUTPUT);
}


void loop(){
  int voltage = analogRead(A1);
  Serial.println(voltage);
  if (voltage < 300){
    digitalWrite(LED_BUILTIN, HIGH);
    delay(100);
  } else if (voltage > 300 && voltage < 700){
    digitalWrite(LED_BUILTIN,HIGH);
    delay(1000);
  } else {
    digitalWrite(LED_BUILTIN, HIGH);
  }
}





//pactice #5

void setup() {
Serial.Begin(9600);
pinMode(LED_BUILTIN, OUTPUT);


}

void loop() {
int voltage = analogRead(A2);
Serial.println(voltage);
if voltage < 200{
digitalWrite(LED_BUILTIN, On)
}elif voltage > 200 and <700{
  digitalWrite(LED_BUILTIN,On)
  delay(300)
  digitalWrite(LED_BUILTIN,Off)
} else {
  digitalWrite(LED_BUILTIN,Off)
}

}


