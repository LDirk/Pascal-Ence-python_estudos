Program Pzim ;

	function fib(n:integer):integer;
	begin
		if n = 0 then
			fib := 0;
		if n= 1 then
		 	fib := 1; 
		if n>1 then
		begin
		fib := fib(n-1) + fib(n-2);
		end;
	end;
	var
		numero, contador: integer;
Begin
	  writeln('Digite o tamanho da sequencia de fibonnaci: ');
	  readln(numero);
	  contador := 0;
	  while contador < numero do
	  begin
	  	writeln(fib(contador));
	    contador := contador + 1 ;
		end;
End.
	  
