
- [Paper](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4176322/)

### INTRODUCTION

- Most **current** approaches for tagging individual cells with a genetic barcode rely on the creation of diverse libraries **in vitro** and subsequent delivery of genetic material into a host cell at low-copy number. Such in vitro approaches are limited by cloning bottlenecks that cause reduced library diversities and sequence biases, by incomplete labelling of all cells within a population, by the possibility of introducing multiple barcodes per cell, and by the challenges of working across organisms (e.g. retroviral barcoding cannot be applied in some organisms like Caenorhabditis elegans).

- **In vivo** barcoding has the potential to overcome all of these limitations. Mechanisms for generating diversity in vivo exist, endogenously, in many organisms—most notably the mammalian immune system. However, efforts to repurpose the immune system's V(D)J recombination for in vivo cellular barcoding yielded limited barcode diversity—on the order of a dozen unique sequences—in cells other than lymphocytes. `Exogenous recombinases` have been successfully applied to generate diverse combinations of colours for cellular tagging purposes. This technique, better known as `Brainbow`, relies on `Cre recombinase` to rearrange a cassette resulting in the stochastic expression of a subset of different coloured fluorescent proteins (XFPs) in neurons. The theoretical diversity of Brainbow is in the hundreds, but cannot be easily assayed with DNA sequencing because it relies heavily on gene copy number variation as well as recombination. We reasoned that by replacing XFPs with unique sequences, we could design a barcoding system with the potential to achieve diversities that matched the scale of high-throughput sequencing technologies.

- We have developed a novel method of generating sequence diversity in vivo for the purpose of cellular barcoding. Our method, which relies on a DNA invertase (转化酶)—`Rci`, recombinase for clustered inversion—to shuffle fragments of DNA, has the potential to easily achieve diversities over 1e9 unique sequences. Here, we show that this method can be applied for the in vivo generation of diversity in E. coli.

### MATERIALS AND METHODS

<div class="ctr"><iframe width="560" height="315" src="https://www.youtube.com/embed/zOStRhccn6M" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></div>

<details><summary>

In silico simulations

- We defined `Cre` recombination as two independent binding events to `loxP` sites.
- We defined `Rci` recombination as two independent binding events to `sfx` sites.
- `Cre` (bad): excision + inversion => less diversity
- `Rci` (good): inversion only => more diversity

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

> what are `sfx sites` ?

A 5-fragment barcode cassette was synthesized as a minigene by Integrated DNA Technologies and inserted into a standard plasmid (IDP190). Several different sfx sites were used to avoid perfect inverted repeats to simplify DNA synthesis. The cassette was constructed as 

`ANCHOR105-sfx101R-BC1-sfx102L-BC2-sfx106R-BC3-sfx112L-BC4-sfx109R-BC5-sfx101L-ANCHOR56` 

