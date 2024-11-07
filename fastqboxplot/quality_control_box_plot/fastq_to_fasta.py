fastq=open("example.fastq","r").read()
fasta=list()
total=len(open("example.fastq","r").readlines())
for i in range(total):
	if i%4==0 or i%4==1: fasta.append(fastq.split("\n")[i])
out=open("output.fasta","w")
for i in range(0,len(fasta),2): out.write("".join(map(str,fasta[i])).replace("@",">")+"\n"+"".join(map(str,fasta[i+1]))+"\n")
