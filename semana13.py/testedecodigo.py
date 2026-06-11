cpp#include <Servo.h> // Inclui a biblioteca padrão para controlar o servo

// Configuração dos pinos
const int pinoBotao = 2; 
const int pinoServo = 9; 

// Variáveis de controle
Servo meuServo;      // Cria o objeto para controlar o motor
bool portaAberta = false; 

void setup() {
  pinMode(pinoBotao, INPUT);     // Define o pino do botão como entrada
  meuServo.attach(pinoServo);    // Associa o motor ao pino digital 9
  meuServo.write(0);             // Inicia com a porta fechada (ângulo 0°)
}

void loop() {
  // Verifica se o botão foi pressionado
  if (digitalRead(pinoBotao) == HIGH) { 
    
    if (portaAberta == false) {
      // Se estava fechada, move o servo para 90 graus para ABRIR
      meuServo.write(90); 
      portaAberta = true; 
    } 
    else {
      // Se estava aberta, volta o servo para 0 graus para FECHAR
      meuServo.write(0); 
      portaAberta = false; 
    }
    
    delay(500); // Pequena pausa para evitar que um clique seja lido várias vezes
  }
}
