Program Pzim ;
var
	nota1, nota2, nota: real;
Begin
  writeln('Digite a primeira nota do aluno,(nota entre 0 a 10) ');
	read(nota1);
	
while (nota1 < 0) or (nota1 >10) do
begin
	writeln('Digite uma nota válida');
	read(nota1);
end;

	writeln('Digite a segunda nota do aluno,(nota entre 0 a 10): ');
	read(nota2);
	
while (nota2 < 0) or (nota2 >10) do
begin
	writeln('Digite uma nota válida');
	read(nota2);
end;
	
	
	
	nota := (nota1+nota2)/2;
	
	if ( nota>= 7 ) then 
	begin 
		writeln('O aluno passou direto');
	end
	
	else if ( nota >= 5) and (nota < 7 ) then
	begin
		writeln('Aluno em prova final')
	end
	
	else
	begin
		writeln('Aluno reprovado');	
	end;
		
End.