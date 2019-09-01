Program Pzim ;
const
	path = 'C:\temp\texto.txt';
	max = 1;

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
	arquivo: text;
	texto: string;
	array_voo:array[1..max] of cadastro_voo;
	i : integer;
	escolha : integer;	
							
Begin
  assign(arquivo,path);
	escolha := 10;
	
	while (escolha<>0) do
begin
	
	writeln('Menu');
	writeln('1 - gravar voo');
	writeln('2 - voos gravados ');
	writeln('0 - sair');
	write('Digite a opção desejada: ');
	readln(escolha);

 if (escolha=0) then 
 begin 
 		break; 
		close(arquivo); 
 end
 
 else if (escolha=1) then
 begin
 		rewrite(arquivo); 
	  reset(arquivo);
	  
 for i:=1 to max do
 begin

		writeln('ENTRADA DE DADOS DO VOO - ',i);
		writeln;
		
		write('Digite o nUmero do voo: ');
		readln(array_voo[i].numero);
		
		write('Digite a cidade de origem do voo: ');
		readln(array_voo[i].cidadeO);
		
		write('Digite a cidade de destino do voo: ');
		readln(array_voo[i].cidadeD);
		
		write('Digite a data de partida do voo: ');
		readln(array_voo[i].data);
		
		write('Digite a hora de partida do voo: ');
		readln(array_voo[i].Hp);
		
		write('Digite a hora de chegada do voo: ');
		readln(array_voo[i].hc);
 end;
 
 for i:=1 to MAX do             
 begin
   	
		writeln(arquivo);
		writeln(arquivo,'--Dados do voo ---',i);
		writeln(arquivo,'Voo numero ',array_voo[i].numero);
		writeln(arquivo,'Origem', array_voo[i].cidadeO);
		writeln(arquivo,'Destino', array_voo[i].cidadeD);
		writeln(arquivo,'Data do voo', array_voo[i].data);
		writeln(arquivo,'hora do voo', array_voo[i].Hp);
		writeln(arquivo,'Hora de chegada no destino', array_voo[i].Hc);
		writeln(arquivo);
 end;
 
 close(arquivo);
 end

 else if (escolha=2) then 
 begin
 reset(arquivo);

 while not eof(arquivo) do
 begin
		readln(arquivo,texto); 
		writeln(texto); 
 end;
 close(arquivo);
 readkey;
 end 
 
 else 
 begin 
 writeln('Digite uma opção válida');
 readkey;
 end;
 close(arquivo);
End;

 
  
End.