
- [Paper](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5499584/)
- SYNseq: 

### prerequisites

- in situ: 在生物学实验上，in situ是指进行于原发生位置的试验（而不是将其移入特殊培养基中），有时意义大致介于in vivo与in vitro之间。当研究者对某一处于人工环境下的器官中之特定细胞作实验时，就可称为in situ。由于不在完整活体中，因此不是in vivo；也不是单纯以人工环境下的细胞作实验，因此也不是in vitro。例如分子生物学上一种用来测定特定核酸序列位置的原位杂交（In situ hybridization）技术，就是一种针对特定组织所作的in situ实验。

- 免疫沉淀(Immunoprecipitation, IP): 水溶性抗原遇到特异性抗体，结合而形成抗原-抗体复合物在水溶液中沉淀的现象

- elution: is the process of extracting one material from another by washing with a solvent

- epitope: the part of an antigen molecule to which an antibody attaches itself

- mCherry: is a member of the mFruits family of monomeric **red fluorescent proteins (mRFPs)**

- HEK cells: Human embryonic kidney 293 cells, are a specific **immortalised** cell line.

- Western blot: 蛋白质转渍法, 利用特定抗体能够专一结合其抗原蛋白质的原理来对样品进行着色，通过分析着色的位置和着色深度获得**特定蛋白质在所分析的细胞或组织中的表达情况的信息**，来分析检测特定蛋白质的生物学检测技术。

- ligation: the joining of two DNA strands or other molecules by a phosphate ester linkage 磷酸酯键.

- assay: 化验

### ABSTRACT

- In SYNseq, each neuron is labeled with a unique random nucleotide sequence—an RNA 'barcode'—which is targeted to the synapse using engineered proteins. 
    - Barcodes in pre- and postsynaptic neurons are then associated through protein-protein crosslinking across the synapse, extracted from the tissue, and joined into a form suitable for sequencing. 
    - Although our **failure to develop an efficient barcode joining scheme** precludes the widespread application of this approach, we expect that with further development SYNseq will enable tracing of complex circuits at high speed and low cost.

### INTRODUCTION

<div class="ctr"><img src="/NeuroNotes/img/p5.png" width="100%"/></div>

- (A) First, we express random mRNA barcodes and modified synaptic proteins in a separate population of pre- and postsynaptic neurons, so that each neuron is **uniquely** labeled with a different barcode sequence (compare ref (17,18)).
    - 17: **NOT unique** `2016 MAPseq` [High-Throughput Mapping of Single-Neuron Projections by **Sequencing** of **barcoded** RNA.](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6640135/)
    - 18: **unique** `2016 Virus` [A New Defective Helper RNA to Produce Recombinant Sindbis Virus that Infects Neurons but does not Propagate.](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4877524/)

<div class="ctr">
    <h3>2016 MAPseq</h3>
    <img src="/NeuroNotes/img/p6.png" width="300"/>
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

#### Neuronal barcodes

We have previously developed a Sindbis-based system for over-expression of neuronal barcodes, which was used to map projections (`MAPseq`). This work revealed that unique barcodes can be efficiently targeted to individual neurons, and **amplified through the Sindbis virus system**. In this expression system each virus particle carries a unique RNA barcode, which is **extensively replicated after infection by the machinery of the Sindbis virus**, and is flanked by sequences that allow for efficient recovery and sequencing. In this work, we sought to extend the MAPseq system by developing **proteins that could specifically target barcodes to the pre- and post-synaptic density, and enable recovery of barcode pairs across individual synapses.**

#### Protein design

