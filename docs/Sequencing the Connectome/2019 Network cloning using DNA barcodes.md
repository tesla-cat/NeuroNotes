
**One possible solution for recreating the target network is to mark each neuron of the tabula rasa (白纸) network with individual barcode tags and to distribute the barcode pairs into synapses according to these tags. The unoccupied synapses of the tabula rasa network would subsequently be eliminated.**

**Implementing this mechanism practically would require a global supervising mechanism that keeps track of unique label assignments and appropriate barcode placements. Such mechanism is therefore not biologically plausible.**

Instead, here we formulate a fully local procedure for recreating the target network in the tabula rasa network in which **processes in each cell rely only on the information available to each cell.** Thus, the target network emerges as a result of `self-organization` of barcodes in the tabula rasa. 

- The barcode pairs are initially arranged randomly.
- The barcodes are rearranged in the network via three types of local moves. 
    - First, each barcode can be reinserted in the synapse between the same pair of cells in different orientation ("flips"). 
    - Second, the barcodes can jump from one synapse to another synapse of the same cell ("jumps"). 
    - Finally, two barcodes located in the same neuron can trade places ("swaps"). 
- The moves minimize the cost function defined by Eq. 1. Minimization of the cost function forces all barcodes facing every neuron to be the same. This arrangement is called OBOC (one-barcode–one-cell).
- To practically implement these three moves, we select two synapses of the same neuron at random, ensure that at least one of them contains a barcode pair, and swap the pairs, even if source and destination are the same or one of them is empty. In implementing these moves, we keep track of the direction of barcode pairs and synapses, that is, barcode pairs are introduced into synapses of the correct orientation. We ensure that the described moves are local in that **the barcode pairs are only relocated between synapses of the same neuron.**

<div class="ctr"><img src="/img/p8.png" width="600"/></div>

# TODO

