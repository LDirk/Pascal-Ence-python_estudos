         Program Pzim ;
	const
		max = 5;
		
	Type	
		cadastro_voo = record
			numero:string;
			cidadeO: string;
			cidadeD: string;
			data: string;
			Hp: string;
			Hc: string;
		end;

	var 
		voo:cadastro_voo;
		i: integer;
		array_voo: array[1..max] of cadastro_voo;
Begin

i:= 1;

while ( i <= max) do                              
begin
		writeln('Informe o numero do',i,'voo');
		read(array_voo[i].numero);
		writeln('Informe a cidade de origem do voo', i ,'voo');
		read(array_voo[i].cidadeO);
		writeln('Informe a cidade de destino do voo', i,'voo');
		read(array_voo[i].cidadeD);
		writeln('Informe a data do voo', i,'voo'
		);
		read(array_voo[i].data);
		writeln('Informe o horario de partida do ', i,'voo');
		read(array_voo[i].Hp);
		writeln('Informe o horario chegada do ' , i, 'voo');
		read(array_voo[i].Hc);
		i := i + 1
end; 
writeln('Pressione enter para exibir os dados');
readkey;

i :=  1;
while (i <= max) do
begin
	writeln;
	writeln('Dados do -', i , ' - voo');
	writeln('Numero:  ' ,array_voo[i].numero);
	writeln('Cidade de origem:  ' ,array_voo[i].cidadeO);
	writeln('Cidade de destino:  ', array_voo[i].cidadeD);
	writeln('Data do voo:  ', array_voo[i].data);
	writeln('Horario de partida do voo: ', array_voo[i].Hp);
	writeln('Horario de chegada do voo: ' ,array_voo[i].Hc);
	i := i+ 1
end;
End.