- In order to enable recovery of synaptic connectivity from neuronal barcodes, we developed a pair of SYNseq carrier proteins that conform to three requirements. 
    - First, we required that they traffic to the pre- and postsynaptic terminals, respectively. 
        - we started with the presynaptic protein `Nrx1B` and the postsynaptic protein `Nlg1AB`. Both are relatively simple, single pass membrane proteins that **traffic naturally to the appropriate side of a mammalian synapse.**
    - Second, we required that the pre- and postsynaptic components be in a form that allowed for synapse-specific covalent cross-linking. 
        - To permit crosslinking of the proteins across the synapse, we fused the self-labeling proteins `CLIP` and `SNAP` to the extracellular domains of `Nrx1B` and `Nlg1AB`, respectively. `CLIP` and `SNAP` are engineered versions of a **DNA repair enzyme that specifically react and form a covalent bond with benzylcytosine (BC) and benzylguanine (BG), respectively.** To crosslink the `CLIP` and `SNAP` domains, we synthesized a bi-functional small molecule that contains `BC` on one end, and `BG` on the other, and is **thus capable of forming a covalent bond between our pre- and postsynaptic proteins.** In addition, this crosslinker contains a `biotin` 生物素 functional group that allows efficient immunoprecipitation (IP). A second version of the crosslinker further allows for elution from beads after IP for biotin via a cleavable disulfide bridge 可裂解二硫键. The two versions of the crosslinker (`BG–PEG–biotin–PEG–BC` and `BG–PEG–(S–S)–biotin–PEG–BC`) behave largely identically and we used them interchangeably in this study, unless elution was necessary. Finally, we fused a `Myc` epitope tag to `Nrx1B`, and an `HA` epitope tag to `Nlg1AB`, to aid in biochemistry and/or visualization.
    - Finally, we required that they bind the barcode mRNA tightly and specifically.
        - To enable these proteins to carry barcode mRNAs, we inserted the RNA binding domain `nλ` into the **cytoplasmic tail** of the two proteins. The `nλ` domain is a 22 amino acid peptide (derived from the `λN` protein of `λ` bacteriophage 噬菌体) that **specifically and strongly binds to a particular 15 nt RNA sequence, termed `boxB`.** We also added the corresponding `boxB` sequence to the barcode mRNA, causing the association of SYNseq proteins and barcode mRNAs.

The design of proteins that fulfilled all of the above requirements necessitated considerable troubleshooting. We tested various positions, RNA binding domains, and linker structures before finding a pair of proteins in which our modifications to Nrx1B and Nlg1AB did not disrupt the proteins' endogenous trafficking pattern. For ease of use and fast turnaround, we performed initial troubleshooting and benchmarking of different constructs by expression and co-expression in HEK cell culture. We then tested promising proteins for the more stringent criteria of synaptic localization and RNA binding in neuronal culture.


#### Barcode mRNA design

The barcode mRNAs necessary for SYNseq underwent few changes from the initial design. Both pre- and postsynaptic barcode RNA carry a random 30 nt barcode sequence in their `5' UTR`, and four copies of the `boxB` sequence, which allows tight association of the barcode RNA to the SYNseq proteins, in the `3' UTR`. Finally, we introduced the coding sequences for `GFP` and `mCherry` into the presynaptic and postsynaptic barcode mRNAs, respectively.

<details>
<summary>

Step 1: SYNseq proteins `traffic` to the membrane, can be `crosslinked` and `bind` barcode mRNA in **HEK cell culture**

</summary>


<div class="ctr">
    <img src="/NeuroNotes/img/p14.png" width="300"/>
</div>

After troubleshooting, we focused on two proteins, `Myc-CLIP-Nrx1B-1xnλ (synPRE-P)` and `HA-SNAP-Nlg1AB-1xnλ (synPOST-P)`, for further testing. Each contained a single repeat of `nλ` surrounded by long flexible linker sequences in their cytoplasmic tail, in a position that was previously reported not to disrupt the proteins' endogenous trafficking. The matching barcode mRNAs encode for `GFP` and `mCherry`, respectively, contain a `random 30 nt barcode sequence` in their `5΄ UTR`, and have four repeats of the `boxB` stem loop in their `3΄UTR`.

- We first examined the localization of the two proteins. Both `synPRE-P` and `synPOST-P` traffic to the HEK cell membrane, as demonstrated by surface staining. This indicates that at least rudimentary **trafficking** of the proteins is uninterrupted by the addition of crosslinking and RNA binding domains.

