Program Pzim ;
var
	valor, comprimento, largura: real;
Begin
	writeln('Digite o comprimento');
	read(comprimento);
	
while (comprimento < 0) do
begin
	writeln('Comprimento inv�lido');
	read(comprimento);	
end;	
	
	writeln('Digite a largura');
	read(largura);
	
while largura < 0 do
begin
	writeln('Largura inv�lida');
	read(largura);	
end;		
	
	
		
	valor:= 35*largura*comprimento;
	writeln('Ser� gasto um total de-' ,valor:2:2,'-reais')
	
  
End.