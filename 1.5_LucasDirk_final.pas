Program Pzim ;
var
	Xa,Ya,Xb,Yb,distancia:real;
Begin



	writeln('Digite a coodernada Xa e Ya');
	read(Xa);
	read(Ya);
		
	writeln('Digite a coodernada Xb e Yb' );
	read(Xb);
	read(Yb);
	
	distancia := sqrt((Xa-Xb)*(Xa-Xb) + (Ya-Yb)*(Ya-Yb));
	writeln('A distancia entre os dois pontos é:', distancia)
End.                                          