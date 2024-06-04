**Dataset Description**

This supplementary material contains five primary dataset folders, aimed at helping readers better understand and verify the experimental results:

1. **Basic OCKR Dataset**: This folder contains the training data used in Section 4.1 "Basic OCKR Results."

2. **Complete Reasoning Data Dataset**: This folder contains the training data used in Section 4.2 "Complete Reasoning Data results."

3. **Chain-of-Thought Training Dataset**: This folder contains the training data used in Section 4.3 "Chain-of-Thought Training."

4. **Cross-Lingual Dataset**: This folder contains the training and testing data used in Section 4.4 "Cross-Lingual."

5. **Test Dataset**: This folder contains the test data used in Sections 4.1 to 4.3.

All datasets are in JSON format. Each test data response includes three parts: the model-generated reference answer, the correct answer for exact match detection (label), and an identifier for distinguishing the type of knowledge (type). For example, a knowledge triplet would be appended after the model-generated answer in the format `[[label:2010]][[type:(y, birth year, year)]]`. If it is a target knowledge triad it will be labeled [[type:targe]].