- We next tested whether we could specifically crosslink `synPRE-P` and `synPOST-P` in a simple scenario. We incubated HEK cells expressing `synPRE-P` and/or `synPOST-P` with the crosslinker, and performed an `IP` for the biotin on the crosslinker. We only detect a 'crosslinked' `synPRE-P—synPOST-P` band (**arrow**) in addition to the signals of the individual `synPRE-P` and `synPOST-P` proteins (**star**), when both synPRE-P and synPOST-P proteins are expressed in the cells, and the crosslinker is added before cell lysis. Importantly, we do not detect this crosslinked band when only one of the two proteins is expressed or when the second protein was added post-lysis. Moreover, the crosslinker is inactive in the lysis buffer and does not result in nonspecific bands. These results **indicate that we can form covalent synPRE-P—synPOST-P protein complexes**, and that post-lysis 裂解后 association of synPRE-P and synPOST-P is low.

<div class="ctr">
    <img src="/NeuroNotes/img/p15.png" width="300"/>
</div>

- Finally, we confirmed that `synPRE-P` and `synPOST-P` specifically bind to barcode mRNA. After expression of either `synPRE-P` or `synPOST-P` in HEK cell culture and incubation with the biotinylated 生物素化 crosslinker, we find that barcode RNA is specifically enriched >32-fold by a pulldown for the biotinylated crosslinker. Importantly, the protein-RNA interaction depends on the presence of both the RNA binding domain `nλ` and its RNA recognition sequence `boxB`.
    - `synPRE-P` and `synPOST-P` **specifically and strongly** bind to their respective barcode mRNAs as evident in RNA-IPs from transiently transfected HEK cells, after membrane tagging with `BG–PEG–biotin–PEG–BC`. We show `qRT-PCR` analysis of three independent RNA-IP experiments and western blot analysis of a representative sample.

From these experiments, we **confirm that `synPRE-P` and `synPOST-P` fulfill basic requirements for SYNseq proteins in HEK cell culture: membrane trafficking, efficient crosslinking and barcode mRNA binding.** To further confirm these properties, we turned to more sensitive assays using neuronal cell culture.

</details>

<details>
<summary>

Step 2: SYNseq proteins `traffic` to synapses in **neuronal cell culture** and can be `crosslinked` into transsynaptic complexes. (no need to check again `binding` barcode mRNA in this step)

</summary>

- check trafficking
    - We used a double promoter Sindbis virus to express both the synPRE-P or synPOST-P protein and the pre- or postsynaptic barcode mRNA from a single virus, ensuring that SYNseq protein expression is always coupled with barcode mRNA expression. 
    - Sindbis virus is a positive strand RNA virus, characterized by a large (up to 6 kb) payload as well as rapid and strong expression of transgenes. It therefore allows for rapid turnaround and iteration of constructs during troubleshooting. 
    - In addition, we have previously shown that Sindbis virus can be used to produce high diversity barcode libraries and can uniquely label neurons. The Sindbis virus was thus well-suited to act as an expression vehicle for assessing SYNseq feasibility. 
    - Surface staining for Sindbis-expressed SYNseq proteins with CLIP-Surface488 (synPRE-P) and SNAP-Surface488 (synPOST-P) **confirmed that our protein modifications did not interfere with proper trafficking** of each protein to the cell membrane in neurons.

<div class="ctr">
    <img src="/NeuroNotes/img/p16.png" width="100%"/>
</div>

