#define PIR_1 D1
#define PIR_2 D2

int pir_value;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  pinMode(PIR_1, INPUT);
  pinMode(PIR_1, INPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  delay(300);
  pir_value = digitalRead(PIR_1);
  Serial.println(pir_value);
  
}
