
## **Sequencing** the connectome

<div class="ctr">
    <img src="/NeuroNotes/img/p11.png" width="500"/>
</div>

<details>
<summary>

### Neuron-neuron synapse (connectome)

- `2012 BOINC`: barcoding of individual neuronal connections
- `2017 SYNSeq`

</summary>

- `BOINC` [**Sequencing** the connectome.](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3479097/)
    - Zador AM, Dubnau J, Oyibo HK, Zhan H, Cao G, Peikon ID.
    - PLoS Biol. 
    - 2012

- `SYNseq` [Using high-throughput **barcode** **sequencing** to efficiently map connectomes.](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5499584/)
    - Peikon ID, Kebschull JM, Vagin VV, Ravens DI, Sun YC, Brouzes E, Corrêa IR Jr, Bressan D, Zador AM.
    - Nucleic Acids Res. 
    - 2017 Jul 7

- `SYNSeq` [Network cloning using DNA **barcodes**.](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6511037/)
    - Shuvaev SA, Başerdem B, Zador AM, Koulakov AA.
    - Proc Natl Acad Sci U S A. 
    - 2019 May 7

</details>


<details>
<summary>

### Single neuron projection (projectome)

- `2016 MAPseq`: Multiplexed Analysis of Projections by Sequencing
    - In MAPseq, neurons are barcoded using a **Sindbis virus** library. Both the source area containing neuronal somata and target projection areas are micro-dissected into "cubelets" and sequenced. Barcodes from the target areas are then matched to those at the source area to reveal projection patterns. The **spatial resolution** of MAPseq is thus determined by the size of the cubelets.
- `2018 BaristaSeq`: Barcode **in situ** targeted sequencing
    - an improved version of the gap padlock probe-based method with a five-fold increase in efficiency
        - To capture short diverse barcode sequences, we needed an approach in which the actual target barcode sequence is captured and amplified. Although some in situ hybridization methods use sequencing to read out gene-specific tags to allow multiplexed detection of RNAs, they **cannot directly sequence the RNAs of interest** and are unsuitable for barcode sequencing. Circligase-based FISSEQ can readout mRNA sequences, but is not sufficiently sensitive for barcode sequencing. We therefore used a targeted approach, BaristaSeq, in which reverse transcription was used to **convert the barcode sequence into cDNA**, after which padlock probe hybridization followed by gap-filling and ligation was used to form a circular template for rolling circle amplification. The gap-filling padlock approach allowed for **efficient amplification of barcodes** in neurons co-expressing barcodes and GFP. We also adapted Illumina Sequencing By Synthesis (SBS) chemistry for in situ reactions. In combination, these strategies formed the basis for a protocol that allowed efficient and robust sequencing of barcoded **cultured neurons**.
    - `MAPseq` and others: the locations of the neurons under investigation had to be determined by manually picking individual neurons—a method which scales poorly. 
    - Efficient barcode sequencing **in situ** would allow us to preserve the location of each neuron's soma while still maintaining high-throughput lineage tracing and projection mapping. 
    - Furthermore, in the case of `MAPseq` where the barcodes fill the neurons, in situ barcode sequencing would potentially allow visualization of the morphology of individual neurons. 
    - Preserving the locations of the cells being sequenced would allow correlation of lineages and projections with other information, such as gene expression assayed through FISH and neuronal activities assayed through functional imaging, at cellular resolution.
- `2019 BARseq = MAPseq + BaristaSeq`: Barcoded Anatomy Resolved by Sequencing
    - a method that combines `MAPseq` with **in situ** sequencing of cellular barcodes (`BaristaSeq`).
    - `MAPseq` protocol relies on tissue homogenization, so the precise location of each soma is lost.
    - In BARseq, we perform in situ sequencing of barcoded somata at the **source**; the target projection areas are still micro-dissected and sequenced as cubelets. BARseq thus inherits the throughput and cubelet resolution of projections of `MAPseq`, but allows the precise somatic **origin** of each axonal projection to be determined with **cellular resolution**.

<div class="ctr">
    <h3>BARseq = MAPseq + BaristaSeq</h3>
    <img src="/NeuroNotes/img/p10.png" width="500"/>
