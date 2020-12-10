import sys

d={}
with open('GRCh38_RefSeq2UCSC.txt') as f:
    for l in f:
        t=l.strip().split('\t')
        #print(t)
        d[t[0]]=t[1]

#print(d)

with open('GCF_000001405.39_GRCh38.p13_genomic.gtf') as f, open('GCF_000001405.39_GRCh38.p13_genomic_GENCODENAMES.gtf','w') as o:
    for l in f:
        if l.startswith('#'):
            o.write(l)
        else:
            tmp=l.split('\t')
            if not tmp[0] in d:
                #print('Not found in dict {}'.format(tmp[0]),file=sys.stderr)
                continue
            newname=d[tmp[0]]
            tmp[0]=newname
            newline='\t'.join(tmp)
            o.write(newline)

