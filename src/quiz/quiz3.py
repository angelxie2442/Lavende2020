# ========================================================================
# Copyright 2020 Emory University
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ========================================================================
from typing import Set, Optional, List
from nltk.corpus import wordnet as wn
from nltk.corpus.reader import Synset
import numpy as np


def antonyms(word: str, pos: Optional[str] = None) -> Set[str]:
    ants = set()
    for syn in wn.synsets(word, pos): ##each synset
        if syn is not None:
            for l in syn.lemmas(): ##each synonym of that synset
                if l is not None:
                    for ant in l.antonyms(): ##each antonym of that synonym
                        if ant is not None:
                            ants.add(ant)
    return list(ants)
    pass

def lch_paths(word_0: str, word_1: str) -> List[List[Synset]]:
    paths=[]
    lchs=set()
    senses_0=wn.synsets(word_0)
    senses_1=wn.synsets(word_1)
    for syn_0 in senses_0:
        for syn_1 in senses_1:
            ##Different combination of senses of word0 and word1
            for lch in syn_0.lowest_common_hypernyms(syn_1):
                if lch is not None:
                    ##add any new lch to the set of lchs
                    lchs.add(lch)
    ##for each unique lch, find all possible paths to roots of that lch
    for h in list(lchs):
        paths.extend(h.hypernym_paths())
    return paths
    pass


if __name__ == '__main__':
    print(antonyms('buy', pos='v'))
    for path in lch_paths('dog', 'cat'):
        print(path)