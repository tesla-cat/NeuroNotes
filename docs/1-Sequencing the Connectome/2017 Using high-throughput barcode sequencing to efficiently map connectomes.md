
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

- With the desired functional properties of `synPRE-P` and `synPOST-P` confirmed, we set out to develop a method for joining RNA barcodes specifically and efficiently. We tested a variety of methods including
    - splinted 夹板 ligation of `RNaseH` trimmed barcode mRNAs by `T4` RNA ligase
    - double-headed ribozymes 核酶 drawing on the `L21` and the `Carinii` ribozyme 
    - barcode joining by reverse transcription where the two barcode RNAs are priming each other 
- before settling on barcode joining by **emulsion 乳胶 reverse transcription-PCR (RT-PCR) followed by overlap PCR**, which had previously proven successful for joining immunoglobulin 免疫球蛋白 mRNAs. 
- Briefly, 
    - we isolate `synPRE-P—synPOST-P` complexes by `IP` and emulsify the complexes using a microfluidic droplet system at a dilution **such that each droplet contains no more than one complex**. 
    - Inside each droplet, we then reverse transcribe the presynaptic and postsynaptic barcode mRNAs and subsequently join them into a single DNA strand by overlap PCR. 
    - We then break the emulsion, isolate the barcode pairs and sequence them on an Illumina sequencing machine.

<div class="ctr">
    <img src="/NeuroNotes/img/p19.png" width="100%"/>
</div>

The success and failure of any method to join barcode mRNAs in SYNseq is measured not simply in the generation of barcode pairs, but critically in the ability of producing barcode pairs from mRNAs in the same complex, but not from mRNAs in different complexes or even unbound mRNAs. When using emulsion RT-PCR to join barcode mRNAs, **such nonspecific joining occurs when more than one synPRE-P—synPOST-P complex, and thus more than one presynaptic or postsynaptic barcode mRNA are loaded into the same droplet**. The fraction of unspecific joining events therefore ultimately depends on the concentration of complexes that are loaded into droplets and decreases with input concentration, as demonstrated by loading droplets with different concentrations of a test RNA that contains the sequences of both pre- and postsynaptic barcodes, but in inverted orientations relative to the final sequencing amplicon.

- To validate the emulsion RT-PCR approach, we first tested joining using protein-RNA complexes derived from **HEK cell culture**. 
    - To measure the rate of nonspecific joining of barcode mRNAs, we set up two experiments in parallel. Each experiment consists of one population of HEK cells that co-express synPRE-P, synPOST-P and barcode mRNAs. In these experiments we used an earlier version of the SYNseq proteins. **The barcode mRNAs in each experiment are tagged with an additional, experiment-specific sequence, a zip code (denoted here as A or B).** We crosslinked and lysed 溶解 each set of cells independently, and pooled the lysates 裂解物. We then immunoprecipitated `synPRE-P—synPOST-P` complexes from the mixed lysate by streptavidin 链霉亲和素 IP, released the complexes from the beads by cleaving 劈开 the disulfide bridge 二硫键 on the crosslinker under mild reducing conditions and finally joined barcode mRNAs using emulsion RT-PCR. Sequencing the resulting barcode pairs revealed **42** presynaptic and **42** postsynaptic barcodes, which were joined into 45 unique barcode pairs.
    - Based on the experimental setup, barcode pairs should show matching zip codes (i.e. A-A pairs or B-B pairs), as those are the only biologically possible combinations. **Any mixed barcode pairs (A–B or B–A) must arise from 'crossover' events and therefore represent the rate of false-positives in recovery of the correct set of synaptic connections by SYNseq.** In our HEK cell experiment, we find a significant crossover rate of **13.3%** (barcodes from one experiment joined to barcodes of another experiment). Extrapolated to include undetectable A–A and B–B crossover events, this indicates an overall **false-positive rate of 26.6%**. This false-positive rate, importantly, only measures false-positives arising from biochemical procedures post-lysis (i.e. protein–RNA dissociation, insufficient dilution for emulsions, etc.). It cannot quantify the false-positive barcode pairs that result from aberrant localization of the proteins or any other in vivo effects. The false-positive rate of this experiment appears to be dominated by the emulsion input concentration, **suggesting that we could reduce the false positive rate by further dilution of the complexes before emulsion.**

