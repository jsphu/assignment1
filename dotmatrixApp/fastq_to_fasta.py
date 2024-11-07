if __name__ != "__main__":
	def read_sequences(input_file:str, is_fasta:bool=False):
		if is_fasta:
			output=[]
			fasta=open(input_file,"r").read()
			for index in range(len(fasta.split("\n"))):
				if index % 2==1: output.append(fasta.split("\n")[index])
			return output
		elif is_fasta==False:
			output=[]
			fastq=open(input_file, "r").read()
			for index in range(len(fastq.split("\n"))):
				if index % 4==1: output.append(fastq.split("\n")[index])
			return output

else:
	fastq=open("input.fastq","r").read()
	fasta=list()
	for i in range(2): fasta.append(fastq.split("\n")[i])
	output=("".join(map(str,fasta[0])).replace("@",">")+"\n"+"".join(map(str,fasta[1])))
	out=open("output.fasta","w")
	out.write(output)
	out.close()
