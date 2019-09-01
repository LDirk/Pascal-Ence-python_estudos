Program Pzim ;
var 
	numero,contador,sequencia,seqanterior,seqfib :integer;
Begin
  writeln('Digite o 	numero de sequencias de fibbonacci');
  writeln('Se você digitar um N não inteiro, o numero de sequencias será o menor inteiro');
  read(numero);
	
while (numero < 0) or (numero =0)  do
begin
	writeln('Digite um número válido: ');
	read(numero)
end;	

                          
if numero > 0 then
begin  
	contador := 3;
	sequencia := 1;
	seqanterior := 0;
	seqfib := 0;
	
	if numero =1 then
	begin	
	seqfib := 0;
	writeln(seqfib)
	end;
	
	if numero =2 then
	begin
	writeln(0);
	seqfib := 1 ;
	writeln(seqfib);
	end; 
	
	
	if numero >= 3 then
	begin
	
		seqfib := 1;
		sequencia := 1;
 		writeln(0);
 		writeln(1);
 		while(contador <= numero) do
 		begin
 			
 			seqfib := sequencia + seqanterior;
 			seqanterior := sequencia;
 			sequencia := seqfib;
 			contador := contador + 1;
 			writeln(seqfib);
 		end;
 	end;
end;


End.
