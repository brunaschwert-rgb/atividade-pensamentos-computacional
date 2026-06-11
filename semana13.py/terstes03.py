⚙️ Como PersonalizarÂngulos: Se o motor girar demais ou de menos, mude os valores dentro de meuServo.write(). Você pode usar qualquer ângulo entre 0° e 180°.Fechamento Automático: Se quiser que ela abra e feche sozinha após alguns segundos (sem precisar apertar o botão de novo), substitua a lógica do loop por:cppif (digitalRead(pinoBotao) == HIGH) {
  meuServo.write(90); // Abre
  delay(5000);        // Espera 5 segundos aberta
  meuServo.write(0);  // Fecha
}



Se você me disser qual o tipo de porta (se é uma maquete escolar, um TCC ou uma fechadura de verdade), 
posso te indicar sensores melhores (como leitores de cartão RFID ou sensores de presença) para deixar o projeto perfeito.
O que acha?
