Você disse: preciso de ajuda para um programa que tenha um codigo que faça a porta abrir r feçarPara criar um projeto de automação que abra e feche uma porta (seja uma maquete, um armário ou uma trava real), a plataforma mais popular, acessível e fácil de programar é o Arduino.
Abaixo, você encontra o circuito básico e o código pronto utilizando um Servo Motor (que gira para empurrar a porta ou liberar uma trava) e um Botão para comandar a ação.
🔌 Componentes Necessários1 Placa Arduino (Uno, Nano ou similar)1 Servo Motor (ex: SG90 para maquetes ou MG996R para portas reais)1 Botão (Pulsador/Push-button)1 Resistor de 10k Ω (para o botão)Cabos Jumper e 1 Protoboard
🛠️ Esquema de Ligação (Hardware)Servo Motor:Fio Vermelho (VCC) → Pino 5V do ArduinoFio Marrom/Preto (GND) → Pino GND do ArduinoFio Laranja/Amarelo (Sinal) → Pino Digital 9 do ArduinoBotão:Uma perna ligada ao 5V.
A outra perna ligada ao Pino Digital 2 do Arduino E também ao GND através do resistor de 10k Ω (ligação em Pull-Down).
💻 Código Pronto (Arduino)Copie e cole este código na sua IDE do Arduino:cpp#include <Servo.h> // Inclui a biblioteca padrão para controlar o servo

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
Use o código com cuidado.Se você quer entender visualmente como fazer as conexões físicas e configurar a biblioteca do motor no seu computador, assista a este guia prático:6mCOMO PROGRAMAR O SERVO MOTOR NO ARDUINO?JuliaLabsYouTube · 28 de fev. de 2023⚙️ Como PersonalizarÂngulos: Se o motor girar demais ou de menos, mude os valores dentro de meuServo.write(). Você pode usar qualquer ângulo entre 0° e 180°.Fechamento Automático: Se quiser que ela abra e feche sozinha após alguns segundos (sem precisar apertar o botão de novo), substitua a lógica do loop por:cppif (digitalRead(pinoBotao) == HIGH) {
  meuServo.write(90); // Abre
  delay(5000);        // Espera 5 segundos aberta
  meuServo.write(0);  // Fecha
}
Use o código com cuidado.Se você me disser qual o tipo de porta (se é uma maquete escolar, um TCC ou uma fechadura de verdade), posso te indicar sensores melhores (como leitores de cartão RFID ou sensores de presença) para deixar o projeto perfeito. O que acha?12 sitesPORTA COM SENHA ARDUINO - Português29 de nov. de 2017 — Se estiver com pressa pague alguém para fazer, se não estiver, comece do zero. Você vai usar um servo motor para fechar a porta? G...Arduino ForumCOMO PROGRAMAR O SERVO MOTOR NO ARDUINO?28 de fev. de 2023 — no Arduíno tem algumas questõezinhas que eu quero conversar com vocês e que eu quero mostrar para vocês de atenção nesse processo ...6mYouTube·JuliaLabsComo usar Servo Motor no Arduino1 de nov. de 2023 — utilizando Arduino com todos os segredos que não te contam mas que faz toda a diferença Eu sou professor Marlon nard especialista ...2mYouTube·Marlon NardiMostrar tudoVocê disse: porta de um caixa pequena que é do tamanho de um suporte de notebookPara um projeto desse tamanho (uma caixa pequena semelhante a um suporte de notebook), a estrutura mecânica é leve. Um Servo Motor SG90 (azul, muito comum) ou o MG90S (com engrenagens de metal, mais forte) são perfeitos para essa aplicação.Como o espaço interno da caixa pode ser limitado, o ideal é usar uma placa menor como o Arduino Nano ou o Arduino Pro Mini para economizar espaço.🧱 Como Fixar o Motor na CaixaPosicionamento: Fixe o servo motor na parede interna da caixa, perto da dobradiça da porta.Braço de Alavanca: Use uma das hélices plásticas que vêm com o servo motor.Mecanismo:Direto: O eixo do servo fica exatamente na linha da dobradiça (o motor gira e a porta gira junto).Haste: O servo empurra um pequeno arame rígido (clipes de papel esticado) conectado à porta.💻 Código Otimizado (Abertura Suave)Motores pequenos dão trancos se mudarem de posição muito rápido, o que pode quebrar a sua caixa ou descolar o motor. Este código faz a portinha abrir e fechar de forma suave e realista:cpp#include <Servo.h>

const int pinoBotao = 2; 
const int pinoServo = 9; 

Servo meuServo;
bool portaAberta = false;

// Ajuste estes ângulos conforme o limite físico da sua caixa
const int anguloFechado = 0;   
const int anguloAberto = 90;   
const int velocidade = 15; // Quanto maior, mais lento (em milissegundos)

void setup() {
  pinMode(pinoBotao, INPUT_PULLUP); // Usa o resistor interno do Arduino (simplifica os fios)
  meuServo.attach(pinoServo);
  meuServo.write(anguloFechado);    // Começa fechada
}

void loop() {
  // Com INPUT_PULLUP, o botão passa a ser lido como LOW quando apertado
  if (digitalRead(pinoBotao) == LOW) { 
    
    if (!portaAberta) {
      // Abre suavemente
      for (int pos = anguloFechado; pos <= anguloAberto; pos++) {
        meuServo.write(pos);
        delay(velocidade);
      }
      portaAberta = true;
    } 
    else {
      // Fecha suavemente
      for (int pos = anguloAberto; pos >= anguloFechado; pos--) {
        meuServo.write(pos);
        delay(velocidade);
      }
      portaAberta = false;
    }
    
    delay(500); // Anti-repique do botão
  }
}
Use o código com cuidado.🔌 Vantagem da Ligação OtimizadaNo código acima, usei INPUT_PULLUP.
Isso significa que você não precisa do resistor físico de 10k no circuito.
Ligue uma perna do botão direto no pino GND.
Ligue a outra perna do botão direto no pino D2 do Arduino.
Para avançarmos na montagem da sua caixa, você prefere que ela abra por controle remoto, por senha em um teclado ou quer manter apenas o botão físico?
