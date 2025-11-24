const int BATHROOM_LIGHT = 11;
const int BEDROOM_LIGHT = 12;
const int KITCHEN_LIGHT = 13;
const int garage_LIGHT = 10;

void menu(){
   Serial.println("[1]. Turn on bathroom_light");
   Serial.println("[2]. Turn off bathroom_light");
   Serial.println("[3]. Turn on bedroom_light");
   Serial.println("[4]. Turn off bedroom_light");
   Serial.println("[5]. Turn on kitchen_light");
   Serial.println("[6]. Turn off kitchen_light");
   Serial.println("[7]. Turn on all lights");
   Serial.println("[8]. Turn off all lights");
   Serial.println("[9]. Blinking lights");
   Serial.println("[10]. Turn on garage_light");
   Serial.println("[11]. Turn off garage_light");
}

void setup() {
  pinMode(BATHROOM_LIGHT, OUTPUT);
  pinMode(BEDROOM_LIGHT, OUTPUT);
  pinMode(KITCHEN_LIGHT, OUTPUT);
  pinMode(garage_LIGHT, OUTPUT);
  Serial.begin(9600);
  menu();
}

void loop() {
  if(Serial.available() > 0){

    int opt = Serial.parseInt();  

    if (opt == 1){
      digitalWrite(BATHROOM_LIGHT, HIGH);
    }
    if (opt == 2){
      digitalWrite(BATHROOM_LIGHT, LOW);
    }
    if (opt == 3){
      digitalWrite(BEDROOM_LIGHT, HIGH);
    }
    if (opt == 4){
      digitalWrite(BEDROOM_LIGHT, LOW);
    }
    if (opt == 5){
      digitalWrite(KITCHEN_LIGHT, HIGH);
    }
    if (opt == 6){
      digitalWrite(KITCHEN_LIGHT, LOW);
    }

    if (opt == 10){
      digitalWrite(garage_LIGHT, HIGH);
    }
    if (opt == 11){
      digitalWrite(garage_LIGHT, LOW);
    }

    if (opt == 7){
      digitalWrite(BATHROOM_LIGHT, HIGH);
      digitalWrite(BEDROOM_LIGHT, HIGH);
      digitalWrite(KITCHEN_LIGHT, HIGH);
      digitalWrite(garage_LIGHT, HIGH);
    }

    if (opt == 8){
      digitalWrite(BATHROOM_LIGHT, LOW);
      digitalWrite(BEDROOM_LIGHT, LOW);
      digitalWrite(KITCHEN_LIGHT, LOW);
      digitalWrite(garage_LIGHT, LOW);
    }

    if (opt == 9){
      for(int i = 0; i < 1000; i++){
        digitalWrite(BATHROOM_LIGHT, HIGH);
        digitalWrite(BEDROOM_LIGHT, HIGH);
        digitalWrite(KITCHEN_LIGHT, HIGH);
        digitalWrite(garage_LIGHT, HIGH);
        delay(300);
        digitalWrite(BATHROOM_LIGHT, LOW);
        digitalWrite(BEDROOM_LIGHT, LOW);
        digitalWrite(KITCHEN_LIGHT, LOW);
        digitalWrite(garage_LIGHT, LOW);
        delay(300);
      }
    }
  }
}