</div>

- `2020 BRICseq = MAPseq + multi source`: BRain-wide Individual-animal Connectome sequencing
    - `MAPseq` was originally developed to study projections from a **single source**. Conceptually, a straightforward generalization of MAPseq to determine the projections from **many source areas in the same experiment** would be to tag neurons with an additional area-specific barcode sequence—a "zipcode"—which could be used to identify the source (somatic origin) of each projection. 
    - We pursued a more convenient strategy, which requires only a single batch of virus. We hypothesized that we could reliably determine the source of each projection using only sequencing, by exploiting the higher abundance of RNA barcodes in the soma-proximal compartments (including soma and proximal dendrites) compared with the axon terminals. According to this 'soma-max' strategy, the cubelet with the highest abundance of a given barcode of interest is assumed to be the source of the projection. Compared to the ground truth determined by the zipcode, the soma-max strategy correctly identified the soma location for 99.2±0.2% of all cells. These results indicate that the soma-max strategy would allow accurate reconstruction of connectivity even when only a **single viral library** is injected.

<div class="ctr">
    <h3>BRICseq = MAPseq + multi source</h3>
    <img src="/NeuroNotes/img/p9.png" width="100%"/>
</div>

- `2021 BARseq2 = BARseq + Spatial transcriptomics`: Barcoded Anatomy Resolved by Sequencing 2
    - In `BARseq`, each neuron is labeled with a unique virally-encoded RNA barcode that is replicated in the somas and transported to the axon terminals. 
    - The barcodes at the axon terminals located at various target areas are sequenced and matched to somatic barcodes, which are sequenced in situ, in order to determine the projection patterns of each labeled neuron. 
    - Because `BARseq` preserves the location of somata with high spatial resolution, in principle it provides a platform to combine projection mapping with other neuronal properties also interrogated in situ, including gene expression. We have previously shown that `BARseq` can be combined with fluorescent in situ hybridization (FISH) and Cre-labeling to uncover **projections across neuronal subtypes defined by gene expression**. However, these approaches **can only interrogate one or a few genes at a time**, which would be insufficient for unraveling the complex relationship between the expression of many genes to diverse cortical projections.
    - Here we aim to develop a technique to simultaneously map projections to multiple brain areas and **detect the expression of dozens of genes** in hundreds to thousands of neurons from a cortical area with high throughput, high spatial resolution, and cellular resolution. 
    - To achieve this goal, we combine the high throughput and multiplexed projection mapping capability of `BARseq` with state-of-the-art **spatial transcriptomic techniques with high imaging throughput and multiplexing capacity**. This second-generation `BARseq` (BARseq2) greatly improves the ability to correlate the expression of many genes to projections to many targets in the same neurons. 
    - As a proof-of-principle, we first demonstrate multiplexed gene detection using BARseq2 by mapping the spatial pattern of up to 65 cadherins and cell-type markers in 29,933 cells. We then correlate the expression of 20 cadherins to projections to up to 35 target areas in 1,349 neurons in mouse motor and auditory cortex. Our study reveals novel sets of cadherins that correlate with homologous projections in both cortical areas. BARseq2 thus bridges transcriptomic signatures obtained through spatial transcriptional profiling with sequencing-based projection mapping to illuminate the molecular logic of long-range projections.

<div class="ctr">
    <h3>BARseq2 = BARseq + Spatial transcriptomics</h3>
    <img src="/NeuroNotes/img/p12.png" width="100%"/>
</div>

</summary>

- `MAPseq` [High-Throughput Mapping of Single-Neuron Projections by **Sequencing** of **barcoded** RNA.](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6640135/)
    - Kebschull JM, Garcia da Silva P, Reid AP, Peikon ID, Albeanu DF, Zador AM.
    - Neuron. 
    - 2016 Sep 7

- `BaristaSeq` [Efficient in situ **barcode** **sequencing** using padlock probe-based **BaristaSeq**.](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5829746/)
    - Chen X, Sun YC, Church GM, Lee JH, Zador AM.
    - Nucleic Acids Res. 
    - 2018 Feb 28

