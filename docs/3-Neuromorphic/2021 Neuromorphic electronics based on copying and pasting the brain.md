
- [Paper](https://static1.squarespace.com/static/5994747fd2b8575a7b742b2a/t/614cca5296410712488c1cda/1632422482768/Copy+and+Paste+Brain+Nature+Electronics+2021.pdf)

## Contemporary neuromorphic approaches

<div class="ctr"><img src="/NeuroNotes/img/p20.png" width="600"/></div>

### analogue-aided ANN

- The backbone of this analogue-aided ANN is a crossbar array of conductive memories (resistive memories, for example) that performs multiply–accumulate operations—the most prevalent ANN algebra—in a physical manner. 
- Each memory stores an ANN optimization parameter (**weight**) as its **conductance** value. Input voltages fed to the rows of the array are multiplied by the weights via Ohm’s law, and the resulting currents are accumulated in each column by Kirchhoff’s law. 
- This physical, and thus analogue, multiply–accumulate operation burns far less power than its digital counterpart. 
- Here the colocalization of memory and computing in the crossbar array, which breaks away from the von Neumann paradigm, is inspired by the brain, where **memory elements (biological synapses)** are distributed across the network. 
- **The goal here, however, is to calculate the ANN algorithm, not to mimic the NNN to create the unique functions of the brain.**

## Copying the NNN

- The original neuromorphic pursuit to mimic the NNN has been
limited by the lack of the NNN’s functional wiring diagram. 
- As a result, the focus of the field has evolved from rigorous brain mimicry to design inspired by qualitative features of the brain such as 
    - asynchronous, 
    - event-driven operation and 
    - in-memory computing.
- Our aim is to turn back to the original idea of brain mimicry
by leveraging recent advances in neuroscience tools, in particular, a silicon neuro-electronic interface called the CMOS nanoelectrode array (CNEA). 
- The CNEA can ‘copy’ the NNN’s functional synaptic connectivity map (Fig. 2) through its massively parallel **intracellular** electrophysiological recording. 
- Over the past decades, non-electrophysiological methods, such as optical and electron microscopy, **genetically encoded indicators** and a host of other experimental methods, have also made spectacular progress in deciphering anatomical and functional connections in the NNN. For instance, electron microscopy was used to obtain the anatomical map of the full nervous system of Caenorhabditis elegans in the mid-1980s and has since been applied to various animal brains, culminating 达到高潮 in the recent anatomical mapping of the complete Drosophila brain.
    - Schefer, L. K. et al. A connectome and analysis of the adult Drosophila central brain. eLife 9, e57443 (2020).
- We, however, will focus mostly on the electrophysiological method, because it is a natural fit to the solid-state
memory network to which the copied biological neuronal networks
will be ‘pasted’.
- Parallelization of intracellular recording has been an important pursuit in neuroscience, because it would enable the functional synaptic connectivity mapping of the NNN. 
- The **Nobel Prize-winning patch clamp** electrode revolutionized neurobiology with its highly sensitive intracellular recording: it can measure not only APs but also subthreshold signals such as postsynaptic potentials (PSPs), and **thus can find a synapse and measure its connection strength**. 
    - However, because the bulky patch clamp cannot scale to a dense array, parallel patch recording has been limited to only about ten neurons, making it difficult to map a network-wide synaptic connectivity. 
    - Conversely, the microelectrode array records from many more neurons to monitor a network, **but this extracellular method is not sensitive enough to record PSPs, making it difficult to study synaptic connections.** 
- The CNEA—the latest version of which integrates 4,096 electronic channels in a CMOS chip with 4,096 vertical nanoelectrodes (Fig. 2a)— **joins intracellular and parallel recording, and thus it can map the NNN’s functional synaptic connectivity (Fig. 2b)**

<div class="ctr"><img src="/NeuroNotes/img/p21.png" width="100%"/></div>

<div class="ctr"><img src="/NeuroNotes/img/p22.png" width="100%"/></div>

- Fig. 2 | Copying the NNN. 
    - a, A CNEA23. 
    - b, Rat neurons on CNEAs (left) and synaptic connectivity map (right) extracted from network-wide intracellular recording data obtained by the CNEA. 
    - c, Intracellular recording at a CNEA channel is enabled by injecting a current Ie into the electrode and by concurrently recording the electrode voltage Ve, which is a scaled version of the membrane potential. Each recorded voltage shown here and in d and e is Ve. Ve serves as an input to the amplifier, whose output voltage is Vamp. 
    - d, Intracellular recording from a pair of connected neurons. **APs of the presynaptic neuron and PSPs of the postsynaptic neuron are time correlated. When APs fire rapidly in the first neuron, synaptic integration occurs in the second neuron (bottom).** 
    - e, In another pair, a histogram of 149 PSP amplitudes of the postsynaptic neuron shows quantization.

### Working with a behavioural neuronal network. 

- **The current version of CNEA determined a synaptic connectivity map from in vitro cultured neurons. These neurons are live, connected and firing, but their random network does not give biological behaviour.** 
- The advance we have made thus far is hence a relatively small
step towards the ultimate goal of copying neuronal networks from
within the brain. 
- Towards this goal, the nanoelectrodes should take different form factors to access 3D neuronal networks found in the
brain, such as nanoelectrodes with long pillar geometry or placed
at each pixel on a macroscopic shank. 
- To start, we are interrogating the neurons’ functional connectivity in **mouse retina** and **olfactory bulb 嗅球/piriform cortex 梨状皮质**. These are attractive initial targets as 
    - they have clear functions, 
    - their inputs can be easily controlled 
    - and there are well-established protocols for preparing ex vivo samples. 
    - At the same time, they are different in terms of their neuronal organizations: 
        - in the retina, cells are arranged into regular lamina; - in the olfactory bulb/piriform cortex, such neat organization is absent.
- As such, these studies will serve as a steppingstone to applying the CNEA to more complicated neuronal circuits in other brain regions and, **ultimately, to probe cortex regions.**
