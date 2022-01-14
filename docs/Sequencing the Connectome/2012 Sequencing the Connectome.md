
- [Paper](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3479097/)
- BOINC: barcoding of individual neuronal connections

### prerequisites

- **excision (切除)**: The removal of a section of double-stranded DNA that is faulty due to mutation or incorrect replication
- **inversion (染色体倒位)**: chromosome rearrangement in which a segment of a chromosome is reversed end-to-end
- **环化重组酶 (cyclization recombinase，Cre)**: 可在无任何辅助因子的作用下与不同形式的loxP（locus X over P1）DNA序列直接结合并相互作用，从而可在特定靶点进行特定基因的敲入、敲除等，具有作用原理简单、空间特异性高、重组效率高等优点而被广泛应用。

### Why Is the Single Neuron Connectome Important?

<div class="ctr"><img src="/NeuroNotes/img/p1.png" width="300"/></div>

- `motion detection circuit` (top): 
    - sequential activation of input neurons from left to right (1, 4, 7, 10) will generate less activity in the output neuron (0) than activation from right to left (10, 7, 4, 1)
- `lateral inhibition circuit` (bottom): 
    - wired similarly, but the addition of a few extra inhibitory connections renders it insensitive to directional motion 

- C. elegans:
    - 302 neurons connected by about 7,000 synapses. 
    - Interestingly, the utility of the connectome in C. elegans is somewhat limited because function is highly multiplexed, with different neurons performing different roles depending on the state of neuromodulation, possibly as a mechanism for compensating for the small number of neurons

### Current Approaches to the Connectome

- physiology
    - Callaway and colleagues used `laser scanning photostimulation` to probe connectivity in visual cortex. They found that if two nearby neurons in layer 2/3 are connected, then they share input from single neurons in layer 4, but if they are not connected they do not share input. Thus, the input from layer 4 to layer 2/3 appears to consist of at least two independent "subnetworks", which happen to overlap in space. 
    - Chklovskii and colleagues used whole cell methods to assess connectivity among triplets of neurons. By enumerating all 16 possible ways that three neurons can be connected, they discovered that several connectivity motifs were overrepresented above the chance levels predicted by the pairwise connection probabilities. Thus connectivity among triplets of cortical neurons deviates markedly from the null hypothesis of random connectivity. 
- light microscopy
    - `GRASP` (GFP Reconstituted Across Synaptic Partners) allows synaptic contacts to be resolved at the level of light microscopy. 
    - `Brainbow` can be used to trace axons and dendrites over considerable distance. This technique relies on stochastic and combinatorial expression of several fluorophores (XFPs). Each neuron expresses a random collection of up to four different XFPs in different ratios, to achieve a theoretical palette of more than 100 different colors. The randomization is achieved by clever application of `Cre-lox recombination`, wherein the protein Cre recombinase catalyzes the inversion or excision of DNA between a pair of short (34 nucleotide) sequences termed lox sites. 
    - Finally, it is now possible to image an entire mouse brain using `two-photon microscopy` in hours or days. 
- electron microscopy (EM)
    - EM is required because light microscopy does not have sufficient resolution to establish whether two nearby neuronal processes are merely close or whether they have actually formed a synapse. 
    - Reconstruction of serial electron micrographs has yielded what to date is the only complete connectome, that of C. elegans. However, even for this simple nervous system, the reconstruction required a heroic effort -- over 50 person-years of labor to collect and analyze the images.

### DNA Sequencing as a Novel Method of Solving the Connectome

- BOINC: three components

<div class="ctr"><img src="/NeuroNotes/img/p4.png" width="300"/></div>

#### First, each neuron must be labeled with a unique sequence of nucleotides—a DNA "barcode". 

- The requisite barcoding is conceptually similar—though different in detail—to the generation of antibody diversity by B cells in the immune system through somatic recombination (体细胞重组). 
- The idea of barcoding individual neurons is inspired by `Brainbow`, except that here DNA sequences substitute for fluorophores (XFPs). The advantage of using sequences is diversity: whereas Brainbow allows for at most hundreds of color combinations, a barcode consisting of even 20 random nucleotides can uniquely label 4^20 neurons, far more than the number of neurons (<10^8) in a mouse brain.
- One strategy for generating sufficient diversity to barcode every neuron's DNA uniquely is shown below. In this strategy, inspired by Brainbow, each cell's genome contains a cassette consisting of a sequence of short unique barcode elements A…E… (top). Each barcode element is flanked by recombination sites (triangles). Upon expression of a suitable recombinase (重组酶), these barcode elements shuffle and invert (shown here by inverted letter). The theoretical diversity that can be generated by this is 2^N\*N!, where N is the number of barcode elements. For a cassette containing N=12 elements, the theoretical diversity is 2e12, far more than needed to barcode the 1e8 neurons in a mouse brain uniquely. Note that if a conventional recombinase like `cre` or `flp` is used here, `excision` will dominate over `inversion` and the resulting diversity scales with the number of barcode elements N. To avoid excision we use `RCI`, a recombinase that inverts but does **NOT** excise. (typo in paper)

<div class="ctr"><img src="/NeuroNotes/img/p2.png" width="400"/></div>

#### Second, barcodes from synaptically connected neurons must be associated. 

- One way to associate a pre- and postsynaptic barcode is by means of a `transsynaptic virus` such as `rabies (狂犬病)` or `pseudorabies (PRV) (伪狂犬病)`. These viruses have evolved exquisite mechanisms for moving genetic material across synapses and have been used extensively for tracing neural circuits in rodents. To share barcodes across synapses, the virus must be engineered to carry the barcode within its own genetic sequence. After transsynaptic spread of the virus each postsynaptic neuron can be thought of as a "bag of barcodes", consisting of copies of its own "host" barcodes, along with "invader" barcodes from presynaptically coupled neurons.

#### Finally, barcodes from synaptically connected neurons must be joined into single pieces of DNA for high-throughput sequencing. 

- Barcodes are joined in vivo (活体), so there is no need to isolate individual neurons prior to extracting DNA. Since only those pairs associated in vivo are actually joined, observing a host-invader barcode pair indicates that the host and the invader were synaptically coupled. 
- One strategy for joining barcodes is based on `phiC31` integrase (整合酶). PhiC31 mediates the integration of a `35-nucleotide AttB` site with a `35-nucleotide AttP` site to form an `AttL` and an `AttR` site. Because the AttL and AttR sites are not targets of phiC31, this reaction is irreversible (unlike comparable reactions with cre and flp). Once the barcodes are joined, they can be amplified by PCR (using primers complementary to the arrows) for sequencing.

<div class="ctr"><img src="/NeuroNotes/img/p3.png" width="300"/></div>

We are developing an approach based on `PRV amplicons`. Although there are many technical problems, including PRV toxicity and monosynaptic spread, which need to be addressed, this approach promises to offer a proof of principle for our proposal to convert connectivity into a sequencing problem.