where R indicates the sfx sequence in 5′-3′ orientation and L indicates the reverse orientation (where orientation is determined by the core sequence: 5′-GTGCCAA-3′). The barcode cassette was synthesized with flanking sequences for use in polymerase (聚合酶) chain reaction (PCR) amplification and sequencing (#3:ANCHOR105 and #4:ANCHOR56). In addition, the cassette was flanked by restriction sites (PciI) and flanking primer sequences (#1:BC_F and #2:BC_R) for subsequent PCR and cloning. An additional BC cassette (containing BC6-11) was synthesized by GeneWiz (BCextension). The cassette was constructed as 

`BamHI-BC6-sfx101R-BC7-sfx102L-BC8-sfx106R-BC9-sfx112L-BC10-sfx109R-BC5-sfx101L-NheI`

<details><summary>sequences</summary>

- Primer Table

| name       | sequence                      |
| -          | -                             |
| BC_F (5BC) | gctttacctcgcactgcccagagtg     |
| BC_R (5BC) | agactcatgcatcgtgccactgtgttcg  |
| ANCHOR56   | ttgcgaacctcatcactcgttgc       |
| ANCHOR105  | tgaggcaaggaagatgctgtcc        |
| NdeI-Rci_F | tctacatatgccgtctccacgcatccgt  |
| NotI-Rci_R | actggcggccgcttacagcggtgtgctgc |
| s-pKat_promoter   | acctagatctcattattgcaattaataaacaactaacggacaattctacctaacaaggaggtaccatatgacct               |
| as-pKat_promoter | aggtcatatggtacctccttgttaggtagaattgtccgttagttgtttattaattgcaataatgagatctaggt               |
| BamHI-BC5_F | tctaggatccggcaatactttcgtgccaatccgg |
| NheI-BC5_R  | actggctagcgcaacgagtgatgaggttcgcaa  |

- sfx sites used

| name   | sequence                        |
| -      | -                               |
| sfx101 | ggcaatactttcgtgccaatccggtacgtgg |
| sfx102 | ctgctggcctacgtgccaatccggtacgtgg |
| sfx106 | gcacgtaggccagtgccaatccggtacctgg |
| sfx109 | ttctctgcaagcgtgccaatccggtacgtgg |
| sfx112 | gccaagcttgttgtgccaatccggtacgtgg |

- BC sequences

| name   | sequence                        |
| -      | -                               |
| BC1 |	ccaattggtagtttgtccagaactcagattttaacagcagaggacgcatgctctaccttcatgatccactgacgtccctgaggctgcaatacatgcaacg |
| BC2 |	aggcagtctccgcggtaagtcctagtgcaatggcgcttttttaccctcgtcctcgagaagaggggacgccagtgcagatatctttaatgtggtaattggg |
| BC3 |	aggactcttggccctccgcccttaggcagtgcatactcttccataaacgggctgttagttatggcgtccgaggattcaaaaaggtgagcgaactcggccg |
| BC4 |	atccggagagacgggcttcaaagctgcctgacgacggttgcgcgtccgtatcaaaatcctcctaataagcccccgtcactgttggttgaagagcccagga |
| BC5 | 	cgggttggccagatgtgcgattatatcgcttaatggctcttgggccgcggtgcgttaccttgcaggaattgaggccgtccgttaatttcccttgcataca |
| BC6 |	ggatccgtcaaatgtgattgatgccctcgatccccgtggagatgagatgcctggctggtcggggtgcaaaccgatcaataacaatcgtcactttcgaggt |
| BC7 |	ccccgcactgatgcctaaacctcgcaggtctttaggatattgacgcttgacgatgtcccacgattaaaccggtgtgcaaccttggatgctgattaatcgc |
| BC8 |	gcgagatgaatggacgggtctggttcgaacgatgtattaattgatgcaggagccccgcacacctaaatatcgatccgggtatgtttaatggtgcgatggc |
| BC9 |	ggctgccctctcctacttacgggtatcggctcccagccccacgtcgcgctctgttctcaaccaactaggatctgatgcacgagattaacgttgacgttgt |
| BC10 |	tacaccggcccgagcgtcgtcctttctatagatggcttccagcgactcaccaggagtgttctggttgggaactacttcgaacgctatgagccttccctat |
| BC11 |	tgctgaaacagttaatactgggacttattcttgggactgatagggttatgacgcttcttatgttctc |

- Plasmid table

| name   | cassette               |
| -      | -                      |
| IDP190 | 5BC Cassette           |
| IDP205 | T7→Rci; 5BC Cassette   |
| DIG35  | pKAT→Rci; 5BC Cassette |
| BCext  | BC6-BC11 extension     |
| DIG70  | T7→Rci; 11BC Cassette  |
| DIG71  | T7→Rci; 11BC Cassette  |

</details>

<details><summary>Plasmid construction</summary>

- The 5-fragment barcode cassette (from plasmid #IDP190) was amplified using primers (引物) #1:BC_F and #2:BC_R, digested with PciI, and cloned into pet22b. A strain of E. coli harbouring the pEK204 plasmid, which encodes Rci recombinase (NCBI Reference Sequence: NC_013120.1), was ordered from NCTC (NCTC 13452: J53-derived E. coli. GenBank accession number EU935740). The open reading frame of Rci was obtained by PCR of the pEK204 plasmid with primers #7:NdeI-Rci_F and #8:NotI-Rci_R, which add restriction sites NdeI and NotI, respectively. Rci was cloned into plasmid pet22b using restriction sites NdeI and NotI (thus removing the periplasmic localization signal of pet22b) to create Plasmid #IDP205:(T7→Rci; 5BC). 

- The constitutively active promoter, pKat (Registry of Standard Biological Parts: BBa_I14034, http://parts.igem.org/Part:BBa_I14034), and a ribosomal binding site (RBS): AGGAGG, flanked by restriction sites BglII and NdeI were synthesized as complementary oligos #9:s-pKat_promoter and #10:as-pKat_promoter, annealed, digested and subsequently cloned into #IDP205 to make plasmid #DIG35:(pKat→Rci, 5BC). 

- To extend the BC cassette we amplified #IDP205 using primers #11:BamHI-BC5_F and #12: NheI-BC5_R and cut with BamHI and NheI. The insert, BC6-BC11, was digested from BCextension with BamHI and NheI. The backbone and insert were ligated to make plasmid #DIG70:(T7→Rci, 5BC). 

- The constitutively active promoter, pKat, and an RBS flanked by restriction sites BglII and NdeI were synthesized as complementary oligos #9:s-pKat_promoter and #10:as-pKat_promoter, annealed, digested and subsequently cloned into #DIG70 to make plasmid #DIG71:(pKat→Rci, 11BC).

All cloning was performed using Top10 chemically competent cells (Invitrogen) with growth at 37°C.

</details>

<details><summary>Bacterial culture & shuffling</summary>

- For initial tests with T7 induced expression of Rci, plasmids IDP205 or DIG35 were transformed into E coli strain BL21(DE3) (NEB) and grown in 5 ml of normal or OvernightExpress (Millipore) supplemented media overnight. 
    - Plasmid DNA was isolated and the Rci coding sequence was removed (to prevent further shuffling) by double digestion (NdeI–NotI), blunting (Mung Bean) and re-ligation (Roche Rapid Ligation kit). 
    - The transformed ligation was plated for clonal analysis. Clonal analysis involved the selection of single colonies, growth in LB for 16 h, plasmid isolation and Sanger sequencing with ANCHOR105 used as a primer. 

- For tests of the pKat driven expression, plasmids IDP205 or DIG35 were transformed into E. coli strain Top10 cells (Invitrogen) and grown in 5 ml of LB overnight. 
    - Plasmid DNA was isolated and the Rci coding sequence was removed (to prevent further shuffling) by double digestion (NdeI–NotI), blunting (Mung Bean) and re-ligation (Roche Rapid Ligation kit). 
    - The transformed ligation was plated for clonal analysis. Clonal analysis involved the selection of single colonies, growth in LB for 16 h, plasmid isolation and Sanger sequencing with ANCHOR105 used as a primer. 

- For high-throughput sequencing by PacBio, plasmids IDP205, DIG35 and DIG71 were transformed into Top10 cells (Invitrogen) and grown overnight in 50 ml of LB. 
    - Plasmid DNA was isolated and digested with PciI to release the barcode cassette. The barcode cassette was prepared for PacBio sequencing using the PacBio SMRTbell Template Prep Kit according to the manufacturer's instructions and cassettes from each original plasmid were sequenced on a single Single Molecule Real Time (SMRT) sequencing cell. PacBio sequences were collapsed into circular consensus reads using the PacBio command line tools.

</details>

#### Barcode Reconstruction

Our sequence alignment algorithm is written in Matlab and uses the Matlab Bioinformatics Toolbox. Sequencing reads are processed independently. Each known barcode fragment is aligned to the sequence read (in both orientations) with a thresholded Smith–Waterman alignment and the position of the segment along the read is stored. The threshold is set by a bootstrap method. Briefly, one hundred randomly generated 100-mers are aligned to all of the sequence traces and a score is associated with each alignment. The mean score plus two standard deviations is considered the threshold for all subsequent alignments. The complete barcode can be reconstructed based on the positions of each segment. Because the algorithm relies only on local alignment, this method is extremely robust to sequencing errors.

