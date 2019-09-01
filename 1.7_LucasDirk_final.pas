Program Pzim ;
	type
		cadastro_voo = record
			numero:real;
			cidadeO: string;
			cidadeD: string;
			data: string;
			Hp: string;
			Hc: string
		end;
	var
		voo:cadastro_voo;
						
Begin
   writeln('Cadastro de voo');
   writeln;
   
   writeln('Informe o numero do voo: ');
   read(voo.numero);
   writeln('Informe a cidade de origem do voo');
   read(voo.cidadeO);
   writeln('Informe o destino do voo');
   read(voo.cidadeD);
   writeln('Informe a data do voo');
   read(voo.data);
   writeln('Informe o horario de partida do voo');
   read(voo.Hp);
   writeln('Informe o horario de chegada do voo');
   read(voo.Hc);
   
  
   
   writeln('numero do voo:', voo.numero:3:1);
   writeln('Cidade de origem do voo:', voo.cidadeO);
   writeln('Cidade de destino do voo', voo.cidadeD);
   writeln('Data do voo', voo.data);
   writeln('Horario de partida do voo', voo.Hp);
   writeln('Horario de chegada do voo', voo.Hc);
      
   
   writeln('tecle [enter] para encerrar');
   readln;
End.