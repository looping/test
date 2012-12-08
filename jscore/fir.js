


function getBestMachMove(map, size, flag) {

	s=new Array();
	q=new Array();
	iMax=new Array();
	jMax=new Array();
	nMax=0;
	for (i=0;i<20;i++) {
		s[i]=new Array();
		q[i]=new Array();
		for (j=0;j<20;j++) {
			s[i][j]=0;
			q[i][j]=0;
		}
	}
	maxS=evaluatePos(s, map, size, flag);
	maxQ=evaluatePos(q, map, size, flag + 2);

	//alert ('maxS='+maxS+', maxQ='+maxQ);

	if (maxQ>=maxS) {
		maxS=-1;
		for (i=0;i<size;i++) {
			for (j=0;j<size;j++) {
				if (q[i][j]==maxQ) {
					if (s[i][j]>maxS) {
						maxS=s[i][j]; 
						nMax=0;
					}
					if (s[i][j]==maxS) {
						iMax[nMax]=i;
						jMax[nMax]=j;
						nMax++;
					} 
				}
			}
		}
	} else {
		maxQ=-1;
		for (i=0;i<size;i++) {
			for (j=0;j<size;j++) {
				if (s[i][j]==maxS) {
					if (q[i][j]>maxQ) {
						maxQ=q[i][j]; 
						nMax=0;
					}
					if (q[i][j]==maxQ) {
						iMax[nMax]=i;
						jMax[nMax]=j;
						nMax++;
					} 
				}
			}
		}
	}
	// alert('nMax='+nMax+'\niMax: '+iMax+'\njMax: '+jMax)

	var h = nMax;
	var minS = 9999999;
	var minIndex = 0;
	//document.getElementById("debug").innerHTML = '';
	while(h){
		h--;
		map[iMax[h]][jMax[h]] = flag;
		var tminS =evaluatePos(s, map, size, flag - 2);
		map[iMax[h]][jMax[h]] = 0;
		document.getElementById("debug").innerHTML += 'Otest point('+(iMax[h])+','+(jMax[h])+') value : '+(tminS)+'<br />';

		if(minS > tminS){
			minS = tminS;
			minIndex = h;		
		}	
	}
	//randomK=Math.floor(nMax*Math.random());
	var pos = new Array();
	pos[0] = iMax[minIndex];
	pos[1] = jMax[minIndex];
	document.getElementById("debug").innerHTML += 'Oselect point('+(pos[0])+','+(pos[1])+') value : '+(minS)+'<br />';
	return pos;
}
var h = 2;
function getBestUserMove(map, size, flag) {
	s=new Array();
	q=new Array();
	iMax=new Array();
	jMax=new Array();
	nMax=0;
	for (i=0;i<20;i++) {
		s[i]=new Array();
		q[i]=new Array();
		for (j=0;j<20;j++) {
			s[i][j]=0;
			q[i][j]=0;
		}
	}
	maxQ=evaluatePos(q, map, size, flag);
	maxS=evaluatePos(s, map, size, flag - 2);

	if (maxS==-1) {
		center=Math.floor(size/2);
		s[center][center]=1
		maxS=1; 
	}

	if (maxS>=maxQ) {
		maxQ=-1;
		for (i=0;i<size;i++) {
			for (j=0;j<size;j++) {
				if (s[i][j]==maxS) {
					if (q[i][j]>maxQ) {
						maxQ=q[i][j];
						nMax=0;
					}
					if (q[i][j]==maxQ) {
						iMax[nMax]=i;
						jMax[nMax]=j;
						nMax++;
					} 
				}
			}
		}
	} else {
		maxS=-1;
		for (i=0;i<size;i++) {
			for (j=0;j<size;j++) {
				if (q[i][j]==maxQ) {
					if (s[i][j]>maxS) {
						maxS=s[i][j]; 
						nMax=0;
					}
					if (s[i][j]==maxS) {
						iMax[nMax]=i;
						jMax[nMax]=j;
						nMax++;
					} 
				}
			}
		}
	}

	// alert('nMax='+nMax+'\niMax: '+iMax+'\njMax: '+jMax)
	var h = nMax;
	var minS = 9999999;
	var minIndex = 0;
	//document.getElementById("debug").innerHTML = '';
	while(h){
		h--;
		map[iMax[h]][jMax[h]] = flag;
		var tminS =evaluatePos(s, map, size, flag - 2);
		map[iMax[h]][jMax[h]] = 0;
		document.getElementById("debug").innerHTML += 'Xtest point('+(iMax[h])+','+(jMax[h])+') value : '+(tminS)+'<br />';

		if(minS > tminS){
			minS = tminS;
			minIndex = h;		
		}	
	}
	//randomK=Math.floor(nMax*Math.random());
	var pos = new Array();
	pos[0] = iMax[minIndex];
	pos[1] = jMax[minIndex];
	document.getElementById("debug").innerHTML += 'Xselect point('+(pos[0])+','+(pos[1])+') value : '+(minS)+'<br />';
	return pos;
	
}
function evaluatePos(a, map, size, mySq)
{
	maxA=-1;
	drawPos=true;
	w=new Array(0,20,17,15.4,14,10);
	nPos=new Array();
	dirA=new Array();
	for (i=0;i<size;i++) {
		for (j=0;j<size;j++) {

			// Compute "value" a[i][j] of the (i,j) move

			if (map[i][j]!=0){
				a[i][j]=-1; 
				continue;
			}  
			if (hasNeighbors(i, j, map, size)==0){
				a[i][j]=-1; 
				continue;
			}

			wp=winningPos(i,j,mySq);
			if (wp>0){
				a[i][j]=wp;
			}else {
				minM=i-4; if (minM<0) minM=0;
				minN=j-4; if (minN<0) minN=0;
				maxM=i+5; if (maxM>size) maxM=size;
				maxN=j+5; if (maxN>size) maxN=size;

				nPos[1]=1; A1=0;
				m=1;
				while (j+m<maxN  && map[i][j+m]!=-mySq) {
					nPos[1]++;
					A1+=w[m]*map[i][j+m];
					m++;
				}
				if (j+m>=size || map[i][j+m]==-mySq){
					A1-=(map[i][j+m-1]==mySq)?(w[5]*mySq):0;
				}
				m=1;
				while (j-m>=minN && map[i][j-m]!=-mySq){
					nPos[1]++; A1+=w[m]*map[i][j-m];
					m++;
				}   
				if (j-m<0 || map[i][j-m]==-mySq){
					A1-=(map[i][j-m+1]==mySq)?(w[5]*mySq):0;
				}
				if (nPos[1]>4){
					drawPos=false;
				}

				nPos[2]=1;
				A2=0;
				m=1; 
				while (i+m<maxM  && map[i+m][j]!=-mySq) {
					nPos[2]++;
					A2+=w[m]*map[i+m][j];
					m++;
				}
				if (i+m>=size || map[i+m][j]==-mySq){
					A2-=(map[i+m-1][j]==mySq)?(w[5]*mySq):0;
				}
				m=1;
				while (i-m>=minM && map[i-m][j]!=-mySq){
					nPos[2]++;
					A2+=w[m]*map[i-m][j];
					m++;
				}   
				if (i-m<0 || map[i-m][j]==-mySq){
					A2-=(map[i-m+1][j]==mySq)?(w[5]*mySq):0; 
				}
				if (nPos[2]>4){
					drawPos=false;
				}

				nPos[3]=1;
				A3=0;
				m=1;
				while (i+m<maxM  && j+m<maxN  && map[i+m][j+m]!=-mySq){
					nPos[3]++; 
					A3+=w[m]*map[i+m][j+m];
					m++;
				}
				if (i+m>=size || j+m>=size || map[i+m][j+m]==-mySq){
					A3-=(map[i+m-1][j+m-1]==mySq)?(w[5]*mySq):0;
				}
				m=1;
				while (i-m>=minM && j-m>=minN && map[i-m][j-m]!=-mySq) {
					nPos[3]++;
					A3+=w[m]*map[i-m][j-m];
					m++;
				}   
				if (i-m<0 || j-m<0 || map[i-m][j-m]==-mySq){
					A3-=(map[i-m+1][j-m+1]==mySq)?(w[5]*mySq):0; 
				}
				if (nPos[3]>4){
					drawPos=false;
				}

				nPos[4]=1; A4=0;
				m=1; 
				while (i+m<maxM  && j-m>=minN && map[i+m][j-m]!=-mySq) {
					nPos[4]++;
					A4+=w[m]*map[i+m][j-m];
					m++;
				}
				if (i+m>=size || j-m<0 || map[i+m][j-m]==-mySq){
					A4-=(map[i+m-1][j-m+1]==mySq)?(w[5]*mySq):0;
				}
				m=1;
				while (i-m>=minM && j+m<maxN  && map[i-m][j+m]!=-mySq){
					nPos[4]++;
					A4+=w[m]*map[i-m][j+m];
					m++;
				} 
				if (i-m<0 || j+m>=size || map[i-m][j+m]==-mySq){
					A4-=(map[i-m+1][j+m-1]==mySq)?(w[5]*mySq):0;
				}
				if (nPos[4]>4){
					drawPos=false;
				}

				dirA[1] = (nPos[1]>4) ? A1*A1 : 0;
				dirA[2] = (nPos[2]>4) ? A2*A2 : 0;
				dirA[3] = (nPos[3]>4) ? A3*A3 : 0;
				dirA[4] = (nPos[4]>4) ? A4*A4 : 0;

				A1=0; A2=0;
				for (k=1;k<5;k++) {
					if (dirA[k]>=A1) {
						A2=A1;
						A1=dirA[k];
					}
				}
				a[i][j]=A1+A2;
			}
			if (a[i][j]>maxA) {
				maxA=a[i][j];
			}
		}
	}
	return maxA;
}
function hasNeighbors(i, j, map, size) 
{
	if (j>0 && map[i][j-1]!=0) return 1;
	if (j+1<size && map[i][j+1]!=0) return 1; 
	if (i>0) {
		if (map[i-1][j]!=0) return 1;
		if (j>0 && map[i-1][j-1]!=0) return 1;
		if (j+1<size && map[i-1][j+1]!=0) return 1;
	}
	if (i+1<size) {
		if (map[i+1][j]!=0) return 1;
		if (j>0 && map[i+1][j-1]!=0) return 1;
		if (j+1<size && map[i+1][j+1]!=0) return 1;
	}
	return 0;

}

