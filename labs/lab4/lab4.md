## Tasks
1. Load the MNIST dataset.
2. Apply PCA and t-SNE on the MNIST dataset. Try the test dataset. t-SNE is time-consuming, so you can use a subset of the dataset.
3. Visualize the results of PCA and t-SNE.<br>
4. Compare the results of PCA and t-SNE.<br>
There are more dense colored point in tSNE than PCA which means that tSNE was able to capture the dense relationship of data in high dimenson to lower dimension however PCA couldn't.Since PCA focuses on preserving global structure and variance, it may not effectively capture the local relationships and clusters present in the data, resulting in a sparse distribution of colored dots.<br>
t-SNE plots tend to exhibit dense clusters of colored dots, reflecting the local similarities and groupings present in the original high-dimensional space.<br>

5. Discuss the pros and cons of PCA and t-SNE.

PCA (Principal Component Analysis):

Pros:
i. Computational Efficiency: PCA is computationally efficient and can handle large datasets with ease.<br>
ii. Interpretability: PCA provides interpretable results by representing data in terms of principal components, which are linear combinations of the original features.<br>
iii. Preserves Global Structure: PCA preserves global structure and captures the directions of maximum variance in the data.<br>
iv. Linear Transformations: PCA performs linear transformations, making it suitable for linearly separable data.<br>

Cons:<br>
i. Linearity Assumption: PCA assumes that the underlying data distribution is linear. It may not effectively capture complex non-linear relationships present in the data.<br>
ii. Sensitivity to Outliers: PCA is sensitive to outliers, as it aims to maximize variance and may be influenced by extreme values.<br>
iii. Limited for Non-linear Data: PCA may not effectively represent non-linear structures and may lose information when applied to highly non-linear data.<br>

tSNE

pros:
i. Non-linear Embedding: t-SNE is effective in capturing non-linear relationships and structures in the data, making it suitable for complex datasets.<br>
ii. Preserves Local Structure: t-SNE preserves local structures and relationships, emphasizing clustering and grouping of data points.<br>
iii. Visual Interpretation: t-SNE produces visually appealing plots that effectively highlight clusters and patterns in the data, facilitating intuitive interpretation.<br>
iv. Robust to Outliers: t-SNE is robust to outliers and noise, as it focuses on local relationships and is less influenced by extreme values.<br>

cons:<br>
i. High Computational Cost: t-SNE is computationally expensive, especially for large datasets, and may require careful tuning of parameters for optimal performance.<br>
ii. Non-deterministic: t-SNE results can vary across different runs due to its stochastic nature, making it challenging to reproduce results exactly.<br>
iii. Overcrowding: In t-SNE plots, dense clusters of points may obscure underlying structures, leading to overcrowding and potential loss of detail in visualization.<br>
iv. Interpretation Challenges: While t-SNE plots are visually informative, interpretation can be subjective and may require domain knowledge to discern meaningful patterns from the visualization.