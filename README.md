# mikado_compare_test

## get gencode and refseq gtf
curl -O ftp://ftp.ebi.ac.uk/pub/databases/gencode/Gencode_human/release_33/gencode.v33.annotation.gtf.gz
gunzip gencode.v33.annotation.gtf.gz
curl -O https://ftp.ncbi.nlm.nih.gov/genomes/all/GCF/000/001/405/GCF_000001405.39_GRCh38.p13/GCF_000001405.39_GRCh38.p13_genomic.gtf.gz
gunzip GCF_000001405.39_GRCh38.p13_genomic.gtf.gz

## download gencode to refseq chr name maping
curl -O https://raw.githubusercontent.com/dpryan79/ChromosomeMappings/master/GRCh38_RefSeq2UCSC.txt

## convert chr names
python refseq2gencode.py

## run mikado compare
mikado compare -r GCF_000001405.39_GRCh38.p13_genomic_GENCODENAMES.gtf -p gencode.v33.annotation.gtf -l compare_refseq.log -o compare_refseq


