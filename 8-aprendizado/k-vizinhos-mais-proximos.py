import os

# Suprimir mensagens de INFO e WARNING do TensorFlow
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# Desativar as otimizações do oneDNN (opcional)
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'

# Definir o número máximo de núcleos CPU que o loky deve usar
os.environ['LOKY_MAX_CPU_COUNT'] = '12'  # Substitua '12' pelo número de núcleos físicos

import tensorflow as tf
from tensorflow.keras import layers, models, Input
import numpy as np
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

# 1. Carregar e Pré-processar os Dados
mnist = tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()

x_train = x_train.astype('float32') / 255.0
x_test = x_test.astype('float32') / 255.0

x_train = np.expand_dims(x_train, -1)  # Forma: (60000, 28, 28, 1)
x_test = np.expand_dims(x_test, -1)  # Forma: (10000, 28, 28, 1)


# 2. Definir a Arquitetura da Rede Neural
def create_embedding_model(input_shape=(28, 28, 1), embedding_dim=64):
    inputs = Input(shape=input_shape)
    x = layers.Conv2D(32, (3, 3), activation='relu')(inputs)
    x = layers.MaxPooling2D((2, 2))(x)
    x = layers.Conv2D(64, (3, 3), activation='relu')(x)
    x = layers.MaxPooling2D((2, 2))(x)
    x = layers.Flatten()(x)
    x = layers.Dense(128, activation='relu')(x)
    embeddings = layers.Dense(embedding_dim, activation=None, name='embedding')(x)
    model = models.Model(inputs=inputs, outputs=embeddings)
    return model


embedding_dim = 64
embedding_model = create_embedding_model(embedding_dim=embedding_dim)
embedding_model.summary()

# 3. Treinar a Rede Neural
num_classes = 10
model = models.Sequential([
    embedding_model,
    layers.Dense(num_classes, activation='softmax')
])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(x_train, y_train, epochs=5, batch_size=128, validation_split=0.1)

# 4. Extrair os Embeddings
encoder = models.Model(inputs=embedding_model.input, outputs=embedding_model.output)

train_embeddings = encoder.predict(x_train)  # Forma: (60000, 64)
test_embeddings = encoder.predict(x_test)  # Forma: (10000, 64)

# 5. Pré-processamento dos Embeddings
# Normalizar os embeddings
scaler = StandardScaler()
train_embeddings_scaled = scaler.fit_transform(train_embeddings)
test_embeddings_scaled = scaler.transform(test_embeddings)

# Reduzir a dimensionalidade com PCA
pca = PCA(n_components=32)  # Reduzindo para 32 dimensões
train_embeddings_pca = pca.fit_transform(train_embeddings_scaled)
test_embeddings_pca = pca.transform(test_embeddings_scaled)

# 6. Implementar o k-NN com scikit-learn
# Selecionar uma amostra do conjunto de treinamento para k-NN
sample_size = 10000  # Ajuste conforme a capacidade de memória
sample_train_embeddings = train_embeddings_pca[:sample_size]
sample_train_labels = y_train[:sample_size]

# Definir o classificador k-NN
k = 5
knn = KNeighborsClassifier(n_neighbors=k, algorithm='auto', n_jobs=-1)

# Treinar o classificador k-NN
knn.fit(sample_train_embeddings, sample_train_labels)

# Prever os rótulos do conjunto de teste
predictions = knn.predict(test_embeddings_pca)

# Avaliar a acurácia
accuracy = accuracy_score(y_test, predictions)
print(f'Acurácia do k-NN com k={k}: {accuracy * 100:.2f}%')
