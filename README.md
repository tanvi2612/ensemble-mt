# Ensemble Machine Translation Models

## Introduction
The project aims to explore and incorporate the benefits of multiple MT systems into one ensemble model, to improve upon the performances of the individual baselines. Find the project assets [here](https://drive.google.com/drive/folders/1C9PympPPGheRWxRlwtMHiwPBoq8yZ783?usp=sharing).

## In this Repository
```bash
.
├── README.md
├── checkpoints                                     # directory conataining zipped checkpoints
│   ├── openNMT-checkpoints.zip                     # openNMT checkpoints, not including the final model
│   └── pbmt-moses-training-checkpoints.zip         # PBMT checkpoints
├── corpus                                          # directory containing split and processed en-hi corpus
│   ├── src-test.tok.true.txt
│   ├── src-test.tok.txt
│   ├── src-test.txt
│   ├── src-train.tok.txt
│   ├── src-train.txt
│   ├── src-val.tok.true.txt
│   ├── src-val.tok.txt
│   ├── src-val.txt
│   ├── tgt-test.tok.txt
│   ├── tgt-test.txt
│   ├── tgt-train.txt
│   ├── tgt-val.tok.txt
│   ├── tgt-val.txt
│   ├── train.en
│   ├── train.hi
│   └── truecase-model.en                           # truecaser model trained on 
├── dataset                                         # directory containing the OpenSubtitles en-hi corpus
│   ├── OpenSubtitles.en-hi.en
│   ├── OpenSubtitles.en-hi.hi
│   ├── OpenSubtitles.en-hi.ids
│   └── 
├── dl4mt-multi-src.zip                             # multi source NMT source code
├── docs
├── lm                                              # directory containing language models
│   ├── arpa.hi                                     # trigram KEN LM
│   ├── bigram-lm                                   # pickled nltk bigram LM
│   └── blm.hi                                      # binarized KEN LM
├── logs                                            # directory containing cmd logs
│   └── pbmt-moses-test.out
├── moses.zip                                       # moses source code
├── openNMT.zip                                     # openNMT source code
├── outputs                                         # directory containing predicted sentences
│   ├── ensemble-predictions.txt
│   ├── openNMT-predicted_test.txt
│   ├── openNMT-predictions.txt
│   └── pbmt-moses.translated.hi
└── scripts                                         # directory containing helper scripts
    ├── perplexity.py
    ├── preprocess.py
    └── split.py

8 directories, 35 files
```

## Authors
Chaitanya Agarwal, Tanvi Kamble
