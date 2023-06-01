## Daniel J. Groso
## Updated September 2022

new_dict = {}
with open('/Users/dgroso/RStudio/01-WANG-LAB/01-RNA-LOCALIZATION-PROJECT/01-DE/mart_export_for_deseq.txt', 'r') as biomart: #path to biomart outfile
    for line in biomart: 
        k = line.split()
        try:
            new_dict[k[1]] = k[4] #key = stable ENS ID, value = gene name
        except KeyError:
            new_dict[k[1]] = '' #raise exception if the ENS ID is not in the file
biomart.close()
```

###### GET GENE NAMES ######
# first, convert deseq csv to tsv / text file with a webtool or other script
with open('/Users/dgroso/RStudio/01-WANG-LAB/01-RNA-LOCALIZATION-PROJECT/01-DE/deseq_out_as_tabs.txt', 'a+') as deseqout: 
    with open('/Users/dgroso/RStudio/01-WANG-LAB/01-RNA-LOCALIZATION-PROJECT/03-DE-KALLISTO/deseq_parsed.tsv', 'w') as newout: # writing to new file. will need to edit with bash commands or manually after
        deseqout.seek(0)
        for line in deseqout:
            vals1 = line.split()
            try:           
                genename = new_dict[vals1[1]]
                data = line[:-1] + '\t' + genename
                newout.write(data + '\n')
            except KeyError:
              pass
deseqout.close()
# parsed file will not have column headers, but can create with bash script create_headers_biomart.sh
