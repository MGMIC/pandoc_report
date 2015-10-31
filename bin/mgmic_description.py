qc_desc="The QC component of MGMIC proceeds via several step. Initially quality is assessed via FastQC.  Subsequently Nextera and Illumina adapters are detected and removed via a combination of custom scripts integrated with TrimGalore and Cutadapt (Martin 2011).  Reads are then trimmed to a quality score of 30 and poly-AAA tails and artifacts are removed via HomerTools.  Trimmomatic is applied to screen sequences for a minimum length of 100 bp. Unpaired reads are removed and sequences are converted to fasta format via Biopieces. Finally, FastQC is re-run to assess the success of quality screening."
qc_desc_off="The QC component of MGMIC workflow was turned off. The Quality Control section will only show the quality of the original files submitted."
s16_desc = "16S rRNA gene sequences are detected in metagenome datasets via Usearch (Edgar 2010) comparison to the Silva 111 small subunit rRNA reference alignment (www.arb-silva.de). All reads with >70% identify over a 100 bp fragment to the Silva database are extracted and then classified via closed reference picking in relation to the Silva 118 reference alignment via QIIME.  For 16S PCR products, sequences are clustered and classified using the QIIME pipeline after de-multiplexing and clustering into Operational Taxonomic Units (OTUs) via UCLUST (Edgar 2010) at the 97% identity level.  From the resulting OTUs, a representative set of sequences was aligned to the SILVA small subunit rRNA reference alignment (www.arb-silva.de) using the PyNAST algorithm (Caporaso et al. 2010) to allow classification. Krona graphs are generated from the L6 taxonomic assignment produced by QIIME."
assemble_desc = "Reads are assembled using Meta-Ray (Boisvert et al. 2010, Boisvert et al. 2012) using a Kmer setting of 31 and discarding all contigs <500bp.  Open reading frames (ORFs) were predicted for all contigs using Prodigal (Hyatt et al. 2012). Tetranucleotide frequency based analysis was used to bin assembled DNA sequence data into genome scaffolds using MaxBin (Wu et al. 2014)."
fgs_desc ="Individual gene databases were generated by mining the IMG database of complete genomes.  Database searches are performed using USEARCH (Edgar 2010) by setting a minimum overlap of 50 columns and 70% identify.  Frequencies are calculated as RPKM (reads per kb per megabase). RPKM  is calculates as = (reads / exon length) * (1,000,000 / mapped reads). For example, suppose a gene has 50 reads that map to it, with a gene length of 7000 bp ( = 7.0 kbp), and there are 5,000,000 reads in that sample. The RPKM value is:  500/(7.000)  (1,000,000/5,000,000) = 14.28 RPKM reads. The value is multiplied by 50 here to estimate approximate what proportion of cells in a sample (in %) contain the gene assuming an average genome size of 2Mbp."
