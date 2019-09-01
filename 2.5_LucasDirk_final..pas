Program Pzim ;

Var num:array[1..11] of integer;
x,y,imenor,troca:integer;

Begin
writeln('Digite os números inteiros que deseja ordenar');

for x:=1 to 10 do
begin
	writeln('Número', x);
	read(num[x]);
end;	

for x:= 1 to 10 do
begin
	imenor := x;
	for y:= x + 1 to 10 do
	begin
		if num[y] < num[imenor] then
			imenor:=y;
	end;
	
	if num[x] <> num[imenor] then
	begin
		troca := num[x];
		num [x] := num[imenor];
		num [imenor] := troca;
	end;
end;

writeln;
writeln('Numeros ordenados em ordem crescente');
writeln;
for x:=1 to 10 do
begin
	writeln(num[x]);
end;
  
End.