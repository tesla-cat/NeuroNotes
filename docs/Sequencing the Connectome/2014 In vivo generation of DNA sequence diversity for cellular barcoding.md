
- [Paper](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4176322/)

### INTRODUCTION

- Most **current** approaches for tagging individual cells with a genetic barcode rely on the creation of diverse libraries **in vitro** and subsequent delivery of genetic material into a host cell at low-copy number. Such in vitro approaches are limited by cloning bottlenecks that cause reduced library diversities and sequence biases, by incomplete labelling of all cells within a population, by the possibility of introducing multiple barcodes per cell, and by the challenges of working across organisms (e.g. retroviral barcoding cannot be applied in some organisms like Caenorhabditis elegans).

- **In vivo** barcoding has the potential to overcome all of these limitations. Mechanisms for generating diversity in vivo exist, endogenously, in many organisms—most notably the mammalian immune system. However, efforts to repurpose the immune system's V(D)J recombination for in vivo cellular barcoding yielded limited barcode diversity—on the order of a dozen unique sequences—in cells other than lymphocytes. `Exogenous recombinases` have been successfully applied to generate diverse combinations of colours for cellular tagging purposes. This technique, better known as `Brainbow`, relies on `Cre recombinase` to rearrange a cassette resulting in the stochastic expression of a subset of different coloured fluorescent proteins (XFPs) in neurons. The theoretical diversity of Brainbow is in the hundreds, but cannot be easily assayed with DNA sequencing because it relies heavily on gene copy number variation as well as recombination. We reasoned that by replacing XFPs with unique sequences, we could design a barcoding system with the potential to achieve diversities that matched the scale of high-throughput sequencing technologies.

- We have developed a novel method of generating sequence diversity in vivo for the purpose of cellular barcoding. Our method, which relies on a DNA invertase (转化酶)—`Rci`, recombinase for clustered inversion—to shuffle fragments of DNA, has the potential to easily achieve diversities over 1e9 unique sequences. Here, we show that this method can be applied for the in vivo generation of diversity in E. coli.

### MATERIALS AND METHODS

<div class="ctr"><iframe width="560" height="315" src="https://www.youtube.com/embed/zOStRhccn6M" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></div>

<details><summary>

In silico simulations

- `Cre` (bad): excision + inversion => less possibilities
- `Rci` (good): inversion only => more possibilities

</summary>

- We performed in silico simulations to determine the behaviour of different cassette architectures. 
    - For `Cre`-based cassettes, ncell cassettes (ncell = 10 000) of nfrag fragments (nfrag = 100) were operated on independently. Each fragment was flanked on its 5′ end with a loxP site in sense orientation (5′-GCATACAT-3′) and on it's 3′ end with a loxP site in the antisense orientation. Concatenation of fragments resulted in cassettes in which adjacent fragments (excluding ends) were separated by two loxP sites in opposing orientation. 
        - We defined Cre recombination as two independent binding events to loxP sites. Binding of Cre to a pair of loxP sites always resulted in recombination, where the result (inversion or excision) was defined by the relative orientation of the sites defined in a look up table (updated after each event). 
        - Completion is defined to be the point at which Cre can no longer mediate an excision event. The number of recombination events required to reach completion was tracked for each cassette. 
    - For `Rci`-based cassettes, ncell cassettes (ncell = 10 000) of nfrag fragments (nfrag = 10) were operated on independently. Here, we considered two architectures. 
        - For the first architecture, each fragment of the cassette was flanked on its 5′ end with an sfx site in sense orientation and on its 3′ end with an sfx site in the antisense orientation. Concatenation of fragments resulted in cassettes in which adjacent fragments (excluding ends) were separated by two sfx sites in opposing orientation. For the purpose of simulations, we consider each pair of sfx sites between fragments to be equivalent to a single bidirectional sfx site. 
            - We defined Rci recombination as two independent binding events to sfx sites. In this case, binding of Rci to a pair of sfx sites always resulted in recombination (inversion). Simulations were allowed to proceed for m recombination events per cassette. 
        - For the second Rci architecture, the 5′ end of the cassette begins with a single sfx site in sense orientation, followed by a single sequence fragment. The cassette is extended by addition of an sfx site and a sequence fragment, with the orientation of sfx sites alternating throughout the cassette. The cassette is terminated at its 3′ end by an sfx site in antisense orientation. 
            - We defined Rci recombination as two independent binding events to sfx sites. Binding of Rci to a pair of sfx sites only resulted in recombination if the sfx sites were in opposite orientations (inversion only). Simulations were allowed to proceed for m recombination events per cassette. 
- The code for running all simulations is provided in Supplementary Materials.

</details>

#### Synthesis of barcode cassettes

> what is `sfx sites` ?

A 5-fragment barcode cassette was synthesized as a minigene by Integrated DNA Technologies and inserted into a standard plasmid (IDP190). Several different sfx sites were used to avoid perfect inverted repeats to simplify DNA synthesis. The cassette was constructed as `ANCHOR105-sfx101R-BC1-sfx102L-BC2-sfx106R-BC3-sfx112L-BC4-sfx109R-BC5-sfx101L-ANCHOR56` where R indicates the sfx sequence in 5′-3′ orientation and L indicates the reverse orientation (where orientation is determined by the core sequence: 5′-GTGCCAA-3′). The barcode cassette was synthesized with flanking sequences for use in polymerase chain reaction (PCR) amplification and sequencing (#3:ANCHOR105 and #4:ANCHOR56). In addition, the cassette was flanked by restriction sites (PciI) and flanking primer sequences (#1:BC_F and #2:BC_R) for subsequent PCR and cloning. An additional BC cassette (containing BC6-11) was synthesized by GeneWiz (BCextension). The cassette was constructed as `BamHI-BC6-sfx101R-BC7-sfx102L-BC8-sfx106R-BC9-sfx112L-BC10-sfx109R-BC5-sfx101L-NheI`

