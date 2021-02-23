# **Report about Galaxy training**

I participated virtually in the GTN Smörgåsbord: A Global Galaxy Course from 15th to 19th February 2021. The course had slides, videos and hands on tutorial so 
that one can learn how to carryout data analysis using tools available on Galaxy servers.
---
### ***Skills learnt**
1. Performing Quality control on FASTQ files.
   Quality control is an essential step which should be carried out before any downstream analysis of your data. This is important so that one can know the status
   of their sequence files which can affect further analysis when not inspected earlier. Galaxy offers FastQC tool which provides a summary of the quality of your 
   sequenced data. It gives a report on the sequence quality score to the level of seqeunce duplications. Through assesing the quality of FASTQ files, further tools
   can then be used for quality correction depending on the output of FastQC, such tools include:
    a) Cutadapt- which trims adapters from the sequence, and also trims the low quality score regions.
    b) Filter- This tool filters your FASTQ files based if there are too many N basecalls in the sequence, filters off the short sequence length and sequences with
       low mean quality score.
    c) MultiQC- This tool aggregates the ouput of the a specified tool in this case, FastQC reports into one report thus making it easier to compare different files 
       at once.
