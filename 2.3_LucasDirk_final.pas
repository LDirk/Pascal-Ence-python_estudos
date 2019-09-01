Program Pzim ;
const 
	max = 7;

var
	 numero : array[1..max] of real;
	 i : integer;
	 soma : real;
	 media : real;
	 somatoriovar: real;
Begin

i := 1;
while i<= max do
begin
	writeln('Digite os sete números que voce deseja calcular a média, variancia e desvio padrão');	
	read(numero[i]);
	i := i + 1	
end;

soma := 0;
i := 1;
while i<= max do
begin
	soma := soma + numero[i];
	i := i + 1;
end;

media := (soma/7);
writeln(media);

i := 1
somatoriovar:= 0
while i <= max do 
begin
	somatoriovar := somatoriovar + (numero[i]-media)*(numero[i]-media)
	i = i + 1
end;

variancia :=(somatoriovar/6)









  
End.