Program Pzim ;
var
		numero, contador,somacont: integer;	
			
begin
	writeln('Digite o n�mero inteiro n, (voce digitar um real positivo, sera gerado uma soma dos quadrados at� o menor inteiro):');
	read(numero);
while numero < 0 do
begin	
	writeln('Digite um n�mero v�lido');
	read(numero);
end;	
	
	
	
	contador:= 0;
	somacont:= 0;
	
	while (contador <= numero) do
	begin
	    somacont:= somacont + contador*contador;
		  contador:= contador + 1;		    
	end;
	
writeln('A soma dos quadrados de 1 at� n �:' ,somacont); 
End.