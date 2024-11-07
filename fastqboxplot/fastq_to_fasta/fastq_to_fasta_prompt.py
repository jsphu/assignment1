prompt=input("which file is fastq?= ")
prompt2=input("where to output results? [Default:'output.fasta']= ")
if prompt2=="":
	prompt2="output.fasta"
fastq=open(prompt,"r").read()
fasta=list()
total=len(open(prompt,"r").readlines())
for i in range(total):
        if i%4==0 or i%4==1:
                fasta.append(fastq.split("\n")[i])
out=open(prompt2,"w")
for i in range(0,len(fasta),2): out.write("".join(map(str,fasta[i])).replace("@",">")+"\n"+"".join(map(str,fasta[i+1]))+"\n")
