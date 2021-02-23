# **Galaxy training report**

---
### **Introduction**

[Galaxy](https://galaxyproject.org/community/) is an online platform developed by a community of scientists. This platform is distributed in different regions by presence of [servers](https://galaxyproject.org/usegalaxy/). These servers are accessible virtually and contain various tools which aid in the analysis of different types of data. From galaxy one can access training materials from the galaxy training network (GTN) [page](https://training.galaxyproject.org/). These page consists  of a wide range of tutorials on how to use the inbuilt tools in galaxy to carry out data analysis. From 15th to 19th February 2021, I participated virtually in the GTN Smörgåsbord: [A Global Course](https://training.galaxyproject.org/training-material/smorgasbord.html). This workshop comprised of different GTN tutorials exposing one to a wide range topics during the entire week.

---

### **Objectives**
1. To familiarize with galaxy platform and learn data analysis using galaxy.
2. To understand NGS analysis using galaxy tools.
3. To determine the importance of using certain tools for your data analysis over others.

---

### **Skills learnt**

1. Performing Quality control on FASTQ files.
   Quality control is an essential step which should be carried out before any downstream analysis of your data. This is important so as to know the status of your FASTQ files. When the quality control step is not done during NGS analysis, this can affect downstream analysis.
   
   Galaxy offers FastQC tool which checks the quality of the sequence files, it then provides a report in form of a webpage which outputs parameters relevant to the status of your sequence files. By assessing these parameters such as; sequence quality score, per base sequence quality, one will know the quality of the FASTQ files and whether any quality correction is needed.
   
   There are tools available on galaxy for sequence quality correction depending on the FastQc results. They include:
   
   a). Cutadapt- It trims adapter sequences and also trims off low quality score regions from the files.
   
   b). Filter- This tool filters FASTQ files if there are many N basecalls in the sequence, reads with short sequence length as well those with low mean quality score.
   
   c). MultiQc- This tool is useful in the aggregation of different outputs from a specific tool such as FastQC thus making it easy to compare different results at once.

