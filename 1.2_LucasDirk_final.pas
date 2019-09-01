Program Pzim ;
var
	centimetro, polegada: real;
Begin
	writeln('Digite os centimetros');
	read(centimetro);
	
while centimetro < 0 do
begin
	writeln('Digite uma medida válida');
	read(centimetro)
end;
	
	polegada := centimetro/2.54 ;
	
	writeln('Isso equivale a ', polegada , 'polegadas');
  
End.