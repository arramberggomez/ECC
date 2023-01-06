# Plain Text Encryption Using ECC

This repository contains code for the implementation of the encryption scheme described in the poster below.

![Symposium Poster](EEC_Spring_2022.jpg)

# Instructions for Use

1. Install SageMath

Download binaries [here](https://www.sagemath.org/download.html) or install from source [here](https://doc.sagemath.org/html/en/installation/index.html).

2. Run Notebook

Clone this repository and cd into it.
```
git clone https://github.com/arramberggomez/ECC.git
```
```
cd ECC
```
Start the sage kernel.
```
sage -n jupyter
```
You will now be redirected to a web browser window that contains all of the files in this repository.
Open the file titled ECC_text_mapping.ipynb and run it.
To encrypt a different message than the one provided, replace the contents of secret_message.txt with the desired message and run the notebook. The encrypted message - encrypted_message.txt - will then be updated.


