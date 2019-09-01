Program Pzim ;
var
	palavra,palavrai: string;
	i :integer;
	
Begin

	write('Escreva a palavra: ');
	read(palavra);
	palavrai := '';
	
	for i:=length(palavra) downto 1 do
		palavrai := palavrai + palavra[i];
		writeln('Voce digitou ', palavra);
		writeln('Ela invertida é: ' , palavrai);
	
End.