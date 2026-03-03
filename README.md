# Bigram Text Generator

[cite_start]**Bigram Text Generator** is a minimalist Natural Language Processing (NLP) tool that demonstrates the core logic of predictive text models[cite: 1]. [cite_start]By analyzing a source text, it builds a statistical map of word pairs (bigrams) to generate original, human-like sentences based on the probability of one word following another[cite: 1].

## The Advantage: Why Bigrams?

In the world of AI, Large Language Models (LLMs) require massive datasets and GPU power. [cite_start]The **Bigram Model** offers a "back-to-basics" approach that is incredibly efficient for understanding the fundamentals of generative AI[cite: 1].

* [cite_start]**Near-Instant Processing**: Because it only looks at the relationship between two adjacent words, the model builds its entire "knowledge base" in milliseconds[cite: 1].
* [cite_start]**Contextual Fluidity**: By using a dictionary-based look-up, the generator creates sentences that maintain the local vocabulary of the source text[cite: 1].
* [cite_start]**Zero Dependencies**: It runs entirely on the CPU using Python's standard `random` module, making it a perfect educational tool[cite: 1].
* [cite_start]**Predictive Logic**: Unlike random word scramblers, this model ensures that every word generated was actually preceded by the previous word in the original training data[cite: 1].



## Project Structure

The project is built on two simple components:

1.  [cite_start]**`bigram_Model.py`**: The engine that handles file reading, builds the dictionary-based model, and runs the generation loop[cite: 1].
2.  [cite_start]**`data.txt`**: The training set containing descriptive prose about a quiet town, Sarah's routine, and the local atmosphere[cite: 2, 3, 10].

## Installation & Usage

1.  [cite_start]Ensure you have a file named `data.txt` in the same directory as the script[cite: 1].
2.  Run the generator:
    ```bash
    python bigram_Model.py
    ```

### Example Output
Starting with the seed word **"the"**, the model might produce[cite: 1]:
> "the sun rose early over the quiet town had its own rhythm, a comforting pattern that repeated every day."

## How it Works (The Logic)

The model operates in three distinct phases:

### 1. Data Ingestion
The script reads `data.txt` and splits the text into a list of individual words[cite: 1].

### 2. Building the Model
The script iterates through the words and stores every word pair in a dictionary[cite: 1]:
* **Key**: The current word[cite: 1].
* **Value**: A list of every word that has ever followed that key in the text[cite: 1].

### 3. Generation Loop
The model starts with a seed word (e.g., "the") and uses `random.choice()` to pick one of its known followers[cite: 1]. [cite_start]This newly chosen word then becomes the "current word" for the next selection, repeating for the specified `length`[cite: 1].

| Variable | Value | Function |
| :--- | :--- | :--- |
| `start` | "the" | [cite_start]The seed word that begins the sentence[cite: 1]. |
| `length` | 40 | [cite_start]The total number of words to generate[cite: 1]. |
| `model` | `{}` | [cite_start]The dictionary storing the bigram relationships[cite: 1]. |

## Training Data Content
The included `data.txt` provides a peaceful narrative used for training, including:
* **Morning Routines**: Sarah stepping outside with tea and birds chirping[cite: 2, 3].
* **Town Life**: Delivery trucks, children on bicycles, and an old man walking his dog[cite: 6, 8, 9].
* **Nature**: Sunlight on the windowsill, clouds drifting, and rain tapping on rooftops[cite: 4, 12, 24].

---