- `MAPseq` [The logic of single-cell projections from visual cortex.](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6585423/)
    - Han Y, Kebschull JM, Campbell RAA, Cowan D, Imhof F, Zador AM, Mrsic-Flogel TD.
    - Nature. 
    - 2018 Apr 5 

- `MAPseq BaristaSeq` [Cellular **barcoding**: lineage tracing, screening and beyond.](http://zadorlab.labsites.cshl.edu/wp-content/uploads/sites/59/2019/08/Kebschull-Zador-2018-Cellular-barcoding-lineage-tracing.pdf)
    - Kebschull JM, Zador AM.
    - Nat Methods. 
    - 2018 Nov

- `BARseq` [High-Throughput Mapping of Long-Range Neuronal Projection Using In Situ **Sequencing**.](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7836778/)
    - Chen X, Sun YC, Zhan H, Kebschull JM, Fischer S, Matho K, Huang ZJ, Gillis J, Zador AM.
    - Cell. 
    - 2019 Oct 17

- `BRICseq` [**BRICseq** Bridges Brain-wide Interregional Connectivity to Neural Activity and Gene Expression in Single Animals.](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7771207/)
    - Huang L, Kebschull JM, Fürth D, Musall S, Kaufman MT, Churchland AK, Zador AM.
    - Cell. 
    - 2020 Jul 9

- `BARseq` [**BARcode** DEmixing through Non-negative Spatial Regression (BarDensr).](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7971881/)
    - Chen S, Loper J, Chen X, Vaughan A, Zador AM, Paninski L.
    - PLoS Comput Biol. 
    - 2021 Mar 8

- `BARseq2` [Integrating **barcoded** neuroanatomy with spatial transcriptional profiling enables identification of gene correlates of projections.](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8178227/)
    - Sun YC, Chen X, Fischer S, Lu S, Zhan H, Gillis J, Zador AM.
    - Nat Neurosci. 
    - 2021 Jun

- `BARseq` [Cellular anatomy of the mouse primary motor cortex.](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8494646/)
    - Muñoz-Castañeda R, Zingg B, Matho KS, Chen X, Wang Q, Foster NN, Li A, Narasimhan A, Hirokawa KE, Huo B, Bannerjee S, Korobkova L, Park CS, Park YG, Bienkowski MS, Chon U, Wheeler DW, Li X, Wang Y, Naeemi M, Xie P, Liu L, Kelly K, An X, Attili SM, Bowman I, Bludova A, Cetin A, Ding L, Drewes R, D'Orazi F, Elowsky C, Fischer S, Galbavy W, Gao L, Gillis J, Groblewski PA, Gou L, Hahn JD, Hatfield JT, Hintiryan H, Huang JJ, Kondo H, Kuang X, Lesnar P, Li X, Li Y, Lin M, Lo D, Mizrachi J, Mok S, Nicovich PR, Palaniswamy R, Palmer J, Qi X, Shen E, Sun YC, Tao HW, Wakemen W, Wang Y, Yao S, Yuan J, Zhan H, Zhu M, Ng L, Zhang LI, Lim BK, Hawrylycz M, Gong H, Gee JC, Kim Y, Chung K, Yang XW, Peng H, Luo Q, Mitra PP, Zador AM, Zeng H, Ascoli GA, Josh Huang Z, Osten P, Harris JA, Dong HW.
    - Nature. 
    - 2021 Oct

</details>


<details>
<summary>

### Toolbox

</summary>

- [In vivo generation of DNA sequence diversity for cellular **barcoding**.](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4176322/)
    - Peikon ID, Gizatullina DI, Zador AM.
    - Nucleic Acids Res. 
    - 2014

- [Long-term Cre-mediated retrograde **tagging** of neurons using a novel recombinant pseudorabies virus.](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4153299/)
    - Oyibo HK, Znamenskiy P, Oviedo HV, Enquist LW, Zador AM.
    - Front Neuroanat. 
    - 2014 Sep 3

- [Sources of PCR-induced distortions in high-throughput **sequencing** data sets.](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4666380/)
    - Kebschull JM, Zador AM.
    - Nucleic Acids Res. 
    - 2015 Dec 2

- [A New Defective Helper RNA to Produce Recombinant Sindbis Virus that Infects Neurons but does not Propagate.](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4877524/)
    - Kebschull JM, Garcia da Silva P, Zador AM.
    - Front Neuroanat. 
    - 2016 May 24

</details>




<details><summary>other papers from Prof. Tony Zador</summary>

## learning

- Corticostriatal Plasticity Established by Initial Learning Persists after Behavioral Reversal.
    - Ghosh S, Zador AM.
    - eNeuro. 
    - 2021 Mar 11
- SYNPLA, a method to identify synapses displaying plasticity after learning.
    - Dore K, Pao Y, Soria Lopez J, Aronson S, Zhan H, Ghosh S, Merrill S, Zador AM, Malinow R, Kebschull JM.
    - Proc Natl Acad Sci U S A. 
    - 2020 Feb 11
- A critique of pure learning and what artificial neural networks can learn from animal brains.
    - Zador AM.
    - Nat Commun. 
    - 2019 Aug 21

## **auditory**

- Selective corticostriatal plasticity during acquisition of an **auditory** discrimination task.
    - Xiong Q, Znamenskiy P, Zador AM.
    - Nature. 
    - 2015 May 21

- **auditory** thalamus and **auditory** cortex are equally modulated by context during flexible categorization of **sounds**.
    - Jaramillo S, Borges K, Zador AM.
    - J Neurosci. 
    - 2014 Apr 9

- Corticostriatal neurons in **auditory** cortex drive **decision**s during **auditory** discrimination.
    - Znamenskiy P, Zador AM.
    - Nature. 
    - 2013 May 23

- Up states are rare in awake **auditory** cortex.
    - Hromádka T, Zador AM, DeWeese MR.
    - J Neurophysiol. 
    - 2013 Apr

- PTEN regulation of local and long-range connections in mouse **auditory** cortex.
    - Xiong Q, Oviedo HV, Trotman LC, Zador AM.
    J Neurosci. 
    - 2012 Feb 1

- The **auditory** cortex mediates the perceptual effects of acoustic temporal expectation.
    - Jaramillo S, Zador AM.
    - Nat Neurosci. 
    - 2011 Feb

- The functional asymmetry of **auditory** cortex is reflected in the organization of local cortical circuits.
    - Oviedo HV, Bureau I, Svoboda K, Zador AM.
    - Nat Neurosci. 
    - 2010 Nov

- Long-lasting context dependence constrains neural encoding models in rodent **auditory** cortex.
    - Asari H, Zador AM.
    - J Neurophysiol. 
    - 2009 Nov

- Representations in **auditory** cortex.
    - Hromádka T, Zador AM.
    - Curr Opin Neurobiol.
    - 2009 Aug

- Engaging in an **auditory** task suppresses responses in **auditory** cortex.
    - Otazu GH, Tai LH, Yang Y, Zador AM.
    - Nat Neurosci. 
    - 2009 May

- Millisecond-scale differences in neural activity in **auditory** cortex can drive **decision**s.
    - Yang Y, DeWeese MR, Otazu GH, Zador AM.
    - Nat Neurosci. 
    - 2008 Nov

- Sparse representation of **sounds** in the unanesthetized **auditory** cortex.
    - Hromádka T, Deweese MR, Zador AM.
    - PLoS Biol. 
    - 2008 Jan

- Toward the mechanisms of **auditory** attention.
    - Hromádka T, Zador AM.
    - Hear Res. 
    - 2007 Jul

- Non-Gaussian membrane potential dynamics imply sparse, synchronous activity in **auditory** cortex.
    - DeWeese MR, Zador AM.
    - J Neurosci. 
    - 2006 Nov 22

- Reliability and representational bandwidth in the **auditory** cortex.
    - DeWeese MR, Hromádka T, Zador AM.
    - Neuron. 
    - 2005 Nov 3

- Neural gallops across **auditory** streams.
    - Deweese MR, Zador AM.
    - Neuron. 
    - 2005 Oct 6

- Synaptic mechanisms of forward suppression in rat **auditory** cortex.
    - Wehr M, Zador AM.
    - Neuron. 
    - 2005

- Shared and private variability in the **auditory** cortex.
    - Deweese MR, Zador AM.
    - J Neurophysiol. 
    - 2004 Sep 

- Linearity of cortical receptive fields measured with natural **sounds**.
    - Machens CK, Wehr MS, Zador AM.
    - J Neurosci. 
    - 2004 Feb 4

- Balanced inhibition underlies tuning and sharpens spike timing in **auditory** cortex.
    - Wehr M, Zador AM.
    - Nature. 
    - 2003 Nov 27

- Binary spiking in **auditory** cortex.
    - DeWeese MR, Wehr M, Zador AM.
    - J Neurosci. 
    - 2003 Aug 27

## **decision**

- Standardized and reproducible measurement of **decision**-making in mice.
    - International Brain Laboratory, Aguillon-Rodriguez V, Angelaki D, Bayer H, Bonacchi N, Carandini M, Cazettes F, Chapuis G, Churchland AK, Dan Y, Dewitt E, Faulkner M, Forrest H, Haetzel L, Häusser M, Hofer SB, Hu F, Khanal A, Krasniak C, Laranjeira I, Mainen ZF, Meijer G, Miska NJ, Mrsic-Flogel TD, Murakami M, Noel JP, Pan-Vazquez A, Rossant C, Sanders J, Socha K, Terry R, Urai AE, Vergara H, Wells M, Wilson CJ, Witten IB, Wool LE, Zador AM.
    - Elife. 
    - 2021 May 20

- Mice and rats achieve similar levels of performance in an adaptive **decision**-making task.
    - Jaramillo S, Zador AM.
    - Front Syst Neurosci. 
    - 2014 Sep 18

## **computation**

- Synaptic connectivity and **computation**.
    - Zador AM.
    - Nat Neurosci. 
    - 2001 Dec

- The basic unit of **computation**.
    - Zador AM.
    - Nat Neurosci. 
    - 2000 Nov

- Dynamic stochastic synapses as **computation**al units.
    - Maass W, Zador AM.
    - Neural Comput. 
    - 1999 May 15

## others

- Identification of a brainstem locus that inhibits tumor necrosis factor.
    - Kressel AM, Tsaava T, Levine YA, Chang EH, Addorisio ME, Chang Q, Burbach BJ, Carnevale D, Lembo G, Zador AM, Andersson U, Pavlov VA, Chavan SS, Tracey KJ.
    - Proc Natl Acad Sci U S A. 
    - 2020 Nov 24

- Differences in sensitivity to neural timing among cortical areas.
    - Yang Y, Zador AM.
    - J Neurosci. 
    - 2012 Oct 24

- PINP: a new method of **tagging** neuronal populations for identification during in vivo electrophysiological recording.
    - Lima SQ, Hromádka T, Znamenskiy P, Zador AM.
    - PLoS One. 
    - 2009 Jul 7

- Correlated connectivity and the distribution of firing rates in the neocortex.
    - Koulakov AA, Hromádka T, Zador AM.
    - J Neurosci. 
    - 2009 Mar 25

- Sparse representations for the cocktail party problem.
    - Asari H, Pearlmutter BA, Zador AM.
    - J Neurosci. 
    - 2006 Jul 12

- Natural scene statistics at the centre of gaze.
    - Reinagel P, Zador AM.
    - Network. 
    - 1999 Nov

- Input synchrony and the irregular firing of cortical neurons.
    - Stevens CF, Zador AM.
    - Nat Neurosci. 
    - 1998 Jul

- Efficient discrimination of temporal patterns by motion-sensitive neurons in primate visual cortex.
    - Buracas GT, Zador AM, DeWeese MR, Albright TD.
    - Neuron. 
    - 1998 May

- Dynamic synapses in the cortex.
    - Zador AM, Dobrunz LE.
    - Neuron. 
    - 1997 Jul

- Electrotonic architecture of hippocampal CA1 pyramidal neurons based on three-dimensional reconstructions.
    - Mainen ZF, Carnevale NT, Zador AM, Claiborne BJ, Brown TH.
    - J Neurophysiol. 
    - 1996 Sep

- The morphoelectrotonic transform: a graphical approach to dendritic function.
    - Zador AM, Agmon-Snir H, Segev I.
    - J Neurosci. 
    - 1995 Mar

</details>
