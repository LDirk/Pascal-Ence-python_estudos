Program Pzim ;
var 
	c, f: real;	
Begin

	writeln('Digite a temperatura em Celsius');
	read(c);
	
while (c < -273.15)  do
begin
	writeln('Digite uma temperatura válida');
	read(c) ;
end;


	f := (9/5)*c + 32;
  writeln(f:2:3 ,'-Graus fahrenheit')
End.