- check crosslinking 
    - We then used the proximity ligation assay (PLA) to screen for protein pairs that interact across synapses. PLA is a double antibody stain that results in a highly amplified signal only if the two probed epitopes are within 40 nm of each other. This interaction length is comparable to the dimensions of a synaptic cleft 间隙(20 nm). The presence of a PLA signal between a pre- and a postsynaptic protein expressed in separate, but synaptically coupled populations of neurons thus provided a **necessary but not sufficient criterion for establishing the synaptic localization of the two proteins**. These experiments thus served as a screen for candidate protein pairs to be later tested in more stringent assays that restrict the interaction distance to <5 nm.
    - To achieve expression of `synPRE-P` and `synPOST-P` in separate, but synaptically coupled populations of neurons, we grew cultured primary hippocampal neurons in a `XONA` microfluidic device. In a XONA, two chambers containing primary neurons are connected via long, thin microfluidic grooves 凹槽. The setup ensures fluidic isolation of the two neural populations, allowing independent viral infection of the two populations, while permitting the growth of axons between chambers through the groves.
    - We infected one population of cells with Sindbis virus expressing the pre-synaptic components and the other population of cells with Sindbis virus expressing the post-synaptic components. Using **PLA** we detected interaction between the `synPRE-P` and `synPOST-P` proteins preferentially where presynaptic (GFP positive) axons reach the postsynaptic chamber, **suggesting that our proteins come within at least 40 nm of each other across separate but synaptically coupled cell populations.**
    - PLA was a rapid and convenient screening tool to troubleshoot protein design. However, its interaction distance of 40 nm is too large to confirm synaptic co-localization of synPRE-P and POST. 
    - In contrast, the **bifunctional crosslinker designed to create the trans-synaptic synPRE-P—synPOST-P complex is only 4 nm long**. Thus, the creation of a synPRE-P—synPOST-P complex across synaptically coupled neuronal populations necessarily implies that the two proteins came within 4 nm of each other, satisfying even the strictest distance-based definitions of a synapse. **Again expressing synPRE-P and synPOST-P in synaptically coupled but separate neuronal populations using a XONA device, we found that we could specifically crosslink and immunoprecipitate synPRE-P and synPOST-P across the two populations of neurons, and by that logic, synapses.** Note that, to simplify biochemistry from neuronal culture, we used a version of synPRE-P that contains a `3xFLAG` epitope tag in addition to the `myc` epitope tag in this and all subsequent experiments.
    - When we immunoprecipitated crosslinked neuron samples from XONA cultures using the biotin tag on the crosslinker, we can detect at least three major products. 
    - First, we recover the desired `synPRE-P—synPOST-P` complex formed by interaction of the proteins across the synaptic cleft. **However, we also observe signals arising from single synPRE-P and synPOST-P proteins** that reacted with the one side of the crosslinker, but which have no partner on the other side of the crosslinker. Such unpaired single proteins occur from at least three processes: from incomplete crosslinking across a synapse, from synapses at which only one side expresses a SYNseq protein, as well as from expression of either synPRE-P or synPOST-P in regions of the neuronal membrane that are not part of a synapse. **Unfortunately, these unpaired proteins present a challenge to many barcode mRNA joining strategies.** We therefore sought to remove them from the IP reaction by performing a double IP, selecting first for the postsynaptic HA tag, then for the presynaptic `3xFLAG` tag, so that only proteins that contain both synPRE-P and synPOST-P remain after the second IP step. **This strategy efficiently removed all unpaired synPRE-P or synPOST-P proteins from the IP and enriches for the transsynaptic protein complex.**
- check binding
    - no need since this is independant of the cell type, already checked by **HEK cell culture**
- From these results, we conclude that `synPRE-P` and `synPOST-P` conform to all three requirements that we had set out for SYNseq proteins: They specifically bind to barcode mRNA, traffic to synapses and can be specifically joined into a transsynaptic protein complex.

<div class="ctr">
    <h3>check crosslinking using PLA (40nm)</h3>
    <img src="/NeuroNotes/img/p17.png" width="100%"/>
    <h3>check crosslinking using bifunctional crosslinker (4nm)</h3>
    <img src="/NeuroNotes/img/p18.png" width="300"/>
</div>

</details>

#### Joining pre- and postsynaptic barcode mRNAs by emulsion RT-PCR

### DISCUSSION