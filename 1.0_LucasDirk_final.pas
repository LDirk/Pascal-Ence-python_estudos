Program Pzim ;
var
	distancia, tempo, velocidade: real;
Begin
writeln('Digite a distancia em Km: ');
read(distancia);
			
while (distancia <= 0)  do
begin
writeln('Digite uma distancia v�lida');
read(distancia);
end;

writeln('Digite o tempo em horas: ');
read(tempo);		

while (tempo <= 0) do
begin
writeln('Digite um tempo v�lido');
read(tempo);
end;
	
velocidade := distancia/tempo;
writeln(velocidade:2:3, 'km/h');
	  
End.