program adivinha;

var
  menor,maior,meio,opcao,palpites : integer;

begin   
                                
  writeln('Escolha um número de 1 a 100');
  writeln('Tentarei adivinhar o número...');
  menor:=1;
  maior:= 100;
  palpites:=0;
  
  repeat
  
    palpites:=palpites+1;
    meio:=(maior+menor)div 2;
    
    writeln('Por acaso o número é ',meio,'?');
    writeln('Se o número for igual digite 1.');
    writeln('Se o número for maior digite 2.');
    writeln('Se o número for menor digite 3.');
    readln(opcao);
    
    if (opcao=2) then 
			menor:=meio+1;
			
    if (opcao=3) then 
			maior:=meio-1;
			
    if (maior<=menor) then 
		begin
      meio:=(maior+menor)div 2;
      opcao:=1;
    end;
    
  until (opcao=1);
  
  writeln('Seu número é ',meio,'!');
  writeln('Foram feitas ',palpites,' perguntas.');
end.