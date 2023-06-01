#!/usr/bin/bash 

sed -i $'1 i\\ \tEns_ID\tbaseMean\tlog2FoldChange\tlfcSE\tstat\tpvalue\tpadj\tsoma_1\tsoma_2\tsoma_3\tneuropil_1\tneuropil_2\tneuropil_3\tgene_name' deseq_parsed.tsv
