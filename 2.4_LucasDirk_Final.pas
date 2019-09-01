Program Pzim ;
var
	x : integer;
	
	function  fatorial(n:integer):integer;
	begin
		if n = 0 then
			fatorial:= 1;
		if n>= 1 then
			fatorial:= n*(fatorial(n-1));
	end;
Begin
	read(x);
	writeln(fatorial(x));
  
End.