- We next tested emulsion RT-PCR for barcode joining in samples from **neuronal cultures**. 
    - We infected XONA devices with barcoded `synPRE-P` and `synPOST-P` Sindbis in the left and right chamber, respectively. Again, we set up two replicate experiments in parallel using experiment specific zip codes to differentiate the barcode mRNAs. **We crosslinked, lysed and mixed the lysates from the two sets of XONA devices** and performed a double immunoprecipitation to isolate synaptic `synPRE-P—synPOST-P` complexes. We then performed emulsion RT-PCR on **a very dilute sample of the IP products to minimize the rate of crossover events**. Sequencing the resulting barcode pairs, **we identified only 2 unique combinations of pre- and postsynaptic barcodes, albeit 尽管 no false positive cross-experiment barcode pairs**.
    - # !!!!!!!!!!!!!?????????????
    - While it is likely possible to increase this number of joined barcode pairs by increasing the number of droplets made, or by slightly increasing the concentration of emulsion input, we found ourselves in a regime far from the optimal necessary to achieve high throughput connectivity mapping by SYNseq. Taken together, our emulsion results suggest, that **while SYNseq can be used to read out synaptic connectivity, barcode joining is currently a very low efficiency process, which will need to be optimized further before SYNseq can be used for circuit mapping.**

### DISCUSSION

#### DNA sequencing for neuroanatomy

SYNseq takes inspiration from GRASP/mGRASP, chromosome confirmation capture and synaptic brainbow. 

#### Challenges ahead

- We concluded by a process of elimination that **it is barcode joining** that is limiting our ability to detect synaptic connections by SYNseq. 
- Barcoding of neurons and HEK cells is a high efficiency process. 
- We further demonstrated that barcode RNA and SYNseq proteins interact strongly and specifically, and that we can produce a significant number of trans-synaptic `synPRE-P—synPOST-P` complexes. 
- Despite this, we are unable to generate a comparable number of joined barcode pairs, which we therefore blame on inefficiencies of the droplet based joining strategy.
- We have not attempted to directly de-convolve the inefficiencies of reverse transcription vs. overlap PCR, but preliminary evidence place our in-droplet RT efficiency on the order of 1%. Such low RT efficiency will have a dramatic impact on our ability to produce joint barcode pairs, as both pre and postsynaptic barcode mRNAs need to be successfully reverse transcribed in each successfully loaded droplet (this will happen in only 0.01^2 of all properly loaded droplets). Given these considerations, we predict reverse transcription, not overlap PCR, which has a chance to join the two barcodes at every cycle of PCR, to be limiting the reaction. Although we were unable to achieve efficient and specific joining of barcodes in droplets, it is possible that with further optimization a droplet-based strategy, perhaps in combination with barcoded beads, might succeed. 
- Alternatively, joining strategies based on RNA ligation, gap filling or immobilization of complexes on beads, chips or in gels might emerge as more efficient strategies. 
- Finally, sequencing assays relying on the joining of barcodes (albeit in DNA form) are being developed for other applications, suggesting that in the future new technologies for barcode joining may emerge. Thus, although our present inability to achieve efficient and specific barcode joining limits the practical application of this approach, we expect the approach we have presented will form that foundation for an efficient method for deducing synaptic connections.

#### Space and neuroanatomy

#### Future directions

We envision that SYNseq will serve as a platform for future development toward encoding neural connectivity, and/or other biological variables—including cellular activity and/or identity—into a form that can be read by high-throughput sequencing, a technology which already operates at the scale of the complexity of neural circuits. 

Improvements to this method that allow for the co-expression of all of the components within the same cells—for example, by employing two separate RNA binding domains —will allow for bi-directional and local-circuit mapping. 

Transgenic techniques, combined with an in vivo barcoding scheme based on recombinases or CRISPR cas9 will allow for scaling this technology to mapping full brains.
