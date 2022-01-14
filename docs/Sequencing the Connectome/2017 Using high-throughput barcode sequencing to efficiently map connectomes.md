
- [Paper](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5499584/)
- SYNseq: 

### prerequisites

- in situ: 在生物学实验上，in situ是指进行于原发生位置的试验（而不是将其移入特殊培养基中），有时意义大致介于in vivo与in vitro之间。当研究者对某一处于人工环境下的器官中之特定细胞作实验时，就可称为in situ。由于不在完整活体中，因此不是in vivo；也不是单纯以人工环境下的细胞作实验，因此也不是in vitro。例如分子生物学上一种用来测定特定核酸序列位置的原位杂交（In situ hybridization）技术，就是一种针对特定组织所作的in situ实验。

### ABSTRACT

- In SYNseq, each neuron is labeled with a unique random nucleotide sequence—an RNA 'barcode'—which is targeted to the synapse using engineered proteins. 
    - Barcodes in pre- and postsynaptic neurons are then associated through protein-protein crosslinking across the synapse, extracted from the tissue, and joined into a form suitable for sequencing. 
    - Although our **failure to develop an efficient barcode joining scheme** precludes the widespread application of this approach, we expect that with further development SYNseq will enable tracing of complex circuits at high speed and low cost.

### INTRODUCTION

<div class="ctr"><img src="/img/p5.png" width="100%"/></div>

- (A) First, we express random mRNA barcodes and modified synaptic proteins in a separate population of pre- and postsynaptic neurons, so that each neuron is **uniquely** labeled with a different barcode sequence (compare ref (17,18)).
    - 17: **NOT unique** `2016 MAPseq` [High-Throughput Mapping of Single-Neuron Projections by **Sequencing** of **barcoded** RNA.](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6640135/)
    - 18: **unique** `2016 Virus` [A New Defective Helper RNA to Produce Recombinant Sindbis Virus that Infects Neurons but does not Propagate.](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4877524/)

<div class="ctr">
    <h3>2016 MAPseq</h3>
    <img src="/img/p6.png" width="300"/>
</div>

- The modified synaptic proteins specifically bind the mRNA barcodes via an RNA binding domain, thereby trafficking barcodes to the pre- (left) or postsynaptic (right) compartments, respectively. The proteins meet at the synapse. 

- (B) Next, the pre- and postsynaptic proteins are cross-linked in situ using a custom synthetic bivalent linker, which covalently joins the extracellular domains of the pre- and postsynaptic proteins. The resulting complexes, consisting of covalently bound pre- and postsynaptic protein pairs bound via the RNA binding domain to their respective barcodes, are then purified via immunoprecipitation (IP). 

- (C) The associated barcode pairs, which represent pairs of connected neurons, are joined, amplified, and sequenced. 

- (D) Sequencing data then allows the reconstruction of a connectivity matrix.

---

- SYNseq consists of four steps: 
    - neuronal barcoding 
    - trafficking of barcodes to the synapses via tight association with engineered synaptic proteins 
        - a pre-synaptic mRNA barcode is trafficked to the presynaptic terminal via association with an engineered version of the Neurexin1B (Nrx1B) protein 
        - Likewise, the postsynaptic barcode is trafficked to the postsynaptic terminal via association with a modified Neuroligin1AB (Nlg1AB) protein
    - joining of barcodes into a form suitable for sequencing
        - Across a synapse, the presynaptic SYNseq components are covalently linked to the postsynaptic SYNseq components and then immunoprecipitated for further biochemical manipulation to link the pre- and postsynaptic barcodes.
    - and reconstruction of the network connectivity 

- We develop a set of reagents that allow for synaptic trafficking of barcodes, specific crosslinking of carrier proteins across synapses, and recovery and joining of the barcode pairs that define a specific synapse. 
- **Unfortunately, however, the efficiency of the last step—barcode joining—is in our hands insufficient to provide for reliable synapse recovery while avoiding false positives.**
- Despite this shortcoming, our work lays the foundation for using high-throughput DNA sequencing for circuit reconstruction. Future improvements upon SYNseq have the potential to enable high-throughput connectomics, opening up many new avenues of research in neuroscience.

### MATERIALS AND METHODS

# TODO

### RESULTS

